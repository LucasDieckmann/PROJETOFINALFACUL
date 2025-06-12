# 7. Qual é a média de força dos personagens com preço 5400?
import pandas as pd
import sqlite3

conn = sqlite3.connect('brawlhalla.db')

# Filtrar os personagens com preço 5400
inicio = pd.read_sql("""
    SELECT * FROM brawlhalla
    WHERE preco = 5400 
""", conn)

media_forca = inicio['forca'].mean()
print(media_forca)
