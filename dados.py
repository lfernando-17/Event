from tkinter import *
from tkinter.ttk import *
import time
from contrato import Contrato
from database import savePalestra

class Palestra(object):
    def __init__(self , nome , title , hora , data , content, responsavel , resp_email) :
        self.nome= nome
        self.title = title
        self.hora = hora
        self.data = data
        self.content = content
        self.responsavel = responsavel
        self.resp_email = resp_email

def Dados(palestrante):
    j = Tk()
    j.title('Dados da Palestra')
    j.geometry('500x600')
    j.resizable(0,0)
    texto=Label(j,text=(f'Bem Vindo {palestrante.nome}'),font=('bold',20))
    texto.pack(pady=30)
    texto=Label(j,text='Preencha o formulário para receber o contrato',font=('bold',10))
    texto.place(x=110,y=70)
    texto = Label(j,text='Escolha o Evento',font=('bold',13))
    texto.place(x=80,y=130)
    eventos = ['Encontro Sustentável' , 'Semana de Tecnologia' , 'Semana da Arte' , 'Semana da Engenharia']
    nome1 = Combobox(j,values=eventos)
    nome1.place(x=220,y=135)

    texto = Label(j,text='Nome da Palestra',font=('bold',13))
    texto.place(x=80,y=180)
    title = Entry(j)
    title.place(x=230,y=180)

    texto = Label(j,text='Hora (Inicio-Fim)',font=('bold',13))
    texto.place(x=100,y=230)
    hora = Entry(j)
    hora.place(x=250,y=230)

    texto = Label(j,text='Data da Palestra',font=('bold',13))
    texto.place(x=100,y=280)
    data = Entry(j)
    data.place(x=250,y=280)

    texto = Label(j,text='Conteudo a ser Abordado',font=('bold',13))
    texto.place(x=140,y=330)
    content = Text(j,width=30,height=8)
    content.place(x=130,y=360)
    def salvar():
        palestra = Palestra(nome1.get(),title.get(),hora.get(),data.get(),content.get('1.0','end-1c'),palestrante.nome,palestrante.email)
        savePalestra(palestra)
        time.sleep(5)
        j.destroy()
        Contrato(palestra)

 
    resp = Button(j,text='Enviar',width=10,command=salvar)
    resp.place(x=200,y=530)
    j.mainloop()



    
