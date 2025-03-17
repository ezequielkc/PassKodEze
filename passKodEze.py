import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  # Biblioteca para copiar senha para a área de transferência

# Função para gerar senha
def gerar_senha():
    try:
        # Obtém o tamanho da senha digitado pelo usuário
        tamanho = int(entry_tamanho.get())
        prefixo = entry_prefixo.get()  # Obtém o prefixo digitado pelo usuário

        # Validação: A senha precisa ter pelo menos 4 caracteres
        if tamanho < 4:
            messagebox.showerror("Erro", "Escolha um tamanho maior ou igual a 4.")
            return

        # Constrói a lista de caracteres possíveis para a senha
        caracteres = ""
        if var_maiusculas.get():
            caracteres += string.ascii_uppercase  # Letras maiúsculas (A-Z)
        if var_minusculas.get():
            caracteres += string.ascii_lowercase  # Letras minúsculas (a-z)
        if var_numeros.get():
            caracteres += string.digits  # Números (0-9)
        if var_especiais.get():
            caracteres += string.punctuation  # Caracteres especiais (!@#$%)

        # Se nenhum tipo de caractere foi selecionado, exibe erro
        if not caracteres:
            messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere.")
            return

        # Gera a senha aleatória
        senha = "".join(random.choice(caracteres) for _ in range(tamanho))

        # Exibe a senha gerada no campo de entrada com o prefixo
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, prefixo + senha)
    
    except ValueError:
        # Se o usuário digitar um valor inválido no tamanho, exibe erro
        messagebox.showerror("Erro", "Digite um número válido para o tamanho.")

# Função para copiar a senha gerada para a área de transferência
def copiar_senha():
    senha = entry_senha.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Copiado!", "Senha copiada para a área de transferência.")

# Criando a interface gráfica
root = tk.Tk()
root.title("PassKodEze - Gerador de Senhas")  # Título da janela
root.geometry("450x400")  # Define o tamanho da janela
root.configure(bg="#34495E")  # Define a cor de fundo

# Estilos globais para os widgets (rótulos, botões, etc.)
label_style = {"bg": "#34495E", "fg": "white", "font": ("Arial", 12)}
button_style = {"font": ("Arial", 12, "bold"), "width": 20}

# Título no topo da janela
tk.Label(root, text="Gerador de Senhas", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white", pady=10).pack(fill="both")

# Campo para definir o prefixo da senha
frame_prefixo = tk.Frame(root, bg="#34495E")
frame_prefixo.pack(pady=5)
tk.Label(frame_prefixo, text="Prefixo da senha:", **label_style).pack(side="left")
entry_prefixo = tk.Entry(frame_prefixo, font=("Arial", 12), width=10)
entry_prefixo.pack(side="left", padx=5)

# Campo para definir o tamanho da senha
frame_tamanho = tk.Frame(root, bg="#34495E")
frame_tamanho.pack(pady=5)
tk.Label(frame_tamanho, text="Tamanho da senha:", **label_style).pack(side="left")
entry_tamanho = tk.Entry(frame_tamanho, font=("Arial", 12), width=5)
entry_tamanho.pack(side="left", padx=5)

# Frame para os checkboxes das opções de caracteres
frame_opcoes = tk.Frame(root, bg="#34495E")
frame_opcoes.pack(pady=5)

var_maiusculas = tk.BooleanVar()
var_minusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_especiais = tk.BooleanVar()

# Criando as caixas de seleção (Checkbuttons)
tk.Checkbutton(frame_opcoes, text="Letras Maiúsculas", variable=var_maiusculas, onvalue=True, offvalue=False, selectcolor="#34495E", **label_style).grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_opcoes, text="Letras Minúsculas", variable=var_minusculas, onvalue=True, offvalue=False, selectcolor="#34495E", **label_style).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_opcoes, text="Números", variable=var_numeros, onvalue=True, offvalue=False, selectcolor="#34495E", **label_style).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_opcoes, text="Caracteres Especiais", variable=var_especiais, onvalue=True, offvalue=False, selectcolor="#34495E", **label_style).grid(row=3, column=0, sticky="w", padx=10)

# Campo de exibição da senha gerada
entry_senha = tk.Entry(root, font=("Arial", 14), width=30, justify="center", bd=2, relief="sunken")
entry_senha.pack(pady=10)

# Botão para gerar senha
btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha, bg="#1ABC9C", fg="white", **button_style)
btn_gerar.pack(pady=5)

# Botão para copiar senha
btn_copiar = tk.Button(root, text="Copiar Senha", command=copiar_senha, bg="#E74C3C", fg="white", **button_style)
btn_copiar.pack(pady=5)

# Executando o loop da interface gráfica
root.mainloop()
