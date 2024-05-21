import PySimpleGUI as sg
import mysql.connector

sg.theme('reddit')

layout = [
     [sg.Text("E-mail"), sg.Input(key="email")],
     [sg.Text("Senha"), sg.Input(key="senha", password_char="*")],
     [sg.Button('Salvar')]
]

janela = sg.Window("Project", layout=layout)

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

cursor.execute('INSERT INTO emails (email) VALUES (%s)', (email, ))
cursor.execute('INSERT INTO senhas (senha) VALUES (%s)', (senha, ))

conexao.commit()

cursor.close()
