import PySimpleGUI as sg
from random import choice
import string

sg.theme("DarkBlue4")

layout = [ [sg.Button("Gerar senha")]]

janela = sg.Window("Gerador de senhas", layout)

while True:
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Gerar senha":
        tamanho_senha = 8
        
        caracteres_senha = string.ascii_letters + string.digits + string.punctuation
        
        senha_gerada = ""
        
        for i in range(tamanho_senha):
            senha_gerada += choice(caracteres_senha)
            
        sg.popup("Senha Gerada", f"A senha gerada é: {senha_gerada}")
janela.close()