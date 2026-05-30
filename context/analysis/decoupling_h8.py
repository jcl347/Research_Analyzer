# H8 leg (b) + (a): EKC-vs-trap decoupling test and Omega-gap calibration
# EXECUTED this session (results in context/results.md). Pure numpy (no pandas/statsmodels;
# two-way FE + cluster-robust SE implemented by hand). Python 3.x, numpy only.
#
# Honest identification note: dln(tau)~dln(Y) is mechanically beta_emissions-1 because
# tau=CO2/GDP has GDP on both sides (stress-test G1/G2). The real estimand is the
# emissions-output elasticity beta from dln(CO2)~dln(GDP).

import csv, math, urllib.request
import numpy as np
from collections import defaultdict

URL = "https://github.com/owid/co2-data/raw/master/owid-co2-data.csv"
PATH = r"C:\Users\jcl34\AppData\Local\Temp\owid-co2-data.csv"

def download():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(PATH, "wb") as f:
        f.write(r.read())

def load():
    raw = []
    with open(PATH, encoding="utf-8") as f:
        rd = csv.reader(f); next(rd)
        for r in rd:
            iso = r[2]
            if len(iso) != 3 or iso.startswith("OWID"):  # real countries only
                continue
            try:
                yr = int(r[1]); pop = float(r[3]); gdp = float(r[4]); co2 = float(r[7])
            except ValueError:
                continue
            if gdp <= 0 or co2 <= 0 or pop <= 0:
                continue
            raw.append((iso, yr, gdp, co2, pop))
    return raw

def build(raw, minyr, isoset=None):
    by = defaultdict(dict)
    for iso, yr, gdp, co2, pop in raw:
        if yr < minyr or (isoset is not None and iso not in isoset):
            continue
        by[iso][yr] = (gdp, co2)
    iso_l, yr_l, dlg, dlc = [], [], [], []
    for iso, d in by.items():
        for yr in sorted(d):
            if yr - 1 in d:
                g1, c1 = d[yr - 1]; g2, c2 = d[yr]
                dlg.append(math.log(g2) - math.log(g1)); dlc.append(math.log(c2) - math.log(c1))
                iso_l.append(iso); yr_l.append(yr)
    return iso_l, yr_l, np.array(dlg), np.array(dlc)

def fe_beta(iso_l, yr_l, dlg, dlc):
    """Two-way (country+year) FE slope of dlc on dlg, cluster-robust SE by country."""
    isos = sorted(set(iso_l)); years = sorted(set(yr_l))
    ii = np.array([isos.index(x) for x in iso_l]); ty = np.array([years.index(x) for x in yr_l])
    N, G, T = len(dlg), len(isos), len(years)
    def dm(v):
        v = v.astype(float).copy()
        for _ in range(3000):
            p = v.copy()
            v = v - (np.bincount(ii, v) / np.bincount(ii))[ii]
            v = v - (np.bincount(ty, v) / np.bincount(ty))[ty]
            if np.max(np.abs(v - p)) < 1e-12:
                break
        return v
    yd, xd = dm(dlc), dm(dlg)
    b = float(xd @ yd / (xd @ xd)); e = yd - b * xd
    meat = sum(float(xd[ii == g] @ e[ii == g]) ** 2 for g in range(G))
    K = 1 + (G - 1) + (T - 1); corr = (G / (G - 1)) * ((N - 1) / (N - K))
    se = math.sqrt(meat / (xd @ xd) ** 2 * corr)
    return b, se, N, G

def main():
    download()
    raw = load()
    # income split by mean GDP per capita over 1990+
    pc = defaultdict(list)
    for iso, yr, gdp, co2, pop in raw:
        if yr >= 1990:
            pc[iso].append(gdp / pop)
    mpc = {i: np.mean(v) for i, v in pc.items() if v}
    med = np.median(list(mpc.values()))
    rich = {i for i, v in mpc.items() if v >= med}
    poor = {i for i, v in mpc.items() if v < med}

    print("=== H8b: emissions-output elasticity beta + intensity trend ===")
    for label, minyr, iss in [("Full 1821+", 1821, None), ("1971+", 1971, None),
                              ("1990+", 1990, None), ("2000+", 2000, None),
                              ("1990+ RICH", 1990, rich), ("1990+ POOR", 1990, poor)]:
        il, yl, dlg, dlc = build(raw, minyr, iss)
        b, se, N, G = fe_beta(il, yl, dlg, dlc)
        dtau = dlc - dlg
        print(f"{label:12} N={N:5d} ctry={G:3d}  beta={b:+.3f}(SE {se:.3f})  "
              f"mean dln(tau)={dtau.mean()*100:+.2f}%/yr  share falling={np.mean(dtau<0)*100:.1f}%")

    print("\n=== H8a: implied output gap 1-(Omega*)^(1/(1-alpha)), waste drag, alpha=0.3 ===")
    for tau in [0.02, 0.05, 0.10, 0.20, 0.30]:
        gaps = [f"{(1-(1-tau)**(psi/0.7))*100:5.1f}%" for psi in (1, 2, 3)]
        print(f"  tau={tau:.2f}  psi=1/2/3: " + " ".join(gaps))

if __name__ == "__main__":
    main()
