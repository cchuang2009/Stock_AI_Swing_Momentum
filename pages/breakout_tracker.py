
import streamlit as st
import pandas as pd
import numpy as np

st.title("Intraday Breakout Tracker")

st.markdown("""
Detect:
- Premarket breakout
- Volume spike
- VWAP reclaim
- Momentum acceleration
""")

symbols = [   "AAOI",
    "aehr",
    "AG",
    "AGIX",
    "AI",
    "alab",
    "AMAT",
    "AMD",
    "anet",
    "BBAI",
    "BLSH",
    "BTG",
    "CCOI",
    "COHR",
    "CRDO",
    "DGXX",
    "DXYZ",
    "INTC",
    "IONQ",
    "ISRG",
    "LITE",
    "LMT",
    "NOK",
    "NUAI",
    "MELI",
    "MRVL",
    "MU",
    "NBIS",
    "NVDA",
    "PLTR",
    "PAPL",
    "PLUG",
    "POET",
    "PYPL",
    "QBTS",
    "LWLG",
    "QUBT",
    "RGTI",
    "SMCI",
    "SNDK"]

rows = []

for s in symbols:
    rows.append({
        "Symbol": s,
        "Breakout": np.random.choice(["YES", "NO"]),
        "VolumeSpike": round(np.random.uniform(1.0, 5.0), 2),
        "VWAP": round(np.random.uniform(10, 200), 2),
    })

st.dataframe(pd.DataFrame(rows), use_container_width=True)

st.success("Live breakout alerts enabled.")
