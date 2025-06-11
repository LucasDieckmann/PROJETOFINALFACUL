import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import sqlite3
import os

# Caminho das imagens
caminho_imagens = r"C:\Users\BONIX\Desktop\projetofinal\prjetofinal\imagens"

# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')
conteudo_tabela = pd.read_sql("SELECT * FROM brawlhalla", conn)

# Função de pesquisa
def pesquisar(event=None):
    pesquisa = entrada_pesquisa.get().lower()
    lista_tabelas.delete(0, tk.END)
    for _, row in conteudo_tabela.iterrows():
        linha = f"{row['id']: <5} {row['personagens']: <20} {row['preco']: <10} {row['forca']: <5} {row['defesa']: <5} {row['destreza']: <5} {row['agilidade']: <5} {row['armaum']: <15} {row['armadois']: <15}"
        if pesquisa in linha.lower():
            lista_tabelas.insert(tk.END, linha)

# Mostrar imagem com base no nome digitado
def mostrar_imagem():
    nome_personagem = entrada_pesquisa.get().lower().strip()
    nome_arquivo = f"{nome_personagem}.png"
    caminho_completo = os.path.join(caminho_imagens, nome_arquivo)

    if os.path.exists(caminho_completo):
        imagem = Image.open(caminho_completo)
        imagem = imagem.resize((320, 180))  # Redimensionar para caber
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem.configure(image=imagem_tk, text='')
        label_imagem.image = imagem_tk
    else:
        label_imagem.configure(text="Imagem não encontrada", image='', fg='red')

# Criar janela principal
pagina = tk.Tk()
pagina.title("Brawlhalla Personagens")
pagina.geometry('900x700')
pagina.configure(bg='#1a1a2e')

# Título
label = tk.Label(pagina, text="Banco Brawlhalla", font=('Helvetica', 14, 'bold'), fg='#00aaff', bg='#1a1a2e')
label.pack(pady=10)

# Entrada de pesquisa
entrada_pesquisa = tk.Entry(pagina, font=('Helvetica', 12), bg='#0f3460', fg='white', insertbackground='white', relief=tk.FLAT)
entrada_pesquisa.pack(pady=10)
entrada_pesquisa.bind("<KeyRelease>", pesquisar)

# Lista com os dados
lista_tabelas = tk.Listbox(pagina, width=110, height=10, font=('Courier', 10), bg='#16213e', fg='white', selectbackground='#00aaff', relief=tk.FLAT)
lista_tabelas.pack(pady=10)

# Botão para mostrar imagem
botao_imagem = tk.Button(pagina, text="Mostrar Imagem", command=mostrar_imagem, bg='#00aaff', fg='white', font=('Helvetica', 10, 'bold'))
botao_imagem.pack(pady=5)

# Área da imagem
label_imagem = tk.Label(pagina, bg='#1a1a2e')
label_imagem.pack(pady=10)

# Preencher lista
for _, row in conteudo_tabela.iterrows():
    lista_tabelas.insert(tk.END, f"{row['id']: <5} {row['personagens']: <20} {row['preco']: <10} {row['forca']: <5} {row['defesa']: <5} {row['destreza']: <5} {row['agilidade']: <5} {row['armaum']: <15} {row['armadois']: <15}")

pagina.mainloop()
