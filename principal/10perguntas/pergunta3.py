# 3. Quais personagens têm defesa igual a 8?

import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

defesa = pd.read_sql("""
    SELECT * FROM brawlhalla
    WHERE defesa = 8
""", conn)

print(defesa)