#como criar interfaces graficas com Tkinter
import requests
from tkinter import *
from tkinter import ttk

#criar uma função mostar na janela

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotaçoes["text"] = texto



# cria uma janela e o titulo e o tamanho dela
janela = Tk()
janela.title('Cotação das moedas')
janela.geometry("210x200")


# cria uma caixa de texto e
# defini a posição do label de acordo com uma coluna e linha
labeltexto = Label(janela, text='aperte o botão para ver as cotações')
labeltexto.grid(column=0, row=0, padx=10, pady=10)

#cria um botão e passa um texto para ele e um comando
# apartir de um função e defini a posição dele
botão = Button(janela, text="atualizar", command=pegar_cotacoes)
botão.grid(column=0, row=2, padx=10, pady=40)

#cria uma caixa de texto vazia
texto_cotaçoes = Label(janela, text="")
texto_cotaçoes.grid(column=0, row=1, padx=10, pady=10)

# cria um loop para a janela
janela.mainloop()
