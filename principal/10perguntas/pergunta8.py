#8. Quais personagens têm exatamente: força = 7 e defesa = 4?

import pandas as pd
import sqlite3

conn = sqlite3.connect('brawlhalla.db')

foredef = pd.read_sql("""
    SELECT * FROM brawlhalla
    WHERE forca = 7 AND defesa = 4
""", conn)

print(foredef)
