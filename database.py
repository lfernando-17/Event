import mysql.connector

conexao = mysql.connector.connect (
    host = 'localhost',
    user = 'root' ,
    password = '',
    database='org'
)

cursor = conexao.cursor()
def savePalest(info):
    cursor.execute("insert into Palestrante (nome , email , telefone , cpf , data , matricula ) values (%s,%s,%s,%s,%s,%s)",(info.nome , info.email , info.telefone , info.cpf ,info.data,info.matricula))
    conexao.commit()
def savePalestra(info) :
    cursor.execute("insert into Palestra(nome_Evento,titulo_Palestra,hora,data,conteudo) values (%s,%s,%s,%s,%s)",(info.nome,info.title,info.hora,info.data,info.content))
    conexao.commit()

#cursor.execute("create database org")
#cursor.execute("create table Palestrante(nome varchar(100) not null ,email varchar(100) not null , telefone int(9) not null , cpf int(12) primary key, data date not null , matricula int(15))")
#cursor.execute("create table Palestra(cod_Palestra int auto_increment primary key ,nome_Evento varchar(100) not null , titulo_Palestra varchar(100) not null , hora varchar(100) not null , data date not null ,conteudo varchar(500))")
