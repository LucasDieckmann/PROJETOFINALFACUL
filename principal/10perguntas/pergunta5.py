# 5. Quais personagens possuem destreza igual ou maior que 7?

import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

destreza = pd.read_sql("""
    SELECT * FROM brawlhalla
    WHERE destreza >= 7
""", conn)

print(destreza)