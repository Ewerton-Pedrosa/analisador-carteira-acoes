from tkinter import *
from tkinter import font
from tkinter import ttk
from pandas_datareader import data as web
from datetime import datetime
from sys import displayhook
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()

class Application ():
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.lista_frameinf()  
        self.variaveis() 
        self.graficos()  
        root.mainloop()    
    def tela(self):
        self.root.title("Analisador de Portifólio de Ações - Ewerton Diniz")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=650, height=550)
    def variaveis(self):
        self.cont = 0
        self.montanteInicial = []
        self.montanteHoje = []
        self.portifolio = []
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
            relheight=0.62
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
            rely=0.73, 
            relwidth=0.96, 
            relheight=0.26
            )
    def widgets(self):
        # -------------------- ABAS --------------------
        self.abas = ttk.Notebook(self.frameSup)
        self.abaCadastro = Frame(self.abas)
        self.abaAnaliseGeral = Frame(self.abas)

        self.abaCadastro.configure(background='#e8f1f2')
        self.abaAnaliseGeral.configure(background='white')

        self.abas.add(self.abaCadastro, text='Cadastro')
        self.abas.add(self.abaAnaliseGeral, text='Análise Geral')

        self.abas.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )
        # -------------------- BOTÕES --------------------
        self.bt_cadastrar = Button(
            self.abaCadastro, 
            text="Cadastrar Ação", 
            font= "helvetica 9 bold",
            bd=3,
            bg="#1e3743",
            fg='white',
            command= self.lista_dados
        )
        self.bt_cadastrar.place(
            relx=0.55,
            rely=0.05,
            relwidth=0.15,
            relheight=0.15
        )
        self.bt_analise = Button(
            self.abaCadastro, 
            text="Análise", 
            font= "helvetica 10 bold",
            bd=3,
            bg="#1e3743",
            fg='white'
        )
        self.bt_analise.place(
            relx=0.7,
            rely=0.05,
            relwidth=0.15,
            relheight=0.15
        )
        self.bt_limpar = Button(
            self.abaCadastro, 
            text="Limpar", 
            font= "helvetica 10 bold",
            bd=3,
            bg="#1e3743",
            fg='white',
            command=self.limpar_entrys
        )
        self.bt_limpar.place(
            relx=0.85,
            rely=0.05,
            relwidth=0.15,
            relheight=0.15
        )
        # -------------------- LABELS E ENTRYS --------------------
        self.lb_acao = Label(
            self.abaCadastro, 
            text="Código da Ação", 
            font="helvetica 9 bold"
            )
        self.lb_acao.place(
            relx=0.01, 
            rely=0.1
            )
        self.entry_acao = Entry(
            self.abaCadastro
        )
        self.entry_acao.place(
            relx=0.01,
            rely=0.2
        )
        self.lb_cotas = Label(
            self.abaCadastro, 
            text="Quantidade de Cotas", 
            font="helvetica 9 bold"
            )
        self.lb_cotas.place(
            relx=0.01, 
            rely=0.3
            )
        self.entry_cotas = Entry(
            self.abaCadastro
        )
        self.entry_cotas.place(
            relx=0.01,
            rely=0.4
        )
        self.lb_dataAquisicao = Label(
            self.abaCadastro, 
            text="Data de Aquisição", 
            font="helvetica 9 bold"
            )
        self.lb_dataAquisicao.place(
            relx=0.01, 
            rely=0.5
            )
        self.entry_dataAquisicao = Entry(
            self.abaCadastro
        )
        self.entry_dataAquisicao.place(
            relx=0.01,
            rely=0.6
        )
        self.lb_comentarios = Label(
            self.abaCadastro, 
            text="Comentários", 
            font="helvetica 9 bold"
            )
        self.lb_comentarios.place(
            relx=0.01, 
            rely=0.7,            
            )
        self.entry_comentarios = Entry(
            self.abaCadastro
        )
        self.entry_comentarios.place(
            relx=0.01,
            rely=0.8,
            relwidth=0.8
        )
    def lista_frameinf(self):
        self.listaAcoes = ttk.Treeview(
            self.frameInf,
            height=3,
            columns=("col1, col2, col3, col4")
        ) 
        self.listaAcoes.heading("#0", text="")
        self.listaAcoes.heading("#1", text="Código da Ação")
        self.listaAcoes.heading("#2", text="Número de Cotas")
        self.listaAcoes.heading("#3", text="Data de Aquisição")
        self.listaAcoes.heading("#4", text="Comentários")

        self.listaAcoes.column("#0", width=1, stretch=NO)
        self.listaAcoes.column("#1", width=110)
        self.listaAcoes.column("#2", width=110)
        self.listaAcoes.column("#3", width=150)
        self.listaAcoes.column("#4", width=200)

        self.listaAcoes.place(
            relx=0.01, 
            rely=0.1, 
            relwidth=0.95, 
            relheight=0.85
            )
       
        self.scrollLista = Scrollbar(self.frameInf, orient='vertical')
        self.listaAcoes.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(
            relx=0.96,
            rely=0.1,
            relwidth=0.04,
            relheight=0.85
        )
    def lista_dados(self):                       
        self.listaAcoes.insert(
            parent='',
            index='end', 
            iid=self.cont, 
            values=(
                self.entry_acao.get(),
                self.entry_cotas.get(), 
                self.entry_dataAquisicao.get(), 
                self.entry_comentarios.get()
                )
            )
        self.cont +=1
        self.graficos()
        self.limpar_entrys()
    def limpar_entrys(self):
        self.entry_acao.delete(0, END)
        self.entry_cotas.delete(0, END)
        self.entry_dataAquisicao.delete(0, END)
        self.entry_comentarios.delete(0, END)
    def graficos(self):
        if self.cont != 0 :
            self.cotacaoAcao = web.DataReader(
                self.entry_acao.get() + '.SA', 
                data_source='yahoo', 
                start=self.entry_dataAquisicao.get(), 
                end=datetime.today().strftime('%m-%d-%Y')
                )
            self.montanteInicial.append(round(float(self.cotacaoAcao['Adj Close'].iloc[0])*int(self.entry_cotas.get()), 2))
            self.montanteHoje.append(round(float(self.cotacaoAcao['Adj Close'].iloc[-1])*int(self.entry_cotas.get()), 2))  
            self.portifolio.append(self.entry_acao.get().upper())
            print(f'Esse é o montante hoje: R$ {self.montanteHoje}')
            print(f'Esse é o montante inicial: R$ {self.montanteInicial}') 
            print(f'Esse é o Portifólio de Ações: {self.portifolio}') 

            # -------------------- FIGURA INTEGRADA A ABA ANALISE --------------------
            self.figura = plt.figure(
                figsize= (6, 3), 
                dpi=60
                )
            self.grafico = self.figura.add_subplot(111)
            self.canva = FigureCanvasTkAgg(self.figura, self.abaAnaliseGeral )
            self.canva.get_tk_widget().place(
                relx=0.01,
                rely=0.01, 
                relwidth=0.45,
                relheight=0.45               
            )
            plt.pie(
                x=self.montanteHoje,
                labels=self.portifolio,
                autopct='%1.1f%%',
                startangle=90,
                shadow=True
                )
            
            
Application()