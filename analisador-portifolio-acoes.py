from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pandas_datareader import data as web
from datetime import datetime
from sys import displayhook
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import base64

root = Tk()

class Application ():
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.lista_frameinf()  
        self.variaveis()
        self.menuAcoes()                  
        root.mainloop()    
    
    def tela(self):
        self.root.title("Analisador de Portifólio de Ações - Ewerton Diniz")
        self.root.configure(background='#2F4F4F')
        self.root.geometry("900x600")
        self.root.resizable(True,True)
        self.root.maxsize(width=1200, height=900)
        self.root.minsize(width=750, height=600)
    
    def variaveis(self):
        self.cont = 0
        self.montanteInicial = []
        self.montanteHoje = []
        self.portifolio = []
        self.dict_acaoDataAquisicao = {}    
    
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
        self.abaAnaliseIndividual = Frame(self.abas)

        self.abaCadastro.configure(background='#e8f1f2')
        self.abaAnaliseGeral.configure(background='white')
        self.abaAnaliseIndividual.configure(background='white')

        self.abas.add(self.abaCadastro, text='Cadastro')
        self.abas.add(self.abaAnaliseGeral, text='Análise Geral')
        self.abas.add(self.abaAnaliseIndividual, text='Análise Individual')

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
            command= self.cadastro_dados
        )
        self.bt_cadastrar.place(
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
            command=self.deleteItemTreeView
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
        self.entry_acao = Entry(self.abaCadastro)
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
        self.entry_cotas = Entry(self.abaCadastro)
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
        self.entry_dataAquisicao = Entry(self.abaCadastro)
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
        self.entry_comentarios = Entry(self.abaCadastro)
        self.entry_comentarios.place(
            relx=0.01,
            rely=0.8,
            relwidth=0.8
        )
    
    def lista_frameinf(self):
        self.trv_listaAcoes = ttk.Treeview(
            self.frameInf,
            height=7,
            columns=("col1, col2, col3, col4, col5, col6, col7")
        ) 
        self.trv_listaAcoes.heading("#0", text="", anchor=CENTER)
        self.trv_listaAcoes.heading("#1", text="Código da Ação", anchor=CENTER)
        self.trv_listaAcoes.heading("#2", text="Número de Cotas", anchor=CENTER)
        self.trv_listaAcoes.heading("#3", text="Data de Aquisição", anchor=CENTER)
        self.trv_listaAcoes.heading("#4", text="Investido", anchor=CENTER)
        self.trv_listaAcoes.heading("#5", text="Acumulado", anchor=CENTER)
        self.trv_listaAcoes.heading("#6", text="Rendimento", anchor=CENTER)
        self.trv_listaAcoes.heading("#7", text="Comentários", anchor=CENTER)

        self.trv_listaAcoes.column("#0", width=1, stretch=NO, anchor=CENTER)
        self.trv_listaAcoes.column("#1", width=110, anchor=CENTER)
        self.trv_listaAcoes.column("#2", width=100, anchor=CENTER)
        self.trv_listaAcoes.column("#3", width=130, anchor=CENTER)
        self.trv_listaAcoes.column("#4", width=100, anchor=CENTER)
        self.trv_listaAcoes.column("#5", width=100, anchor=CENTER)
        self.trv_listaAcoes.column("#6", width=120, anchor=CENTER)
        self.trv_listaAcoes.column("#7", width=250, anchor=CENTER)

        self.trv_listaAcoes.place(
            relx=0.01, 
            rely=0.01, 
            relwidth=0.96, 
            relheight=0.85
            )
       
        self.scrollListaY = Scrollbar(self.frameInf, orient='vertical', command=self.trv_listaAcoes.yview)
        self.trv_listaAcoes.configure(yscroll=self.scrollListaY.set)
        self.scrollListaY.pack(side= RIGHT, fill='y') # o Método Pack foi mais eficaz na criação do scroll
        
        self.scrollListaX = Scrollbar(self.frameInf, orient='horizontal', command=self.trv_listaAcoes.xview)
        self.trv_listaAcoes.configure(xscrollcommand=self.scrollListaX.set)
        self.scrollListaX.pack(side= BOTTOM, fill='x')
        
    def cadastro_dados(self):
        # -------------------- CONSULTA API --------------------        
        try:
            self.cotacaoAcao = web.DataReader(
                self.entry_acao.get() + '.SA', 
                data_source='yahoo', 
                start=self.entry_dataAquisicao.get(), 
                end=datetime.today().strftime('%m-%d-%Y')
                )
        except:
            messagebox.showerror(title='ERRO', message='Verifique os dados de entrada e tente novamente')            
        # -------------------- LISTAS PARA GRAFICOS PIZZA --------------------    
        self.montanteInicial.append(round(float(self.cotacaoAcao['Adj Close'].iloc[0])*int(self.entry_cotas.get()), 2))
        self.montanteHoje.append(round(float(self.cotacaoAcao['Adj Close'].iloc[-1])*int(self.entry_cotas.get()), 2))  
        self.portifolio.append(self.entry_acao.get().upper())
        # -------------------- DICIONÁRIO ACAO X DATA AQUISICAO PARA GRAFICOS INDIVIDUAIS --------------------
        self.dict_acaoDataAquisicao [self.entry_acao.get().upper()] = self.entry_dataAquisicao.get()
        print(self.dict_acaoDataAquisicao)
        # -------------------- DADOS NA TREE VIEW --------------------                       
        self.trv_listaAcoes.insert(
            parent='',
            index='end', 
            iid=self.cont, 
            values=(
                self.entry_acao.get().upper(),
                self.entry_cotas.get(), 
                self.entry_dataAquisicao.get(),
                f'R${(self.montanteInicial[self.cont]):.2f}', 
                f'R${(self.montanteHoje[self.cont]):.2f}',
                f'R${(float(self.montanteHoje[self.cont])-float(self.montanteInicial[self.cont])):.2f} ({(((float(self.montanteHoje[self.cont])-float(self.montanteInicial[self.cont]))*100)/float(self.montanteInicial[self.cont])):.2f}%)',
                self.entry_comentarios.get()
                )            
            )
        self.cont +=1
        self.graficos() 
        self.menuAcoes()               
        self.limpar_entrys()

    def limpar_entrys(self):            
        self.entry_acao.delete(0, END)
        self.entry_cotas.delete(0, END)
        self.entry_dataAquisicao.delete(0, END)
        self.entry_comentarios.delete(0, END) 

    def deleteItemTreeView(self):
        self.cont -= 1 #variável que demarca os endereços de indexação
        self.linhaSelecionada = self.trv_listaAcoes.selection()[0]        
        self.acaoSelecionada = self.trv_listaAcoes.item(self.linhaSelecionada, "values")[0]
        print(self.acaoSelecionada)
        del self.dict_acaoDataAquisicao[self.acaoSelecionada]
        self.trv_listaAcoes.delete(self.linhaSelecionada)
        print(self.dict_acaoDataAquisicao)
        self.montanteInicial.pop(int(self.linhaSelecionada))
        self.montanteHoje.pop(int(self.linhaSelecionada))
        self.portifolio.pop(int(self.linhaSelecionada))
        self.graficos()
        self.menuAcoes()

    def graficos(self):        
            # -------------------- GRAFICO INVESTIMENTO INICIAL --------------------
            self.figura = plt.figure(
                figsize= (6, 3), 
                dpi=70
                )
            self.grafico = self.figura.add_subplot(111)
            self.canva = FigureCanvasTkAgg(self.figura, self.abaAnaliseGeral )
            self.canva.get_tk_widget().place(
                relx=-0.1,
                rely=0.01, 
                relwidth=0.65,
                relheight=0.65               
            )
            plt.pie(
                x=self.montanteInicial,
                labels=self.portifolio,                
                autopct='%1.1f%%',
                startangle=90,
                shadow=True
                )            
            self.lb_totalInvestido = Label(
                self.abaAnaliseGeral,
                text='Total Investido',
                font='helvetica 11 bold',
                background='white'
                )
            self.lb_totalInvestido.place(
                relx=0.17,
                rely=0.75,                
            )
            self.entry_totalInvestido = Entry(self.abaAnaliseGeral)
            self.entry_totalInvestido.place(
                relx=0.17,
                rely=0.85
            )
            self.entry_totalInvestido.insert(0, f'R$ {sum(self.montanteInicial):.2f}')
             # -------------------- GRAFICO INVESTIMENTO ACUMULADO --------------------
            self.figura = plt.figure(
                figsize= (6, 3), 
                dpi=70
                )
            self.grafico = self.figura.add_subplot(111)
            self.canva = FigureCanvasTkAgg(self.figura, self.abaAnaliseGeral )
            self.canva.get_tk_widget().place(
                relx=0.45,
                rely=0.01, 
                relwidth=0.65,
                relheight=0.65               
            )
            plt.pie(
                x=self.montanteHoje,
                labels=self.portifolio, 
                autopct='%1.1f%%',
                startangle=90,
                shadow=True
            )
            self.lb_totalAcumulado = Label(
                self.abaAnaliseGeral,
                text='Total Acumulado',
                font='helvetica 11 bold',
                background='white'
                )
            self.lb_totalAcumulado.place(
                relx=0.72,
                rely=0.75,                
            )
            self.entry_totalAcumulado = Entry(self.abaAnaliseGeral)
            self.entry_totalAcumulado.place(
                relx=0.72,
                rely=0.85
            )
            self.entry_totalAcumulado.insert(0, f'R$ {sum(self.montanteHoje):.2f}')
            #-------------------- LABEL RENDIMENTO DA CARTEIRA --------------------
            self.vr_rendimentoCarteira = float((sum(self.montanteHoje))*100/float(sum(self.montanteInicial))-100)
            self.lb_rendimentoCarteira = Label(
                self.abaAnaliseGeral,
                bg='white',
                text=f'Sua carteira teve um rendimento de {self.vr_rendimentoCarteira:.2f}%',
                font='helvetica 10 bold'
            )
            self.lb_rendimentoCarteira.place(relx=0.35, rely=0.5)

    def graficosIndividuais(self):
        self.cotacaoAcaoIndividual = web.DataReader(
            self.acaoEscolhida.get() + '.SA', 
            data_source='yahoo', 
            start=self.dict_acaoDataAquisicao[self.acaoEscolhida.get()], #usar um dicionario key=acao, product=dataAquisicao
            end=datetime.today().strftime('%m-%d-%Y')
            )
        displayhook(self.cotacaoAcaoIndividual)
       # -------------------- CRIA O ESPAÇO QUE RECEBERÁ O GRÁFICO DE LINHA --------------------
        self.figura = plt.figure(
                figsize= (6, 3), 
                dpi=70
                )
        self.grafico = self.figura.add_subplot(111)
        self.canva = FigureCanvasTkAgg(self.figura, self.abaAnaliseIndividual )
        self.canva.get_tk_widget().place(
            relx=0.02,
            rely=0.1, 
            relwidth=0.5,
            relheight=0.85               
        )
        # -------------------- PLOTA O GRÁFICO DE LINHA NO ESPAÇO CRIADO ANTERIORMENTE --------------------
        self.cotacaoAcaoIndividual['Adj Close'].plot(figsize=(6, 3))
        plt.ylabel("PREÇO POR COTA EM R$", fontsize=11)
        plt.xlabel("DATA", fontsize=11)              
         # -------------------- CRIA O ESPAÇO QUE RECEBERÁ O GRÁFICO DE BARRA --------------------
        self.figura = plt.figure(
                figsize= (6, 3), 
                dpi=70
                )
        self.grafico = self.figura.add_subplot(111)
        self.canva = FigureCanvasTkAgg(self.figura, self.abaAnaliseIndividual )
        self.canva.get_tk_widget().place(
            relx=0.53,
            rely=0.1, 
            relwidth=0.5,
            relheight=0.85  
        )
        # -------------------- PLOTA O GRÁFICO DE BARRA NO ESPAÇO CRIADO ANTERIORMENTE --------------------
        self.cotacaoAcaoIndividual['Volume'].plot(figsize=(6,3))
        plt.ylabel("VOLUME DE AÇÕES NEGOCIADAS", fontsize= 11)
        plt.xlabel("DATA", fontsize= 11)

    def menuAcoes(self):  
        if self.cont != 0: # Cria somente depois da primeira inserção de dados 
            if self.cont > 1: # destroi antes de criar o menuOption se já houver outro menuOption
                self.menuOption.destroy()   
            self.acaoEscolhida = StringVar(self.abaAnaliseIndividual)
            self.acaoEscolhida.set(self.portifolio[0])
            self.menuOption = OptionMenu(self.abaAnaliseIndividual, self.acaoEscolhida, *self.portifolio)
            self.menuOption.place(relx=0.02, rely=0.02)
            self.bt_analise = Button(
            self.abaAnaliseIndividual, 
                text="Análise", 
                font= "helvetica 10 bold",
                bd=3,
                bg="#1e3743",
                fg='white',
                command=self.graficosIndividuais
            )
            self.bt_analise.place(
                relx=0.85,
                rely=0.01,
                relwidth=0.1,
                relheight=0.1
            )
    
Application()
