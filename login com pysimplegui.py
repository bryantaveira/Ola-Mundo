from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('usuario'), sg.Input(key='usuario')],
    [sg.Text('senha'), sg.Input(key='senha', password_char='*') ],
    [sg.Checkbox('Salvar login')],
    [sg.Button('Entrar')]
] 
#janela
janela = sg.Window("tela de login", layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'bryan' and valores['senha'] == '123456':
            print('bem vindo')