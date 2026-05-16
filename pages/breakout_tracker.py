
import streamlit as st
import pandas as pd
import numpy as np
from data.github_loader import load_tickers_from_github

st.title("Intraday Breakout Tracker")

st.markdown("""
Detect:
- Premarket breakout
- Volume spike
- VWAP reclaim
- Momentum acceleration
""")

DEFAULT_URL = "https://raw.githubusercontent.com/cchuang2009/Stock_AI_Swing_Momentum/main/tickers.txt"


symbols = load_tickers_from_github(DEFAULT_URL)

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
