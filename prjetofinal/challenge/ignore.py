import tkinter as tk
import pandas as pd
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')
conteudo_tabela = pd.read_sql("SELECT * FROM brawlhalla", conn)

# Função de pesquisa
def pesquisar(event):
    pesquisa = entrada_pesquisa.get().lower()
    lista_tabelas.delete(0, tk.END)
    for _, row in conteudo_tabela.iterrows():
        linha = f"{row['id']: <5} {row['personagens']: <20} {row['preco']: <10} {row['forca']: <5} {row['defesa']: <5} {row['destreza']: <5} {row['agilidade']: <5} {row['armaum']: <15} {row['armadois']: <15}"
        if pesquisa in linha.lower():
            lista_tabelas.insert(tk.END, linha)

# Criar janela principal
pagina = tk.Tk()
pagina.title("Tabelas do Banco de Dados")
pagina.geometry('800x400')
pagina.configure(bg='#1a1a2e')  # Fundo preto azulado

# Estilizando os widgets
label = tk.Label(pagina, text="Banco Brawlhalla", font=('Helvetica', 14, 'bold'), fg='#00aaff', bg='#1a1a2e')
label.pack(pady=10)

entrada_pesquisa = tk.Entry(pagina, font=('Helvetica', 12), bg='#0f3460', fg='white', insertbackground='white', relief=tk.FLAT)
entrada_pesquisa.pack(pady=10)
entrada_pesquisa.bind("<KeyRelease>", pesquisar)

lista_tabelas = tk.Listbox(pagina, width=110, height=15, font=('Courier', 10), bg='#16213e', fg='white', selectbackground='#00aaff', relief=tk.FLAT)
lista_tabelas.pack(pady=10)

# Preencher a lista com dados do banco de dados
for _, row in conteudo_tabela.iterrows():
    lista_tabelas.insert(tk.END, f"{row['id']: <5} {row['personagens']: <20} {row['preco']: <10} {row['forca']: <5} {row['defesa']: <5} {row['destreza']: <5} {row['agilidade']: <5} {row['armaum']: <15} {row['armadois']: <15}")

pagina.mainloop()
