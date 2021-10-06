from tkinter.constants import CENTER, LEFT, RIGHT, TOP, VERTICAL, Y
from typing import TextIO
from screeninfo import get_monitors
import tkinter as tk
import time
from tkinter import Scrollbar, ttk
from Usuarios2 import Usuarios
import tkinter.messagebox as tkMessageBox

def buscarUsuario():
	#busca no banco moradores e visitantes pelo cpf ou casa ou veiculo
	user = Usuarios()
	resposta = user.selectidic(tb_movimento=tb_movimento)

	tkMessageBox.showinfo('Resposta', message=resposta)
def novocadas():
    textcpf.delete(0,'end')
    textnome.delete(0,'end')
    textfone.delete(0,'end')
    textemail.delete(0,'end')
    Textid.delete(0,'end')
    textguiche.delete(0, 'end')
    textguiche.insert(0,0)
    textguiche.config(state='disabled')
    Textid.config(state='disabled')
    textcpf.focus()
    tkMessageBox.showinfo('Resposta', "Iniciando um novo cadastro")
    



def mostraSalientado(evento):
			
    cont = 0
    textcpf.delete(0,'end')
    textnome.delete(0,'end')
    textfone.delete(0,'end')
    textemail.delete(0,'end')
    textguiche.config(state='normal')
    Textid.config(state='normal')
    Textid.delete(0,'end')
    
    
    selecionado = tb_movimento.selection()[0]
    valor = tb_movimento.item(selecionado,"values")
    textcpf.insert(0,valor[1])
    textnome.insert(0,valor[2])
    textfone.insert(0,valor[3])
    textemail.insert(0,valor[4])
    Textid.insert(0,valor[0])
		

def reali_cadstro():
    user = Usuarios()
    cpf = textcpf.get()
    nome = textnome.get()
    fone = textfone.get()
    email = textemail.get()
    guiche = textguiche.get()
    textguiche.config(state='disabled')

    if cpf == "" or nome == "" or fone == "" or email == "":
        tkMessageBox.showinfo('Resposta', "Favor Preencher o campo histórico")
    else:
        user.cpf = cpf
        user.nome = nome
        user.fone = fone
        user.email = email
        user.guiche = guiche
        #user.id = '1'
        

        resposta = user.insertUser()

        tkMessageBox.showinfo('Resposta', message=user.id + resposta)
        buscarUsuario()
        #novocadas()


