import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')

df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
df_green.to_sql(name='green_taxi_data', con=engine, if_exists='replace', index=False)

print(f"Loaded {len(df_green)} rows into green_taxi_data")