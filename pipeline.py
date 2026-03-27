from extract import fetch_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Extracting data...")
    raw_data = fetch_data()

    print("Transforming data...")
    clean_data = transform_data(raw_data)

    print("Loading data...")
    load_data(clean_data)

    print("ETL selesai!")

if __name__ == "__main__":
    run_pipeline()