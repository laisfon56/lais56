import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Produto:
    def __init__(self, nome, tipo, preco):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def mostrar(self):
        return f"{self.nome} ({self.tipo}) - R${self.preco:.2f}"

class Celular(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, "Celular", preco)

class Tablet(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, "Tablet", preco)

class Mouse(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, "Mouse", preco)

class Periferico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, "Periférico", preco)

lista_produtos = []

def cadastraProduto():
    nome = entryNome.get()
    preco = entryPreco.get()
    tipo = varTipo.get()
    erro = 0

    if nome == "" or preco == "":
        messagebox.showinfo("Erro", "Nome e Preço devem ser preenchidos!")
        erro = 1

    if erro == 0:
        try:
            preco = float(preco)
        except ValueError:
            messagebox.showinfo("Erro", "Preço deve ser um número válido!")
            erro = 1

    if erro == 0:
        if tipo == "Celular":
            produto = Celular(nome, preco)
        elif tipo == "Tablet":
            produto = Tablet(nome, preco)
        elif tipo == "Mouse":
            produto = Mouse(nome, preco)
        else:
            produto = Periferico(nome, preco)
        
        lista_produtos.append(produto)
        messagebox.showinfo("Cadastro", f"Produto {nome} cadastrado com sucesso!")
        entryNome.delete(0, tk.END)
        entryPreco.delete(0, tk.END)
        atualizaListabox()

def atualizaListabox():
    listbox.delete(0, tk.END)
    for produto in lista_produtos:
        listbox.insert(tk.END, produto.mostrar())

janela = tk.Tk()
janela.title("Cadastro de Produtos de Computadores")
janela.geometry("600x400")
janela.config(bg="#f0f0f0")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
tab1.grid_rowconfigure(4, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista de Produtos")

label1 = tk.Label(tab1, text="Nome do Produto: ", font=("Helvetica", 14), bg="#f0f0f0")
label1.grid(row=0, column=0, sticky="w", padx=15, pady=10)

entryNome = tk.Entry(tab1, font=("Helvetica", 14), bd=2, relief="solid", width=30)
entryNome.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label2 = tk.Label(tab1, text="Preço: R$", font=("Helvetica", 14), bg="#f0f0f0")
label2.grid(row=1, column=0, sticky="w", padx=15, pady=10)

entryPreco = tk.Entry(tab1, font=("Helvetica", 14), bd=2, relief="solid", width=30)
entryPreco.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo de Produto: ", font=("Helvetica", 14), bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=15, pady=10)

varTipo = tk.StringVar(value="Celular")
tk.Radiobutton(tab1, text="Celular", font=("Helvetica", 14), variable=varTipo, value="celular", bg="#f0f0f0").grid(row=2, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Tablet", font=("Helvetica", 14), variable=varTipo, value="tablet", bg="#f0f0f0").grid(row=2, column=1, sticky="e", padx=10)
tk.Radiobutton(tab1, text="Mouse", font=("Helvetica", 14), variable=varTipo, value="Mouse", bg="#f0f0f0").grid(row=3, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Periférico", font=("Helvetica", 14), variable=varTipo, value="Periferico", bg="#f0f0f0").grid(row=3, column=1, sticky="e", padx=10)

tk.Button(tab1, text="Cadastrar Produto", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=cadastraProduto, relief="solid").grid(row=4, columnspan=2, pady=20)

listbox = tk.Listbox(tab2, font=("Helvetica", 12), width=45, height=10, bd=2, relief="solid")
listbox.grid(row=0, column=0, sticky="nsew", padx=15, pady=10)

tk.Button(tab2, text="Atualizar Lista", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=atualizaListabox, relief="solid").grid(row=1, column=0, pady=10)

janela.mainloop()