# Anchor regression + discriminating cognitive-channel test (Thermo-Ecological Solow)
# AGENT-GENERATED STARTER CODE from the hypothesis-test-system workflow. Review before running.
# Data access paths are in context/data-sources.md. Requires: pandas, linearmodels, statsmodels.


# =====================================================================
# Sec-6.1 anchor regression + discriminating cognitive-channel test
# Python (pandas + linearmodels). Requires: pip install pandas numpy linearmodels statsmodels
#
# NAMED DATASETS (download first; see dataIntegrityNote for URLs):
#   pwt   = PWT 10.01 Data sheet  -> columns: countrycode, year, rtfpna, hc, labsh, rgdpna, emp, pop
#   co2   = OWID co2-intensity    -> columns: iso_code(Code), year, emissions_total_per_gdp   (tau proxy)
#   pm    = WDI EN.ATM.PM25.MC.M3 -> columns: iso3, year, pm25
#   hale  = WHO WHOSIS_000002     -> columns: SpatialDim(iso3), TimeDim(year), NumericValue(hale) [Dim1=SEX_BTSX]
#   wdi   = WDI macro             -> columns: iso3, year, gdp_pc(NY.GDP.PCAP.KD), s(NY.GNS.ICTR.ZS), n(SP.POP.GROW)
# =====================================================================
import numpy as np, pandas as pd
from linearmodels.panel import PanelOLS

# ---- 1. Load (adjust paths/parsers to the files you downloaded) ----
pwt  = pd.read_excel("pwt100.xlsx", sheet_name="Data")[["countrycode","year","rtfpna","hc","labsh","rgdpna","emp","pop"]].rename(columns={"countrycode":"iso3"})
co2  = pd.read_csv("co2-intensity.csv").rename(columns={"Code":"iso3","emissions_total_per_gdp":"tau"})[["iso3","year","tau"]]
pm   = pd.read_csv("pm25_wdi.csv").rename(columns={})[["iso3","year","pm25"]]
hale = pd.read_csv("hale_who.csv")
hale = hale[hale["Dim1"]=="SEX_BTSX"].rename(columns={"SpatialDim":"iso3","TimeDim":"year","NumericValue":"hale"})[["iso3","year","hale"]]
wdi  = pd.read_csv("wdi_macro.csv")[["iso3","year","gdp_pc","s","n"]]

# ---- 2. Merge to a country-year panel ----
df = (pwt.merge(co2, on=["iso3","year"], how="inner")
          .merge(pm,  on=["iso3","year"], how="left")
          .merge(hale,on=["iso3","year"], how="left")
          .merge(wdi, on=["iso3","year"], how="left")
          .sort_values(["iso3","year"]))

# ---- 3. Build LHS = dln(TFP) and lagged RHS; H proxy = HALE (primary) ----
df["dln_tfp"] = df.groupby("iso3")["rtfpna"].transform(lambda x: np.log(x).diff())
df["tau_l1"]  = df.groupby("iso3")["tau"].shift(1)            # P1: b1<0
df["lnH_l1"]  = np.log(df.groupby("iso3")["hale"].shift(1))    # P2/b2>0
df["ln_gdp_l1"]= np.log(df.groupby("iso3")["gdp_pc"].shift(1)) # convergence control (also tests P5 via interaction)
df["lnH_alt_l1"]= -np.log(df.groupby("iso3")["pm25"].shift(1)) # inverse-PM2.5 H proxy (NOTE F10: invalid if PM2.5 hits TFP via tau)
df = df.set_index(["iso3","year"])

# ---- 4a. ANCHOR REGRESSION (Eq. §6.1): country FE + year FE, cluster by country ----
m_anchor = PanelOLS.from_formula(
    "dln_tfp ~ tau_l1 + lnH_l1 + ln_gdp_l1 + s + n + EntityEffects + TimeEffects",
    data=df, drop_absorbed=True).fit(cov_type="clustered", cluster_entity=True)
print(m_anchor)   # expect tau_l1 coef<0, lnH_l1 coef>0 PER THE PAPER

# ---- 4b. DISCRIMINATING COGNITIVE-CHANNEL TEST (addresses G12 falsifiability) ----
# The ONLY prediction that separates the thermo mechanism from plain development/EKC is zeta(H):
# pollution erodes COGNITION, so its drag must be (i) larger in cognitively-intensive sectors and
# (ii) operate THROUGH a contemporaneous productivity hit, not merely track income.
# Test 1: horse-race tau against pure development. If b1 -> 0 once ln(GDPpc) & a rich-control set
#         enter, P1 is just EKC (NOT falsifying the mechanism). Survival of b1<0 net of income is the test.
m_devhorse = PanelOLS.from_formula(
    "dln_tfp ~ tau_l1 + lnH_l1 + ln_gdp_l1 + I(ln_gdp_l1**2) + s + n + EntityEffects + TimeEffects",
    data=df, drop_absorbed=True).fit(cov_type="clustered", cluster_entity=True)
print(m_devhorse)
# Test 2 (the sharp one): sector panel df_sec with cog_intensity in [0,1] per sector.
#   dln(LP)_ist = c1*pm25_l1 + c2*(pm25_l1 * cog_intensity_s) + FE; PREDICT c2<0 (P2).
#   A pure income story predicts c2=0 (income doesn't differentially hit cognitive sectors via PM2.5).
# m_cog = PanelOLS.from_formula(
#     "dln_lp ~ pm25_l1 + pm25_l1:cog_intensity + EntityEffects + TimeEffects",
#     data=df_sec.set_index(['sector_iso','year']), drop_absorbed=True
#     ).fit(cov_type="clustered", cluster_entity=True)
# print(m_cog)   # c2<0 => cognitive-channel signature; c2~0 => indistinguishable from development
