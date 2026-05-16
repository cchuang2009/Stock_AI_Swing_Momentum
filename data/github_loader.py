import requests

DEFAULT_URL = "https://raw.githubusercontent.com/cchuang2009/Stock_AI_Swing_Momentum/main/tickers.txt"

def load_tickers_from_github(url):

    tickers = []

    try:

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            for line in response.text.splitlines():

                line = line.strip().upper()

                if line:
                    tickers.append(line)

    except Exception:
        pass

    return tickers
