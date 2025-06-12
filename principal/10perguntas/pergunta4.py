# 4. Qual personagem tem a maior agilidade?
import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

agilidade = pd.read_sql("""
     SELECT * FROM brawlhalla
    ORDER BY agilidade DESC
    LIMIT 1
""", conn)

print(agilidade)