from tkinter import *
from tkinter import ttk

cor1 = '#A0C4FF' #azul
cor2 = '#FFC6FF'#rosa
cor3 = '#FFADAD' #vermelho
cor4 = '#FFD6A5' #laranja
cor5 = '#FDFFB6' #amarelo


'''CORPO DA CALCULADORA'''
root = Tk()
root.title('Calculadora')
root.geometry('238x380')
root.minsize(238, 380)
root.maxsize(238, 380)
root.config(background=cor1)
corpo = Frame(root, width=220, heigh=380, background=cor1)
corpo.grid(row=1, column=0, columnspan=4, sticky=N + W + S + E, padx=13, pady=8)


'''VISOR'''
tela = Frame(root, width=211, height=55, bg=cor2)
tela.grid(row=0, column=0, columnspan=3, sticky=N + W + S + E, padx=13, pady=8)


#Colocando valores no visor
valor_texto= StringVar()
visor_tela = Label(tela, width=14, height=2, textvariable=valor_texto, bg=cor2, anchor='e', fg='#242323', font=('Sans-serif', 18), justify=RIGHT)
visor_tela.place(x=5, y=0)


'''DEFININDO FUNÇÕES'''
def entrada_valores(evento):
    resultado = eval('10 + 1')

    #Printando os valores digitados
    valor_texto.set(todos_valores)


'''BOTÕES'''
b_apagar = Button(corpo, text='<--', width=13, height=2, bg=cor3, fg='black')
b_apagar.place(x=0, y=0)
b_clean = Button(corpo, text='C', width=5, height=2, bg=cor3, fg='black')
b_clean.place(x=111, y=0)
b_divisao = Button(corpo, text='/', width=5, height=2, bg=cor4, fg='black')
b_divisao.place(x=166, y=0)

b_7 = Button(corpo, text='7', width=5, height=2, bg=cor5, fg='black')
b_7.place(x=0, y=50)
b_8 = Button(corpo, text='8', width=5, height=2, bg=cor5, fg='black')
b_8.place(x=55, y=50)
b_9 = Button(corpo, text='9', width=5, height=2, bg=cor5, fg='black')
b_9.place(x=111, y=50)
b_mult = Button(corpo, text='*', width=5, height=2, bg=cor4, fg='black')
b_mult.place(x=166, y=50)

b_4 = Button(corpo, text='4', width=5, height=2, bg=cor5, fg='black')
b_4.place(x=0, y=100)
b_5 = Button(corpo, text='5', width=5, height=2, bg=cor5, fg='black')
b_5.place(x=55, y=100)
b_6 = Button(corpo, text='6', width=5, height=2, bg=cor5, fg='black')
b_6.place(x=111, y=100)
b_sub = Button(corpo, text='-', width=5, height=2, bg=cor4, fg='black')
b_sub.place(x=166, y=100)

b_1 = Button(corpo, text='1', width=5, height=2, bg=cor5, fg='black')
b_1.place(x=0, y=150)
b_2 = Button(corpo, text='2', width=5, height=2, bg=cor5, fg='black')
b_2.place(x=55, y=150)
b_3 = Button(corpo, text='3', width=5, height=2, bg=cor5, fg='black')
b_3.place(x=111, y=150)
b_adic = Button(corpo, text='+', width=5, height=2, bg=cor4, fg='black')
b_adic.place(x=166, y=150)

b_ponto = Button(corpo, text='.', width=5, height=2, bg=cor4, fg='black')
b_ponto.place(x=0, y=200)
b_0 = Button(corpo, text='0', width=5, height=2, bg=cor5, fg='black')
b_0.place(x=55, y=200)
b_pot = Button(corpo, text='^', width=5, height=2, bg=cor4, fg='black')
b_pot.place(x=111, y=200)
b_result = Button(corpo, text='=', width=5, height=2, bg=cor4, fg='black')
b_result.place(x=166, y=200)

b_sair = Button(corpo, text='SAIR', width=13, height=2, bg=cor2, fg='black')
b_sair.place(x=55, y=250)


'''CHAMAR FUNÇÕES'''
entrada_valores()


root.mainloop()