def cria_tela2():
    try:
        x=1
        #pega o valor digitado
        textonatela = 'Seja Bem Vindo'
        width = 0
        y=100
        #define monitores e onde será projetado
        #print(get_monitors()[0])
        for m in get_monitors():
            #print('monitores',str(m))
            width = m.x
            #print('Largura ',width)
        #cria tela para projetar
        global tela2
        tela2 = tk.Tk()

        tela2.geometry("800x500+0+100")
        tela2['bg'] = 'white'
        tela2.title("")
        pad=3
        tela2.geometry("{0}x{1}+".format(tela2.winfo_screenwidth()-pad, tela2.winfo_screenheight()-pad) + str(width) + "+0")

        label = tk.Label(tela2,text=textonatela,bg = "white", fg='black', font=('arial',60,'bold'))
        label.place(relx=0.2, rely = 0.2)

        frame2 = tk.Frame(tela2,bg='SkyBlue',bd=2,relief= "solid")
        frame2.place(relx=0.05, rely = 0.4)
        titu_dep2 = tk.Label(frame2,width=30,bd=4,bg='SkyBlue', height=2,text= 'Verifique sua senha',fg='black',font=('arial',20,'bold'))
        titu_dep2.pack(side=TOP)
        global tb_movimento2
        tb_movimento2 = ttk.Treeview(frame2, column=(1,3,6), show='headings', height=20)
        tb_movimento2.pack(side=LEFT)
        tb_movimento2.column(1, width=100, anchor="center")
        tb_movimento2.column(3, width=400, anchor="center")
        tb_movimento2.column(6, width=100, anchor="center")

        #cabeçalhos
        tb_movimento2.heading(1, text='Senha')
        tb_movimento2.heading(3, text='NOME')
        tb_movimento2.heading(6, text='GUICHE')
        

        sb2 = Scrollbar(frame2, orient=VERTICAL)
        sb2.pack(side=RIGHT, fill=Y)
        tb_movimento2.config(yscrollcommand=sb.set)
        sb2.config(command=tb_movimento2.yview)
        style2 = ttk.Style()
        style2.theme_use("clam")
        style2.map("Treeview")
        style2.configure(".", font=('Helvetica', 12), foreground="blue")

        user = Usuarios()
        resposta = user.selesenhas(tb_movimento2=tb_movimento2)
        #repete os textos
        '''info = tb_movimento2.get_children()
        valor = tb_movimento2.item(info[0],"values")
        print(valor)
        for i in info:
            info2 = tb_movimento2.set(i)
            print(i,":",info2[0])
            for a in info2:
                print(a,":",info2[a])'''
        while True:
            resposta = user.selesenhas(tb_movimento2=tb_movimento2)
            #textonatela = 'Senha: '+ user.id + ' - '+ user.nome + ' - Favor dirigir-se ao Guichê'+ user.guiche
            info = tb_movimento2.get_children()
            valor = tb_movimento2.item(info[0],"values")
            id = valor[0]
            nome = valor[1]
            guiche = valor[2]
            textonatela = 'Senha: {0} - {1} - Favor dirigir-se ao Guichê{2}'.format(id,nome,guiche)
            time.sleep(0.4)
            
            label.config(text=textonatela)
            label.place(relx=y/100, rely = 0.1)
            tela2.update()
            #x=x-1
            y=y-10
            if y/100 == 0:
                time.sleep(0.5)
            if y <= -100-len(textonatela)*3:
                y=110
        #tela2.update()
        
    except:
        pass

def sai_tela2():
    try:
        if tela2 is not None:
            tela2.destroy()
    
    except:
        tela.destroy()
   
def chamandoguiche(guiche):
    try:
        if tela2 is not None:
            textguiche.config(state='normal')
            textguiche.delete(0, 'end')
            textguiche.insert(0,guiche)
            user = Usuarios()
            user.cpf = textcpf.get()
            user.nome = textnome.get()
            user.fone = textfone.get()
            user.email = textemail.get()
            user.guiche = textguiche.get()
            user.id = Textid.get()
            altera = user.updateUser()
            iniciando = buscarUsuario()
            resposta = user.selesenhas(tb_movimento2=tb_movimento2)
    
    except:
        tkMessageBox.showinfo('Resposta', "Favor abrir o painel")
    

tela = tk.Tk()

tela.geometry("1440x900+0+0")
tela['bg'] = 'Green'
tela.title("Sistema de Senhas")


lblcpf = tk.Label(tela,bg = "white",bd=4,text=" CPF ", fg='Black', font=('arial',10,'bold'))
lblcpf.place(relx=0.05, rely=0.1)
textcpf = tk.Entry(tela,bg = "white",width=30, bd=4, fg='Black',justify='center', font=('arial',10,'bold'))
textcpf.place(relx=0.12, rely = 0.1)

lblnome = tk.Label(tela,bg = "white",bd=4,text=" Nome ", fg='Black', font=('arial',10,'bold'))
lblnome.place(relx=0.42, rely=0.1)
textnome = tk.Entry(tela,bg = "white",width=30, bd=4, fg='Black',justify='center', font=('arial',10,'bold'))
textnome.place(relx=0.49, rely = 0.1)

lblfone = tk.Label(tela,bg = "white",bd=4,text=" Fone ", fg='Black', font=('arial',10,'bold'))
lblfone.place(relx=0.05, rely=0.2)
textfone = tk.Entry(tela,bg = "white",width=30, bd=4, fg='Black',justify='center', font=('arial',10,'bold'))
textfone.place(relx=0.12, rely = 0.2)

