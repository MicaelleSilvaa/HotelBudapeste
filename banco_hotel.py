import customtkinter
from caixa import Banco
from tkinter import ttk, font
from tkinter import messagebox
from tkinter import *

class ModeloTelaPrincipal(Banco):
    def __init__(self, windows):
        self.janela = windows
        self.janela.title('Budapeste Hotel')
        self.janela.geometry('1000x600+0+0')
        '''self.janela._set_appearance_mode('dark')'''
        self.janela['bg']= '#242424'
        self.janela.resizable(width=False, height=False)
        self.img = PhotoImage(file='imagens/2.png')
        self.label_cpf = Label(self.janela, image= self.img, borderwidth= 0)
        self.label_cpf.place(x=20, y=20)

        self.img2 = PhotoImage(file='imagens/nome.png')
        self.label_cpf2 = Label(self.janela, image= self.img2, borderwidth= 0)
        self.label_cpf2.place(x=800, y= 520)

        
        self.criar_tabela()
        self.frames_cadastro = []


    #--------------------- Título ---------
        '''self.titulo = customtkinter.CTkLabel(self.janela,
        text='Cadastro de Hóspedes',
        font=('Poppins Bold', 25, 'italic'),
        text_color='white', fg_color= '#242424')
        self.titulo.place(x=10, y= 20)'''
    #---------------------- Labels e caixas de textos --------------------
        self.label_nome = customtkinter.CTkLabel(self.janela,
        text='Nome',
        font=('times', 20, 'italic'), text_color= '#F2A516', fg_color= '#242424')
        self.label_nome.place(x=250, y=20)

        self.caixa_nome = customtkinter.CTkEntry(self.janela,
        placeholder_text='Digite o nome',
        width=200, height=30,
        fg_color='black', border_width= 0, text_color= 'white')
        self.caixa_nome.place(x=250, y= 50)

        self.cpf = customtkinter.CTkLabel(self.janela,
        text='CPF',
        font=('times', 20, 'italic'), text_color= '#F2A516', fg_color= '#242424')
        self.cpf.place(x=250, y=90)

        self.caixa_cpf = customtkinter.CTkEntry(self.janela,
        placeholder_text='Digite o cpf',
        width=200, height=30,
        fg_color='black', border_color= '#8C694A', border_width= 0, text_color= 'white')
        self.caixa_cpf.place(x=250, y=120)
        
        self.data = customtkinter.CTkLabel(self.janela,text='Data',
        font=('times', 20, 'italic'), text_color= '#F2A516', fg_color= '#242424')
        self.data.place(x= 250, y= 160)
               
        
        self.caixa_data = customtkinter.CTkEntry(self.janela,placeholder_text='Digite a data de cadastro',
        width=200, height=30,
        fg_color='black', border_width= 0, text_color= 'white' )
        self.caixa_data.place(x=250, y= 190)
        
        
        self.email = customtkinter.CTkLabel(self.janela,text='Email',
        font=('times', 20, 'italic'), text_color= '#F2A516', fg_color= '#242424')
        self.email.place(x= 500, y= 20)

        self.caixa_email = customtkinter.CTkEntry(self.janela,placeholder_text='Digite o email',
        width=200, height=30,
        fg_color='black', border_width= 0, text_color= 'white')
        self.caixa_email.place(x=500, y= 50)

        self.contato = customtkinter.CTkLabel(self.janela,text='Contato',
        font=('times', 20, 'italic'), text_color= '#F2A516', fg_color= '#242424')
        self.contato.place(x= 500, y= 90)

        self.caixa_contato = customtkinter.CTkEntry(self.janela,placeholder_text='Digite o contato',
        width=200, height=30,
        fg_color='black', border_width= 0, text_color= 'white' )
        self.caixa_contato.place(x=500, y= 120)
        
        self.quarto = customtkinter.CTkLabel(self.janela,text='Quarto',
        font=('times', 20, 'italic'), text_color= '#F2A516', fg_color= '#242424')
        self.quarto.place(x= 500, y= 160)

        self.caixa_quarto = customtkinter.CTkEntry(self.janela,placeholder_text='Digite o número do quarto',
        width=200, height=30,
        fg_color='black', border_width= 0, text_color= 'white' )
        self.caixa_quarto.place(x=500, y= 190)
        
        
        #------------------------VISUALIZAÇÃO PELA TREEVIEW-------------------------
        
        
        self.relatorio = ttk.Treeview(self.janela, columns=('id', 'nome_hospede', 'email_hospede',
                                                            'cpf_hospede', 'contato_hospede', 'quarto_hospede', 'data_hospede'),
                                      show='headings')
        self.relatorio.column('id', minwidth=50, width=30)
        self.relatorio.column('nome_hospede', minwidth=50, width=50)
        self.relatorio.column('email_hospede', minwidth=50, width=50)
        self.relatorio.column('cpf_hospede', minwidth=50, width=50)
        self.relatorio.column('contato_hospede', minwidth=50, width=50)
        self.relatorio.column('quarto_hospede', minwidth=50, width=50)
        self.relatorio.column('data_hospede', minwidth=50, width=50)

        self.relatorio.heading('id', text='ID')
        self.relatorio.heading('nome_hospede', text='NOME')
        self.relatorio.heading('email_hospede', text='EMAIL')
        self.relatorio.heading('cpf_hospede', text='CPF')
        self.relatorio.heading('contato_hospede', text='CONTATO')
        self.relatorio.heading('quarto_hospede', text='QUARTO')
        self.relatorio.heading('data_hospede', text='DATA')


        self.relatorio.place(x=20, y=300)
        self.mostrar_dados()

        self.relatorio.bind('<Double-1>', self.multiplo_clique)
        
        # -----------------------------BOTÕES-------------------------------------------

        self.botao_cadastrar = customtkinter.CTkButton(self.janela,
        text='Cadastrar',
         text_color= '#F2A516', fg_color= 'black', hover_color= 'white', font=('times', 15, 'bold'), command=self.cadastrar)
        self.botao_cadastrar.place(x=400, y=240) #ativar função de cadastro

        self.botao_atualizar = customtkinter.CTkButton(self.janela,
        text='Atualizar', text_color= '#F2A516', fg_color= 'black', hover_color= 'white', font=('times', 15, 'bold'), command=self.atualizar_dados)
        self.botao_atualizar .place(x=400, y=350)

        self.botao_deletar= customtkinter.CTkButton(self.janela,
        text='Deletar', text_color= '#F2A516', fg_color= 'black', hover_color= 'white', font=('times', 15, 'bold'), command=self.deletar_dados)
        self.botao_deletar.place(x=400, y=400)
        
        self.voltar = customtkinter.CTkButton(self.janela,
        text='Lista completa', text_color= '#F2A516', fg_color= 'black', hover_color= 'white', font=('times', 15, 'bold'), command=self.mostrar_dados)
        self.voltar.place(x=400, y=300)

 
        # -------------- PESQUISANDO DADOS -------------------

        self.label_pesquisa = customtkinter.CTkLabel(self.janela,
        text= 'PESQUISA DE CLIENTE',
        font=('times', 15, 'bold'), text_color= '#F2A516')
        self.label_pesquisa.place(x=390, y=440)

        self.caixa_pesquisa = customtkinter.CTkEntry(self.janela, placeholder_text='Digite o cpf')
        self.caixa_pesquisa.place(x=400, y=470), 
        self.botao_pesquisa = customtkinter.CTkButton(self.janela,
        text='Pesquisar', text_color= '#F2A516', fg_color= 'black', hover_color= 'white', font=('times', 15, 'bold'), command=self.pesquisar_dados)
        self.botao_pesquisa.place(x=400, y=500)
        
