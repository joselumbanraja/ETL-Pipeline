import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)

    # Ambil kolom yang penting saja
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]]

    # Rename biar clean
    df.columns = [
        "coin_id",
        "symbol",
        "name",
        "price",
        "market_cap",
        "volume"
    ]

    # Handle missing value
    df = df.dropna()

    return df