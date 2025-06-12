import pandas as pd
import sqlite3

conn = sqlite3.connect('brawlhalla.db')

arma = pd.read_sql("""
    SELECT * FROM brawlhalla
    WHERE LOWER(armaum) = 'foice' OR LOWER(armadois) = 'foice'
""", conn)

print(arma)