#---------------------------FUNÇÕES-----------------------------
    
    def aviso(self, numero_quarto):
        frame = Frame(self.janela, bg='#F2A516', width=140, height=80)
        frame.place(x=800, y=len(self.frames_cadastro) * 50 + 50)
        fonte = font.Font(size=12)
        
        # Criando o widget Label dentro do frame
        label = Label(frame, text="RESERVADO\nQuarto " + numero_quarto, fg='black', bg='#F2A516', wraplength=200, font=fonte)
        label.pack(fill='both', expand=True)

        # Adicionando o frame à lista de frames de cadastro
        self.frames_cadastro.append(frame)
        
    def verificar_quarto_ocupado(self, quarto):
        self.conecta_banco()
        self.sql.execute("SELECT * FROM hospedes WHERE quarto_hospede = ?", (quarto,))
        resultado = self.sql.fetchone()
        self.desconecta_banco()
        return resultado is not None


    def cadastrar(self):
        self.capturar_nome = self.caixa_nome.get()
        self.capturar_email = self.caixa_email.get()
        self.capturar_contato = self.caixa_contato.get()
        self.capturar_cpf = self.caixa_cpf.get()
        self.capturar_data = self.caixa_data.get()
        self.capturar_quarto = self.caixa_quarto.get()

        if len(self.capturar_quarto) != 2:
            messagebox.showwarning('Quarto Inválido', 'O número do quarto deve conter apenas dois dígitos.')
            return

        if self.verificar_quarto_ocupado(self.capturar_quarto):
            messagebox.showwarning('Quarto Ocupado', 'Esse quarto já está ocupado.')
            return

        self.conecta_banco()
        self.sql.execute('''INSERT INTO hospedes (nome_hospede, email_hospede,cpf_hospede, contato_hospede, data_hospede, quarto_hospede) 
                         values(?,?,?,?,?,?) ''', (self.capturar_nome, self.capturar_email, self.capturar_cpf, self.capturar_contato,
                                               self.capturar_data, self.capturar_quarto))

        try:
            if self.capturar_nome == '' or self.capturar_email == '' or self.capturar_cpf == '' or self.capturar_contato == '' or self.capturar_data == '' or self.capturar_quarto == '':
                messagebox.showerror('Sistema de cadastro', 'Preencha todos os campos!')
            else:
                self.conexao.commit()
                messagebox.showinfo('Cadastro', f'Parabéns! Dados Salvos!')
                self.mostrar_dados()
                self.desconecta_banco()
                self.aviso(self.capturar_quarto)
                self.limpar_dados()
        except:
            messagebox.showerror('Cadastro', 'Erro no processamento do seu cadastro.')
            self.desconecta_banco()
            self.limpar_dados()

        self.desconecta_banco()



    def mostrar_dados(self): #conectar variáveis
        self.relatorio.delete(*self.relatorio.get_children())
        self.conecta_banco()
        self.sql.execute('''SELECT * FROM hospedes ORDER BY id''')
        self.lista_dados = self.sql.fetchall()
        for item in self.lista_dados:
            self.relatorio.insert('', 'end', values=(item))



    def deletar_dados(self):
        try:
            self.conecta_banco()
            self.selecionar = self.relatorio.item(self.relatorio.selection()[0],'values')
            self.sql.execute('''DELETE FROM hospedes WHERE id=''' + self.selecionar[0])
            self.conexao.commit()

            messagebox.showinfo('Exclusão', 'Dados removidos com Sucesso!')
            self.mostrar_dados()
            self.desconecta_banco()
        except IndexError:
            messagebox.showerror('Exclusão', 'Selecione um dado para excluir')
        self.desconecta_banco()


    def atualizar_dados(self):
        try:
            self.capturar_nome= self.caixa_nome.get()
            self.capturar_cpf= self.caixa_cpf.get()
            self.capturar_data = self.caixa_data.get()
            self.capturar_email = self.caixa_email.get()
            self.capturar_contato = self.caixa_contato.get()
            self.capturar_quarto = self.caixa_quarto.get()
            self.conecta_banco()

            self.selecionar = self.relatorio.item(self.relatorio.selection()[0],'values')
            self.sql.execute(f'UPDATE hospedes SET nome_hospede = ?, cpf_hospede =?, data_hospede = ?, email_hospede = ?, contato_hospede = ?, quarto_hospede = ? where id=?',
                             (self.capturar_nome,self.capturar_cpf, self.capturar_data, self.capturar_email, 
                              self.capturar_contato, self.capturar_quarto, self.selecionar[0]))
            self.conexao.commit()
            self.limpar_dados()

            messagebox.showinfo('Alteração ', 'Dados alterados com sucesso!')
            self.mostrar_dados()
            self.desconecta_banco()
        except IndexError:
            messagebox.showerror('Alteração', 'Selecione um dado para alterar')
            self.desconecta_banco()

    def limpar_dados(self):
        self.caixa_nome.delete(0,END)
        self.caixa_cpf.delete(0,END)
        self.caixa_data.delete(0,END)
        self.caixa_email.delete(0, END)
        self.caixa_contato.delete(0, END)
        self.caixa_quarto.delete(0,END)
       

    def pesquisar_dados(self):
        self.relatorio.delete(*self.relatorio.get_children())
        try:
            self.pesq = self.caixa_pesquisa.get()
            print(self.pesq)
            self.sql.execute('SELECT * FROM hospedes WHERE cpf_hospede LIKE "' + self.pesq + '%" ')
            self.dados = self.sql.fetchall()
            print(self.dados)
            if len(self.dados) == 0:
                messagebox.showwarning('Erro!', 'Esse hóspede não está cadastrado')
            else:
                for item in self.dados:
                    self.relatorio.insert('', 'end', values=(item))
                messagebox.showinfo('Sucesso!', 'Esse hóspede está cadastrado')
        except:
            messagebox.showwarning('Erro!', 'Ocorreu um erro ao pesquisar os dados')


    def multiplo_clique(self, event):
        self.limpar_dados()
        self.caixa_recebe_id = customtkinter.CTkEntry(self.janela)

        self.relatorio.selection()
        for elemento in self.relatorio.selection():
            coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7 = self.relatorio.item(elemento, 'values')
            self.caixa_recebe_id.insert(END, coluna1)
            self.caixa_nome.insert(END, coluna2)
            self.caixa_email.insert(END, coluna3)
            self.caixa_cpf.insert(END, coluna4)
            self.caixa_contato.insert(END, coluna5)
            self.caixa_quarto.insert(END, coluna6)
            self.caixa_data.insert(END, coluna7)

#Feito por Micaelle Silva :)

#----------------------- Chamando a classe ModeloSistema -----------------
windows = Tk()
objeto = ModeloTelaPrincipal(windows)
windows.mainloop()