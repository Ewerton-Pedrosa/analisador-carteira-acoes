from tkinter import *
from tkinter import font

root = Tk()

class Application ():
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        root.mainloop()    
    def tela(self):
        self.root.title("Analisador de Portifólio de Ações - Ewerton Diniz")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=650, height=550)
    def frames(self):
        self.frameSup = Frame(
            self.root, 
            bd= 4, 
            bg= '#e8f1f2', 
            highlightbackground='#1b98e0', 
            highlightthickness=1
            )
        self.frameSup.place(
            relx= 0.02, 
            rely=0.1, 
            relwidth=0.96, 
            relheight=0.42
            )
        self.frameInf = Frame(
            self.root, 
            bd= 4, 
            bg= '#e8f1f2', 
            highlightbackground='#1b98e0', 
            highlightthickness=1
            )
        self.frameInf.place(
            relx= 0.02, 
            rely=0.54, 
            relwidth=0.96, 
            relheight=0.42
            )
    def widgets(self):
        # -------------------- BOTÕES --------------------
        self.bt_cadastrar = Button(
            self.frameSup, 
            text="Cadastrar Ação", 
            font= "helvetica 9 bold"
        )
        self.bt_cadastrar.place(
            relx=0.55,
            rely=0.05,
            relwidth=0.15,
            relheight=0.15
        )
        self.bt_analise = Button(
            self.frameSup, 
            text="Análise", 
            font= "helvetica 10 bold"
        )
        self.bt_analise.place(
            relx=0.7,
            rely=0.05,
            relwidth=0.15,
            relheight=0.15
        )
        self.bt_limpar = Button(
            self.frameSup, 
            text="Limpar", 
            font= "helvetica 10 bold"
        )
        self.bt_limpar.place(
            relx=0.85,
            rely=0.05,
            relwidth=0.15,
            relheight=0.15
        )
        # -------------------- LABELS E ENTRYS --------------------
        self.lb_acao = Label(
            self.frameSup, 
            text="Código da Ação", 
            font="helvetica 9 bold"
            )
        self.lb_acao.place(
            relx=0.01, 
            rely=0.1
            )
        self.entry_acao = Entry(
            self.frameSup
        )
        self.entry_acao.place(
            relx=0.01,
            rely=0.2
        )
        self.lb_cotas = Label(
            self.frameSup, 
            text="Quantidade de Cotas", 
            font="helvetica 9 bold"
            )
        self.lb_cotas.place(
            relx=0.01, 
            rely=0.3
            )
        self.entry_cotas = Entry(
            self.frameSup
        )
        self.entry_cotas.place(
            relx=0.01,
            rely=0.4
        )
        self.lb_dataAquisicao = Label(
            self.frameSup, 
            text="Data de Aquisição", 
            font="helvetica 9 bold"
            )
        self.lb_dataAquisicao.place(
            relx=0.01, 
            rely=0.5
            )
        self.entry_dataAquisicao = Entry(
            self.frameSup
        )
        self.entry_dataAquisicao.place(
            relx=0.01,
            rely=0.6
        )
        self.lb_comentarios = Label(
            self.frameSup, 
            text="Comentarios", 
            font="helvetica 9 bold"
            )
        self.lb_comentarios.place(
            relx=0.01, 
            rely=0.7,            
            )
        self.entry_comentarios = Entry(
            self.frameSup
        )
        self.entry_comentarios.place(
            relx=0.01,
            rely=0.8,
            relwidth=0.8
        )
        
Application()