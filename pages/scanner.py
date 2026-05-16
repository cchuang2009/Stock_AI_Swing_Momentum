
import streamlit as st
from core.scoring import calculate_score
from data.market_data import get_market_data
from data.github_loader import load_tickers_from_github

DEFAULT_URL = "https://raw.githubusercontent.com/cchuang2009/Stock_AI_Swing_Momentum/main/tickers.txt"

st.title("Nasdaq AI Scanner")

default_watchlist = load_tickers_from_github(DEFAULT_URL)

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
