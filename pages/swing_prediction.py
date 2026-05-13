
import streamlit as st
import pandas as pd
import numpy as np

st.title("Swing Prediction Engine")

candidates = [
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
