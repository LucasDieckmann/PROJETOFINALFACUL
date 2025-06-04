#quero q faça alguma funções uma que retorne todo dataframe em 1 json
#outra que ordene os herois por ordem escolhida
#força  / vida / valor
#crescente e decrescente
#tudo no pandas
import pandas as pd
import json
from sqlalchemy import create_engine

def dfj(df):
    return df.to_json(orient='records', indent=4)

# Exemplo de uso
conn = create_engine('sqlite:///brawlhalla.db').connect()
df = pd.read_sql("SELECT * FROM brawlhalla", conn)
json_data = dfj(df)
print(json_data)
