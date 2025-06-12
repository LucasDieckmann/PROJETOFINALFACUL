import pandas as pd
import json
from sqlalchemy import create_engine

def dfj(df):
    return df.to_json(orient='records', indent=4)

conn = create_engine('sqlite:///brawlhalla.db').connect()
df = pd.read_sql("SELECT * FROM brawlhalla", conn)
print(df)
