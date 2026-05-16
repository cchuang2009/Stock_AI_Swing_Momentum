
import streamlit as st
import pandas as pd
from data.github_loader import load_tickers_from_github


st.title("Custom Watchlist Tracker")
DEFAULT_URL = "https://raw.githubusercontent.com/cchuang2009/Stock_AI_Swing_Momentum/main/tickers.txt"

default_watchlist = load_tickers_from_github(DEFAULT_URL)

watch_input = st.text_input(
    "Watchlist",
    value=",".join(default_watchlist)
)

watchlist = [x.strip().upper() for x in watch_input.split(",")]

rows = []

for s in watchlist:
    rows.append({
        "Symbol": s,
        "Status": "Monitoring",
        "Alert": "Breakout Watch",
    })

st.dataframe(pd.DataFrame(rows), use_container_width=True)

st.markdown("""
### Real-Time Monitoring
- Relative volume
- Breakout alerts
- Momentum reversal
- VWAP reclaim
- Premarket strength
""")
