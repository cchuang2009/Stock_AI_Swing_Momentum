
import streamlit as st
import pandas as pd
import numpy as np
from data.github_loader import load_tickers_from_github

st.title("Swing Prediction Engine")

DEFAULT_URL = "https://raw.githubusercontent.com/cchuang2009/Stock_AI_Swing_Momentum/main/tickers.txt"

candidates = load_tickers_from_github(DEFAULT_URL)

rows = []

for s in candidates:
    rows.append({
        "Symbol": s,
        "BreakoutProbability": round(np.random.uniform(60, 95), 2),
        "Risk": np.random.choice(["High", "Medium"]),
        "SuggestedAction": np.random.choice([
            "Breakout Entry",
            "Pullback Buy",
            "Watch Only"
        ])
    })

df = pd.DataFrame(rows)

st.dataframe(df, use_container_width=True)

st.warning("High-beta AI momentum stocks are highly volatile.")
