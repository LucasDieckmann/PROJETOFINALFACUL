# 1. Qual personagem tem o maior custo (preço)?
import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

df_max_preco = pd.read_sql("""
    SELECT * FROM brawlhalla
    ORDER BY preco DESC
    LIMIT 1
""", conn)

print(df_max_preco)