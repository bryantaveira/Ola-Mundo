#tela delogin dark com customtkinter
import tkinter
import customtkinter
from customtkinter import *

# cria um arquivo de texto
banco_de_dados = "dados.txt"

#função para cadastrar usuario
def email_ver(email):
    try:
        with open(banco_de_dados, "r") as arquivo:
            for linha in arquivo:
                usuario, senha = linha.strip().split(',')
                if usuario == email:
                    return True
    #tratamento de dados
    except FileNotFoundError:
        return False
    return False

#funçao que cadastra
def cad_email(email, senha):
    if email_ver(email):
        return False
    else:
        with open(banco_de_dados, 'a') as arquivo:
            arquivo.write(f'{email},{senha}\n')
        return True
    
def entrar(email, senha):
    try:
        with open(banco_de_dados, 'r') as arquivo:
            for linha in arquivo:
                usuario, senha_salva = linha.strip().split(",")
                if usuario == email and senha_salva == senha:
                    return True
    except FileNotFoundError:
        return False
    return False

def login():
    email = email_campo.get()
    senha = senha_campo.get()
    if email and senha:
        if entrar(email, senha):
            label_status.configure(text="Login bem-sucedido!", text_color="green")
        else:
            label_status.configure(text="e-mail ou senha incorretos.", text_color="red")
    else:
        label_status.configure(text="Preencha todos os campos.", text_color="red")

def cadastro():
    email = email_campo.get()
    senha = senha_campo.get()
    if email and senha:
        if cad_email(email, senha):
            label_status.configure(text="e-mail cadastrado com sucesso!", text_color='green')
        else:
            label_status.configure(text="e-mail' já registrado.", text_color="red")
    else:
        label_status.configure(text="Preencha todos os campos.", text_color="red")

#janela
janela = customtkinter.CTk()
janela.geometry('300x280')
janela.title('Login')

texto = CTkLabel(janela, text='Fazer login')
texto.pack(padx=0, pady=10)

#cria uma caixa para por e-mail
email_campo = CTkEntry(janela, placeholder_text='email')
email_campo.pack(padx=60, pady=10)

#cria uma caixa para senha
senha_campo = CTkEntry(janela, placeholder_text='senha',show="*")
senha_campo.pack(padx=10, pady=10)

#cria um botão e passa uma funçao para ele
botão = CTkButton(janela,text='Logar', command=login)
botão.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
botão.pack(padx=10, pady=10)
#cria um botçao para cadastrar
botão = CTkButton(janela,text='Cadastar', command=cadastro)
botão.pack(padx=10, pady=10)
botão.place(relx=0.5, rely=00.8, anchor=tkinter.CENTER)

label_status = CTkLabel(janela, text="")
label_status.pack(pady=10)
label_status.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# cria o loop da janela
janela.mainloop()

