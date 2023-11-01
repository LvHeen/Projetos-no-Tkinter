from tkinter import *
import tkinter as tk
import os
from time import strftime
 
root = tk.Tk()
root.title('Relógio')
root.geometry('400x200')
root.maxsize(400, 200)
root.minsize(400, 200)
root.config(background='#ffe5ec')

def get_nome():
    nome_usuario = os.getlogin()
    nome.config(text='Olá, ' + nome_usuario)
nome = Label(root, bg= '#ffe5ec', fg='#fb6f92', font=('Arial', 16)) #fonte não muda?
nome.pack()

def get_data():
    data_atual =strftime('%d %b %Y')
    data.config(text=data_atual)
data = Label(root, bg= '#ffe5ec', fg='#fb6f92', font=('Arial', 12)) #fonte não muda?
data.pack(pady=2)

def get_hora():
    hora_atual = strftime('%H:%M:%S')
    hora.config(text=hora_atual)
    hora.after(1000, get_hora)
hora = Label(root, bg= '#ffe5ec', fg='#fb6f92', font=('Arial', 65, 'bold')) 
hora.pack(pady=2)
tela = tk.Canvas(root, width=600, height=60, bg='#ffe5ec', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
 
get_nome()
get_data()
get_hora()

root.mainloop()
