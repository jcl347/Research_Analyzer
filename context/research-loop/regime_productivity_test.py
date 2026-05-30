# Fine-tuning probe: is the pollution -> productivity drag regime-conditional (decoupler vs not)?
# EXECUTED this session. Pure numpy. Merges World Bank labor productivity with OWID intensity.
# Result (NULL): no detectable macro regime-conditional drag -> consistent with the zeta(H)
# "masking" hypothesis (loss invisible in aggregate productivity); redirects to micro tests.
#
# Data: WB SL.GDP.PCAP.EM.KD (GDP per person employed) via api.worldbank.org;
#       OWID owid-co2-data.csv (co2_per_gdp = tau, gdp, population).

import csv, json, math
import numpy as np
import urllib.request
from collections import defaultdict

def fetch_wb(path):
    url = "https://api.worldbank.org/v2/country/all/indicator/SL.GDP.PCAP.EM.KD?format=json&per_page=20000&date=1991:2022"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=240) as r:
        json.dump(json.loads(r.read().decode("utf-8"))[1], open(path, "w"))

def main():
    wb = r"C:\Users\jcl34\AppData\Local\Temp\wb_labprod.json"
    owid = r"C:\Users\jcl34\AppData\Local\Temp\owid-co2-data.csv"
    LP = defaultdict(dict)
    for x in json.load(open(wb)):
        iso = x.get("countryiso3code") or ""
        if len(iso) == 3 and x["value"] is not None:
            LP[iso][int(x["date"])] = float(x["value"])
    TAU = defaultdict(dict)
    with open(owid, encoding="utf-8") as f:
        rd = csv.reader(f); next(rd)
        for r in rd:
            iso = r[2]
            if len(iso) != 3 or iso.startswith("OWID"):
                continue
            try:
                yr = int(r[1]); tau = float(r[17])
            except ValueError:
                continue
            if tau > 0:
                TAU[iso][yr] = tau
    # classify decoupler by 1991+ mean dln(tau)
    regime = {}
    for iso, d in TAU.items():
        dl = [math.log(d[y]) - math.log(d[y-1]) for y in sorted(d) if y >= 1991 and y-1 in d]
        if len(dl) >= 8:
            regime[iso] = "decoupler" if np.mean(dl) < 0 else "non_decoupler"
    # build annual panel
    iso_l, yr_l, dlLP, lag_lntau, lag_lnLP, nondec = [], [], [], [], [], []
    for iso in set(LP) & set(TAU) & set(regime):
        for t in sorted(set(LP[iso]) & set(TAU[iso])):
            if t-1 in LP[iso] and t-1 in TAU[iso]:
                dlLP.append(math.log(LP[iso][t]) - math.log(LP[iso][t-1]))
                lag_lntau.append(math.log(TAU[iso][t-1])); lag_lnLP.append(math.log(LP[iso][t-1]))
                nondec.append(1.0 if regime[iso] == "non_decoupler" else 0.0)
                iso_l.append(iso); yr_l.append(t)
    y = np.array(dlLP); X0 = np.array(lag_lntau); X1 = np.array(lag_lnLP); D = np.array(nondec)
    isos = sorted(set(iso_l)); years = sorted(set(yr_l))
    ii = np.array([isos.index(a) for a in iso_l]); ty = np.array([years.index(a) for a in yr_l])
    N, G, T = len(y), len(isos), len(years)

    def dm(v):
        v = v.astype(float).copy()
        for _ in range(3000):
            p = v.copy()
            v = v - (np.bincount(ii, v) / np.bincount(ii))[ii]
            v = v - (np.bincount(ty, v) / np.bincount(ty))[ty]
            if np.max(np.abs(v - p)) < 1e-12:
                break
        return v

    def feols(y, cols):
        yd = dm(y); Xd = np.column_stack([dm(c) for c in cols])
        XtX = Xd.T @ Xd; beta = np.linalg.solve(XtX, Xd.T @ yd); e = yd - Xd @ beta
        inv = np.linalg.inv(XtX); meat = np.zeros((Xd.shape[1],)*2)
        for g in range(G):
            m = ii == g; s = Xd[m].T @ e[m]; meat += np.outer(s, s)
        K = Xd.shape[1] + (G-1) + (T-1); corr = (G/(G-1)) * ((N-1)/(N-K))
        se = np.sqrt(np.diag(inv @ meat @ inv * corr))
        return beta, se

    print(f"panel N={N} countries={G} years {min(years)}-{max(years)}")
    print(f"mean dln(LP): decouplers={y[D==0].mean()*100:+.2f}%/yr  non-decouplers={y[D==1].mean()*100:+.2f}%/yr")
    b, se = feols(y, [X0, X1])
    print(f"(1) lag ln(tau) b={b[0]:+.4f} (t={b[0]/se[0]:+.2f});  convergence lag ln(LP) b={b[1]:+.4f} (t={b[1]/se[1]:+.2f})")
    b2, se2 = feols(y, [X0, X0*D, X1])
    print(f"(2) nonDecoupler x lag ln(tau) b={b2[1]:+.4f} (t={b2[1]/se2[1]:+.2f})  [predicted <0; found ns/wrong-sign]")

if __name__ == "__main__":
    main()
