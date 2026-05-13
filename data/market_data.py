
import pandas as pd
import yfinance as yf

def get_market_data(tickers):

    rows = []

    for ticker in tickers:

        try:
            stock = yf.Ticker(ticker)

            hist = stock.history(period="1mo")

            if len(hist) < 5:
                continue

            close = hist["Close"].iloc[-1]

            avg_volume = hist["Volume"].tail(20).mean()

            today_volume = hist["Volume"].iloc[-1]

            rvol = round(today_volume / avg_volume, 2) if avg_volume else 0

            ma20 = hist["Close"].tail(20).mean()

            momentum = round(((close - ma20) / ma20) * 100, 2)

            rows.append({
                "Symbol": ticker,
                "Price": round(close, 2),
                "RVOL": rvol,
                "Momentum": momentum,
                "NewsScore": 5,
                "ShortInterest": 5,
                "OptionsFlow": 5,
            })

        except Exception:
            continue

    return pd.DataFrame(rows)
