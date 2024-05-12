import PySimpleGUI as sg
import mysql.connector

sg.theme('reddit')

layout = [
     [sg.Text("E-mail"), sg.Input(key="email")],
     [sg.Text("Senha"), sg.Input(key="senha", password_char="*")],
     [sg.Button('Salvar')]
]

janela = sg.Window("Principal", layout=layout)

while True:
     event, values = janela.read()
     if event == sg.WIN_CLOSED:
          break
     elif event == 'Salvar':
          email = values['email']
          senha = values['senha']
          break


conexao = mysql.connector.connect(

     host='localhost',
     user='root',
     password='password',
     database='db_database'
)

cursor = conexao.cursor()

comando = f'INSERT INTO emails (email) VALUES ("%S"); INSERT INTO senhas (senha) VALUES ("%S")'

cursor.execute(comando(email, senha))

conexao.commit()

cursor.close()
