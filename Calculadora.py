from tkinter import *
from tkinter import ttk

cor1 = '#A0C4FF' #azul
cor2 = '#FFC6FF'#rosa
cor3 = '#FFADAD' #vermelho
cor4 = '#FFD6A5' #laranja
cor5 = '#FDFFB6' #amarelo

num1 = ''
num2 = ''
divisao = FALSE
multiplicacao = FALSE
subtracao = FALSE
adicao = FALSE
potenciacao = FALSE


'''CORPO DA CALCULADORA'''
root = Tk()
root.title('Calculadora')
root.geometry('238x320')
root.minsize(238, 320)
root.maxsize(238, 320)
root.config(background=cor1)
corpo = Frame(root, width=220, heigh=360, background=cor1)
corpo.grid(row=1, column=0, columnspan=4, sticky=N + W + S + E, padx=13, pady=8)


'''CONFIGURAÇÕES DA TELA'''
tela = Entry(root, width=16, borderwidth=2, bg=cor2, font=('Sans-serif', 18), justify=RIGHT)
tela.grid(row=0, column=0, columnspan=3, sticky=N + W + S + E, padx=13, pady=9)


'''FUNÇÕES'''
def b_divisao():
    global num1
    global divisao
    divisao = TRUE
    num1 = tela.get()
    tela.delete(0, END)
def b_mult():
    global num1
    global multiplicacao
    multiplicacao = TRUE
    num1 = tela.get()
    tela.delete(0, END)
def b_sub():
    global num1
    global subtracao
    subtracao = TRUE
    num1 = tela.get()
    tela.delete(0, END)
def b_adic():
    global num1
    global adicao
    adicao = TRUE
    num1 = tela.get()
    tela.delete(0, END)
def b_pot():
    global num1
    global potenciacao
    potenciacao = TRUE
    num1 = tela.get()
    tela.delete(0, END)

def b_click(num):
    tela.insert(END, num)
    
def b_apagar():
    input_len = len(tela.get())
    tela.delete(input_len - 1)
def b_clean():
    tela.delete(0, END)
def b_igual():
    global divisao
    global multiplicacao
    global subtracao
    global adicao
    global potenciacao
    num2 = tela.get()
    tela.delete(0, END)
    #Calculando
    if divisao == TRUE:
        tela.insert(0, float(num1) / float(num2))
        divisao = FALSE
    if multiplicacao == TRUE:
        tela.insert(0, float(num1) * float(num2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        tela.insert(0, float(num1) - float(num2))
        subtracao = FALSE
    if adicao == TRUE:
        tela.insert(0, float(num1) + float(num2))
        adicao = FALSE
    if potenciacao == TRUE:
        tela.insert(0, float(num1) ** float(num2))
        potenciacao = FALSE


'''BOTÕES'''
apagar = Button(corpo, text='<--', width=13, height=2, bg=cor3, fg='black', command=b_apagar)
apagar.place(x=0, y=0)
b_clean = Button(corpo, text='C', width=5, height=2, bg=cor3, fg='black', command=b_clean)
b_clean.place(x=111, y=0)
divisao = Button(corpo, text='/', width=5, height=2, bg=cor4, fg='black', command=b_divisao)
divisao.place(x=166, y=0)

b_7 = Button(corpo, text='7', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(7))
b_7.place(x=0, y=50)
b_8 = Button(corpo, text='8', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(8))
b_8.place(x=55, y=50)
b_9 = Button(corpo, text='9', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(9))
b_9.place(x=111, y=50)
mult = Button(corpo, text='*', width=5, height=2, bg=cor4, fg='black', command=b_mult)
mult.place(x=166, y=50)

b_4 = Button(corpo, text='4', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(4))
b_4.place(x=0, y=100)
b_5 = Button(corpo, text='5', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(5))
b_5.place(x=55, y=100)
b_6 = Button(corpo, text='6', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(6))
b_6.place(x=111, y=100)
sub = Button(corpo, text='-', width=5, height=2, bg=cor4, fg='black', command=b_sub)
sub.place(x=166, y=100)

b_1 = Button(corpo, text='1', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(1))
b_1.place(x=0, y=150)
b_2 = Button(corpo, text='2', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(2))
b_2.place(x=55, y=150)
b_3 = Button(corpo, text='3', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(3))
b_3.place(x=111, y=150)
adic = Button(corpo, text='+', width=5, height=2, bg=cor4, fg='black', command=b_adic)
adic.place(x=166, y=150)


pot = Button(corpo, text='^', width=5, height=2, bg=cor4, fg='black', command=b_pot)
pot.place(x=0, y=200)
b_0 = Button(corpo, text='0', width=5, height=2, bg=cor5, fg='black', command=lambda:b_click(0))
b_0.place(x=55, y=200)
igual = Button(corpo, text='=', width=13, height=2, bg=cor4, fg='black', command=b_igual)
igual.place(x=111, y=200)


root.mainloop()