lblemail = tk.Label(tela,bg = "white",bd=4,text=" Email ", fg='Black', font=('arial',10,'bold'))
lblemail.place(relx=0.42, rely=0.2)
textemail = tk.Entry(tela,bg = "white",width=30, bd=4, fg='Black',justify='center', font=('arial',10,'bold'))
textemail.place(relx=0.49, rely = 0.2)

lblguiche = tk.Label(tela,bg = "white",bd=4,text=" Guiche ", fg='Black', font=('arial',10,'bold'))
lblguiche.place(relx=0.05, rely=0.3)
textguiche = tk.Entry(tela,bg = "white",width=5, bd=4, fg='Black',justify='center', font=('arial',10,'bold'))
textguiche.place(relx=0.12, rely = 0.3)
textguiche.insert(0,0)
textguiche.config(state='disabled')

lblid = tk.Label(tela,bg = "white",bd=4,text=" Senha ", fg='Black', font=('arial',10,'bold'))
lblid.place(relx=0.42, rely=0.3)
Textid = tk.Entry(tela,bg = "white",width=5, bd=4, fg='Black',justify='center', font=('arial',10,'bold'))
Textid.place(relx=0.49, rely = 0.3)
Textid.insert(0,0)
Textid.config(state='disabled')


frame = tk.Frame(tela,bg='SkyBlue',bd=2,relief= "solid")
frame.place(relx=0.05, rely = 0.4)
titu_dep = tk.Label(frame,width=30,bd=4,bg='SkyBlue', height=2,text= 'Lista de Senhas',fg='black',font=('arial',14,'bold'))
titu_dep.pack(side=TOP)
global tb_movimento
tb_movimento = ttk.Treeview(frame, column=(1,2,3,4,5,6), show='headings', height=12)
tb_movimento.pack(side=LEFT)
tb_movimento.column(1, width=100, anchor="center")
tb_movimento.column(2, width=200, anchor="center")
tb_movimento.column(3, width=400, anchor="center")
tb_movimento.column(4, width=100, anchor="center")
tb_movimento.column(5, width=100, anchor="center")
tb_movimento.column(6, width=100, anchor="center")

#cabeçalhos
tb_movimento.heading(1, text='Senha')
tb_movimento.heading(2, text='CPF')
tb_movimento.heading(3, text='NOME')
tb_movimento.heading(4, text='FONE')
tb_movimento.heading(5, text='EMAIL')
tb_movimento.heading(6, text='GUICHE')
tb_movimento.bind('<<TreeviewSelect>>', mostraSalientado)

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
tb_movimento.config(yscrollcommand=sb.set)
sb.config(command=tb_movimento.yview)
style = ttk.Style()
style.theme_use("clam")
style.map("Treeview")
style.configure(".", font=('Helvetica', 12), foreground="blue")


botao = tk.Button(tela,text="    Painel   ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=cria_tela2)
botao.place(relx=0.05, rely = 0.9)

botao2 = tk.Button(tela,text="     Sair      ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=sai_tela2)
botao2.place(relx=0.20, rely = 0.9)

botao3 = tk.Button(tela,text=" Guichê 1 ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=lambda:chamandoguiche(1))
botao3.place(relx=0.35, rely = 0.9)

botao4 = tk.Button(tela,text=" Guichê 2 ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=lambda:chamandoguiche(2))
botao4.place(relx=0.5, rely = 0.9)

botao5 = tk.Button(tela,text=" Guichê 3 ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=lambda:chamandoguiche(3))
botao5.place(relx=0.65, rely = 0.9)

botao7 = tk.Button(tela,text="    Novo   ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=novocadas)
botao7.place(relx=0.05, rely = 0.8)

#botao8 = tk.Button(tela,text="    Chamar   ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=novocadas)
#botao8.place(relx=0.20, rely = 0.8)

botao6 = tk.Button(tela,text=" Cadastrar ",bg = "Black",bd=4, fg='white', font=('arial',10,'bold'), command=reali_cadstro)
botao6.place(relx=0.35, rely = 0.8)


iniciando = buscarUsuario()
tela.mainloop()

