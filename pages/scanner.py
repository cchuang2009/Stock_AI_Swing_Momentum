
import streamlit as st
from core.scoring import calculate_score
from data.market_data import get_market_data

st.title("Nasdaq AI Scanner")

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
    "EUV",
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

user_input = st.text_input(
    "Add custom tickers (comma separated)",
    value=",".join(default_watchlist)
)

tickers = [x.strip().upper() for x in user_input.split(",")]

if st.button("Run Scanner"):

    with st.spinner("Scanning market..."):

        df = get_market_data(tickers)

        if len(df) > 0:

            df["MomentumScore"] = df.apply(calculate_score, axis=1)

            df = df.sort_values(
                by="MomentumScore",
                ascending=False
            )

            st.dataframe(df, use_container_width=True)

        else:
            st.warning("No market data found.")

st.subheader("Scanner Logic")

st.markdown("""
### Conditions
- Relative Volume > 2
- Price > MA20
- Momentum acceleration
- AI narrative strength
- Volume expansion
""")
