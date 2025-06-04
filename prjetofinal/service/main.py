import pandas as pd
from sqlalchemy import create_engine
import sqlite3
conn = sqlite3.connect('brawlhalla.db')

df = pd.read_sql("""
           SELECT * FROM brawlhalla       
                  """, conn)

print(df)


