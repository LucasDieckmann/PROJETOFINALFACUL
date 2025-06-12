# 2. Qual personagem tem a maior força?
import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

forca = pd.read_sql("""
    SELECT * FROM brawlhalla
    ORDER BY forca DESC
    LIMIT 1
""", conn)

print(forca)