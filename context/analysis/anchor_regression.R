# Anchor regression + discriminating cognitive-channel test (Thermo-Ecological Solow)
# AGENT-GENERATED STARTER CODE from the hypothesis-test-system workflow. Review before running.
# Data access paths are in context/data-sources.md. Requires: fixest, modelsummary, data.table.


# =====================================================================
# Sec-6.1 anchor regression + discriminating cognitive-channel test  (R)
# Requires: install.packages(c("fixest","data.table"))
#
# NAMED DATASETS (download first; URLs in dataIntegrityNote):
#   PWT 10.01 "Data" sheet : iso3=countrycode, year, rtfpna, hc, labsh, rgdpna, emp, pop
#   OWID co2-intensity     : iso3=Code, year, tau=emissions_total_per_gdp        (tau proxy)
#   WDI EN.ATM.PM25.MC.M3   : iso3, year, pm25
#   WHO WHOSIS_000002       : iso3=SpatialDim, year=TimeDim, hale=NumericValue (Dim1=='SEX_BTSX')
#   WDI macro               : iso3, year, gdp_pc(NY.GDP.PCAP.KD), s(NY.GNS.ICTR.ZS), n(SP.POP.GROW)
# =====================================================================
library(data.table); library(fixest)

# ---- 1. Load (readxl::read_excel for the PWT .xlsx 'Data' sheet) ----
pwt  <- as.data.table(readxl::read_excel("pwt100.xlsx", sheet="Data"))[
          , .(iso3=countrycode, year, rtfpna, hc, labsh, rgdpna, emp, pop)]
co2  <- fread("co2-intensity.csv")[, .(iso3=Code, year, tau=emissions_total_per_gdp)]
pm   <- fread("pm25_wdi.csv")[,  .(iso3, year, pm25)]
hale <- fread("hale_who.csv")[Dim1=="SEX_BTSX", .(iso3=SpatialDim, year=TimeDim, hale=NumericValue)]
wdi  <- fread("wdi_macro.csv")[, .(iso3, year, gdp_pc, s, n)]

# ---- 2. Merge to country-year panel ----
df <- Reduce(function(a,b) merge(a,b, by=c("iso3","year"), all.x=TRUE),
             list(pwt, co2, pm, hale, wdi))
setorder(df, iso3, year)

# ---- 3. LHS = dln(TFP); lagged RHS; H proxy = HALE (primary) ----
df[, dln_tfp  := log(rtfpna) - shift(log(rtfpna)), by=iso3]      # within-country TFP growth
df[, tau_l1   := shift(tau),            by=iso3]                  # P1: b1<0
df[, lnH_l1   := shift(log(hale)),      by=iso3]                  # P2/b2>0
df[, lngdp_l1 := shift(log(gdp_pc)),    by=iso3]                  # convergence control
df[, lnH_altl1:= shift(-log(pm25)),     by=iso3]                  # inverse-PM2.5 H proxy (F10 caveat: endogenous)

# ---- 4a. ANCHOR REGRESSION: dln(TFP) ~ tau_{t-1} + lnH_{t-1} + X | country + year FE, cluster by country
m_anchor <- feols(dln_tfp ~ tau_l1 + lnH_l1 + lngdp_l1 + s + n | iso3 + year,
                  data = df, cluster = ~iso3)
summary(m_anchor)        # PAPER PREDICTS: coef(tau_l1) < 0 ,  coef(lnH_l1) > 0

# ---- 4b. DISCRIMINATING COGNITIVE-CHANNEL TEST (addresses critique G12 falsifiability) ----
# P1/P2/P5 are ALSO implied by plain development/EKC. The zeta(H) cognitive channel is the
# ONLY discriminating signature. Two-part design:

# Test 1 - development horse-race: add ln(GDPpc) and its square. If tau_l1 collapses to ~0,
#          the result is EKC, not the thermo mechanism. Survival of b1<0 net of income = pass.
m_horse <- feols(dln_tfp ~ tau_l1 + lnH_l1 + lngdp_l1 + I(lngdp_l1^2) + s + n | iso3 + year,
                 data = df, cluster = ~iso3)
summary(m_horse)

# Test 2 - the SHARP test (needs a sector panel df_sec with cog_intensity_s in [0,1]):
#   dln(LP)_ist = c1*pm25_{t-1} + c2*(pm25_{t-1} x cog_intensity_s) + sector*country FE + year FE
#   PREDICT c2 < 0 (P2: pollution hits cognitively-intensive sectors harder). A pure income story
#   predicts c2 = 0. Sign and significance of c2 is what falsifies the cognitive mechanism.
# m_cog <- feols(dln_lp ~ pm25_l1 + pm25_l1:cog_intensity | sector_iso + year,
#                data = df_sec, cluster = ~sector_iso)
# summary(m_cog)         # c2<0 => cognitive signature; c2~0 => indistinguishable from development
#
# IDENTIFICATION CAVEATS to honor (stress-test F10/G1/G11):
#  - tau has Y in its denominator (G1): lag does not fully fix simultaneity; consider GMM/IV on
#    an exogenous emissions-technology shifter, or use ln(emissions_per_capita) net of ln(GDPpc).
#  - HALE (and inverse-PM2.5) are DOWNSTREAM of pollution (G11): putting H on the RHS partials out
#    part of the effect under study; report the anchor with and without lnH_l1.
#  - PM2.5 is an INVALID instrument for H (F10) if it also reaches TFP via the tau channel.
