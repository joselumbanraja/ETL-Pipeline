import requests

def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data")