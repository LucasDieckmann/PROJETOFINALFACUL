import pandas as pd
import json
from sqlalchemy import create_engine

def dfj(df):
    return df.to_json(orient='records', indent=4)

def tj(perso, conexao):
    query = f"SELECT * FROM {perso}"
    df = pd.read_sql(query, conexao)
    return dfj(df)

# Exemplo de uso
conn = create_engine('sqlite:///brawlhalla.db').connect()
json_data = tj('brawlhalla', conn)
print(json_data)
