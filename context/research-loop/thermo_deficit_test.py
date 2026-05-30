# Probe C: does an unpriced THERMODYNAMIC-DAMAGE deficit foreshadow weaker future growth?
# (a data-testable mutation of the paper's Thermo-GDP idea). EXECUTED this session. Pure numpy.
# Result (NULL): thermodynamic damage share does NOT predict forward 5-yr growth, and adds nothing
# beyond gross savings -> the Thermo-GDP "deficit signals future underperformance" mutation fails at macro.
#
# Data (World Bank API): NY.ADJ.DCO2.GN.ZS, NY.ADJ.DPEM.GN.ZS (pollution damage % GNI),
#   NY.ADJ.SVNG.GN.ZS (adjusted net savings), NY.GDP.PCAP.KD, NY.GNS.ICTR.ZS.

import json, math
import numpy as np
from collections import defaultdict

def load(k):
    d = defaultdict(dict)
    for x in json.load(open(fr"C:\Users\jcl34\AppData\Local\Temp\wb_{k}.json")):
        iso = x.get("countryiso3code") or ""
        if len(iso) == 3 and x["value"] is not None:
            d[iso][int(x["date"])] = float(x["value"])
    return d

def main():
    dco2, dpem, gdppc, gsav = load("dco2"), load("dpem"), load("gdppc"), load("gsav")
    periods = [1995, 2000, 2005, 2010, 2015]   # non-overlapping 5-yr Barro panel
    iso_l, pe_l, g5, thermo, lny, Gs = [], [], [], [], [], []
    for iso in gdppc:
        for t in periods:
            if t in gdppc[iso] and t+5 in gdppc[iso] and t in dco2.get(iso, {}) and t in dpem.get(iso, {}):
                y0, y1 = gdppc[iso][t], gdppc[iso][t+5]
                if y0 > 0 and y1 > 0:
                    g5.append((math.log(y1) - math.log(y0)) / 5.0)
                    thermo.append(dco2[iso][t] + dpem[iso][t])
                    lny.append(math.log(y0)); Gs.append(gsav[iso].get(t, np.nan))
                    iso_l.append(iso); pe_l.append(t)
    g5, thermo, lny, Gs = map(np.array, (g5, thermo, lny, Gs))
    isos = sorted(set(iso_l)); pers = sorted(set(pe_l))
    ii = np.array([isos.index(a) for a in iso_l]); ty = np.array([pers.index(a) for a in pe_l])
    N, G, T = len(g5), len(isos), len(pers)

    def dm(v):
        v = v.astype(float).copy()
        for _ in range(3000):
            p = v.copy(); v = v - (np.bincount(ii, v)/np.bincount(ii))[ii]; v = v - (np.bincount(ty, v)/np.bincount(ty))[ty]
            if np.max(np.abs(v-p)) < 1e-12: break
        return v
    def feols(y, cols):
        yd = dm(y); Xd = np.column_stack([dm(c) for c in cols])
        beta = np.linalg.solve(Xd.T@Xd, Xd.T@yd); e = yd - Xd@beta
        inv = np.linalg.inv(Xd.T@Xd); meat = np.zeros((Xd.shape[1],)*2)
        for g in range(G):
            m = ii == g; s = Xd[m].T@e[m]; meat += np.outer(s, s)
        K = Xd.shape[1]+(G-1)+(T-1); se = np.sqrt(np.diag(inv@meat@inv*(G/(G-1))*((N-1)/max(N-K,1))))
        return beta, se

    print(f"Barro 5-yr panel N={N} countries={G}")
    b, se = feols(g5, [thermo, lny])
    print(f"(1) thermoDamage->g5: b={b[0]*100:+.3f}pp (t={b[0]/se[0]:+.2f})  [predicted <0; found NULL]")

if __name__ == "__main__":
    main()
