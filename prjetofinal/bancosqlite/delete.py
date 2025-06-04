import os

db_path = "braw.db"

# Fecha conexões pendentes antes de remover
try:
    import sqlite3
    conn = sqlite3.connect(db_path)
    conn.close()
except Exception as e:
    print(f"Erro ao fechar conexão: {e}")

# Agora tenta remover o arquivo
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print("Banco de dados apagado com sucesso!")
    except PermissionError:
        print("Erro: O arquivo está em uso por outro processo.")
else:
    print("O banco de dados não existe.")
