from tkinter import *

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
        self.root.minsize(width=400, height=300)
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
        # ---------------- BOTÕES -------------------------
        self.bt_cadastrar = Button(
            self.frameSup, 
            text="Cadastrar Ação", 
            font= "helvetica 9 bold"
        )
        self.bt_cadastrar.place(
            relx=0.2,
            rely=0.1,
            relwidth=0.15,
            relheight=0.15
        )
        self.bt_analise = Button(
            self.frameSup, 
            text="Análise", 
            font= "helvetica 10 bold"
        )
        self.bt_analise.place(
            relx=0.4,
            rely=0.1,
            relwidth=0.15,
            relheight=0.15
        )
        

Application()