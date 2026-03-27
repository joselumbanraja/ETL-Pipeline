from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine(
        'postgresql://postgres:1@localhost:5432/etl_db'
    )

    df.to_sql(
        name="crypto_markets",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data berhasil disimpan ke database!")