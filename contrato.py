from tkinter import *
from tkinter.ttk import *
import smtplib
import time
from database import AceitarContrato


def Contrato(palestra):
    i=Tk()
    i.title('Contrato')
    i.resizable(0,0)
    i.geometry('600x500')
    texto1=Label(i,text='Contrato',font=('bold',20))
    texto1.pack(pady=30)
    texto = Label(i,text='Nome do Palestrante :',font=('bold',14))
    texto.place(x=100,y=150)
    texto = Label(i,text=(palestra.responsavel),font=('bold',14))
    texto.place(x=300,y=150)
    #Buscar no banco de dados

    texto = Label(i,text='Nome do Evento : ',font=('bold',14))
    texto.place(x=100,y=170)
    texto = Label(i,text=(palestra.nome),font=('bold',14))
    texto.place(x=260,y=170)

    texto = Label(i,text='Título da Palestra :',font=('bold',14))
    texto.place(x=100,y=190)
    texto = Label(i,text=(palestra.title),font=('bold',14))
    texto.place(x=260,y=190)

    texto = Label(i,text='Hora da Palestra :',font=('bold',14))
    texto.place(x=100,y=230)
    texto = Label(i,text=(palestra.hora),font=('bold',14))
    texto.place(x=260,y=230)
    

    texto = Label(i,text='Data da palestra :',font=('bold',14))
    texto.place(x=100,y=250)
    texto = Label(i,text=(palestra.data),font=('bold',14))
    texto.place(x=260,y=250)
    def envio():
        time.sleep(5)
        texto1.config(text='EMAIL DE CONFIRMAÇÃO ENVIADO !')

    resp = Button(i,text='Confirmar',width=10,command=envio)
    resp.place(x=200,y=330)
    def die():
        i.destroy()
    resp1 = Button(i,text='Cancelar',width=10,command=die)
    resp1.place(x=300,y=330)

    i.mainloop()

