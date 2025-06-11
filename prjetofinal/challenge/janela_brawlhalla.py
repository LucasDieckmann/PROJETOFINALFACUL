import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import sqlite3
import os

# Caminho da pasta com as imagens
CAMINHO_IMAGENS = r"prjetofinal\imagens"

# Conectar ao banco de dados
conn = sqlite3.connect('brawlhalla.db')
conteudo_tabela = pd.read_sql("SELECT * FROM brawlhalla", conn)

# Função para exibir a imagem
def mostrar_imagem(nome_personagem):
    nome_arquivo = f"{nome_personagem}.png"
    caminho_completo = os.path.join(CAMINHO_IMAGENS, nome_arquivo)

    if os.path.exists(caminho_completo):
        imagem = Image.open(caminho_completo)
        imagem = imagem.resize((600, 300))  
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk  # Mantém referência para não apagar
    else:
        messagebox.showerror("Erro", f"Imagem '{nome_arquivo}' não encontrada!")

# Função chamada ao clicar no botão ou na lista
def exibir_imagem_selecionada():
    selecionado = lista_tabelas.curselection()
    if selecionado:
        linha = lista_tabelas.get(selecionado[0])
        nome_personagem = linha.split()[1]  # O nome está na segunda posição
        mostrar_imagem(nome_personagem)
    else:
        messagebox.showinfo("Aviso", "Selecione um personagem na lista.")

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
pagina.title("Brawlhalla - Visualizador de Personagens")
pagina.geometry('1000x600')
pagina.configure(bg='#1a1a2e')

# Título
label = tk.Label(pagina, text="Banco Brawlhalla", font=('Helvetica', 16, 'bold'), fg='#00aaff', bg='#1a1a2e')
label.pack(pady=10)

# Entrada de pesquisa
entrada_pesquisa = tk.Entry(pagina, font=('Helvetica', 12), bg='#0f3460', fg='white', insertbackground='white')
entrada_pesquisa.pack(pady=5)
entrada_pesquisa.bind("<KeyRelease>", pesquisar)

# Lista de personagens
lista_tabelas = tk.Listbox(pagina, width=110, height=15, font=('Courier', 10), bg='#16213e', fg='white', selectbackground='#00aaff')
lista_tabelas.pack(pady=10)
lista_tabelas.bind("<<ListboxSelect>>", lambda e: exibir_imagem_selecionada())


# Área da imagem
label_imagem = tk.Label(pagina, bg='#1a1a2e')
label_imagem.pack(pady=10)

# Preencher a lista inicialmente
for _, row in conteudo_tabela.iterrows():
    linha = f"{row['id']: <5} {row['personagens']: <20} {row['preco']: <10} {row['forca']: <5} {row['defesa']: <5} {row['destreza']: <5} {row['agilidade']: <5} {row['armaum']: <15} {row['armadois']: <15}"
    lista_tabelas.insert(tk.END, linha)

pagina.mainloop()
