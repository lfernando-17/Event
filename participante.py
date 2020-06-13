from tkinter import *
from tkinter.ttk import *
import time
from dados import  Dados
from database import savePalest
class Palestrante(object):
    def __init__(self , nome , email ,telefone ,cpf , data,matricula):
        self.nome = nome
        self.email = email
        self.telefone=telefone
        self.cpf = cpf
        self.data = data
        self.matricula = matricula
i = Tk()
i.title('Organizador de Eventos')
i.resizable(0,0)
i.geometry('500x600')
texto=Label(i,text='Bem Vindo Palestrante',font=('bold',20))
texto.pack(pady=30)
texto=Label(i,text='Preencha o formulário para receber o contrato',font=('bold',10))
texto.place(x=110,y=70)
texto = Label(i,text='Nome',font=('bold',13))
texto.place(x=150,y=130)
nome1 = Entry(i)
nome1.place(x=220,y=135)

texto = Label(i,text='Email',font=('bold',13))
texto.place(x=150,y=180)
email1 = Entry(i)
email1.place(x=230,y=180)

texto = Label(i,text='Telefone',font=('bold',13))
texto.place(x=150,y=230)
telefone1 = Entry(i)
telefone1.place(x=230,y=230)

texto = Label(i,text='CPF',font=('bold',13))
texto.place(x=150,y=280)
cpf1 = Entry(i)
cpf1.place(x=210,y=280)

texto = Label(i,text='Data de Nascimento',font=('bold',13))
texto.place(x=90,y=330)
data1 = Entry(i)
data1.place(x=250,y=330)

texto = Label(i,text='É ex-aluno ?',font=('bold',13))
texto.place(x=130,y=370)
def novo():
    matricula1.delete(0,100)
    matricula1.configure(state='disabled')

def antigo():
    matricula1.configure(state='normal')
valor = IntVar()
ra1 = Radiobutton(i,text='Sim',variable=valor,value=1,command=antigo)
ra1.place(x=250,y=370)
ra2 = Radiobutton(i,text='Não',variable=valor,value=2,command=novo)
ra2.place(x=300,y=370)

texto = Label(i,text='Matricula',font=('bold',13))
texto.place(x=140,y=420)
matricula1 = Entry(i)
matricula1.place(x=230,y=420)

def Enviar():
    participante=Palestrante(nome1.get(),email1.get(),telefone1.get(),cpf1.get(),data1.get(),matricula1.get())
    savePalest(participante)
    time.sleep(5)
    i.destroy()
    Dados(participante)
    
resp = Button(i,text='Enviar',width=10,command=Enviar)
resp.place(x=200,y=470)


i.mainloop()