#10. Qual é a arma mais comum entre todos os personagens?

import pandas as pd
import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')

precomenor = pd.read_sql("""
SELECT arma, COUNT(*) AS total
FROM (
    SELECT armaum AS arma FROM brawlhalla
    UNION ALL
    SELECT armadois AS arma FROM brawlhalla
)
GROUP BY arma
ORDER BY total DESC
LIMIT 1;
        
""", conn)

print(precomenor)