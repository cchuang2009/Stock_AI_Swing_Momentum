
import streamlit as st
import pandas as pd

st.title("Custom Watchlist Tracker")

default_watchlist = [
       "AAOI",
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
    "SNDK"
]

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
