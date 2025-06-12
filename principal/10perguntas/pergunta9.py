#9. Quantos personagens custam menos que 3000?
import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

precomenor = pd.read_sql("""
     SELECT * FROM brawlhalla
        WHERE preco < 3000
""", conn)

print(precomenor)