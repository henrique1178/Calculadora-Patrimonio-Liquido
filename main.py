from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from colors import *

# criando a janela
janela = Tk()
janela.title("")
janela.geometry("380x500")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# aplicando tema
style = ttk.Style(janela)
style.theme_use('clam')

# criando frames
frameCima = Frame(janela, width=380, height=50, bg=co1)
frameCima.grid(row=0, column=0, columnspan=2)

framedResultado = Frame(janela, width=380, height=50, bg=co3)
framedResultado.grid(row=1, column=0, pady=10)

framedBaixo = Frame(janela, width=380, height=400, bg=co3)
framedBaixo.grid(row=2, column=0, pady=10)

# dividindo os frames de baixo
frameAtivos = Frame(framedBaixo, width=180, height=370, bg=co9)
frameAtivos.grid(row=0, column=0, padx=4)

framePassivo = Frame(framedBaixo, width=180, height=370, bg=co9)
framePassivo.grid(row=0, column=1)

# LOGO
# abrindo a imagem
app_img = Image.open(r'C:\Users\anton\OneDrive\Documentos\CalcularPatrimonio\images\logo.png')
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

# Ajustando a largura do Label que contém a imagem
app_logo = Label(frameCima, image=app_img, bg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text='Calculadora de Patrimônio Líquido', width=900, compound=LEFT, padx=5, anchor=NW,
             font=('Ivy,12'), bg=co1, fg=co4)
app_.place(x=50, y=0)

l_linha = Label(frameCima, width=380, anchor=NW, font=('Verdana,1'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# calcular o valor
def calcularvalor():
    # obter valor dos ativos
    ativo1 = e_valor_casa.get()
    ativo2 = e_valor_imoveis.get()
    ativo3 = e_valor_veiculos.get()
    ativo4 = e_valor_investimentos.get()
    ativo5 = e_valor_outros.get()

    # obter valor do passivo
    passivo1 = e_hipoteca.get()
    passivo2 = e_emprestimos_carro.get()
    passivo3 = e_emprestimos_estudantis.get()
    passivo4 = e_outros_dividas.get()

    # verificar se todos os campos estão preenchidos
    if any(valor == '' for valor in [ativo1, ativo2, ativo3, ativo4, ativo5, passivo1, passivo2, passivo3, passivo4]):
        print('Todos os Campos devem estar preenchidos!!')
        return
    
    # calcular total de ativos e passivos
    Total_ativos = sum(float(valor) for valor in [ativo1, ativo2, ativo3, ativo4, ativo5])
    Total_passivo = sum(float(valor) for valor in [passivo1, passivo2, passivo3, passivo4])
    
    # calcular patrimônio líquido
    Patrimonio_Liquido = Total_ativos - Total_passivo
    l_resultado['text'] = 'R${:,.2f}'.format(Patrimonio_Liquido)

# Entrando Ativos
l_nome = Label(frameAtivos, text='Insira Ativos', padx=10, width=35, height=1, anchor=NW, font=('Verdana,11'), bg=co2, fg=co1)
l_nome.place(x=0, y=0)

# Valor Casa
l_nome = Label(frameAtivos, text='Valor Casa', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=40)
e_valor_casa = Entry(frameAtivos, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_valor_casa.place(x=10, y=65)

# Imóveis
l_nome = Label(frameAtivos, text='Valor Imóveis', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=105)
e_valor_imoveis = Entry(frameAtivos, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_valor_imoveis.place(x=10, y=125)

# Veículos
l_nome = Label(frameAtivos, text='Veículos', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=165)
e_valor_veiculos = Entry(frameAtivos, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_valor_veiculos.place(x=10, y=195)

# Investimentos
l_nome = Label(frameAtivos, text='Investimentos', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=230)
e_valor_investimentos = Entry(frameAtivos, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_valor_investimentos.place(x=10, y=255)

# Outros Ativos
l_nome = Label(frameAtivos, text='Outros Ativos', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=295)
e_valor_outros = Entry(frameAtivos, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_valor_outros.place(x=10, y=315)

# Entrando Passivos
l_nome = Label(framePassivo, text='Insira Passivos', padx=10, width=35, height=1, anchor=NW, font=('Verdana,11'), bg=co5, fg=co1)
l_nome.place(x=0, y=0)

# Hipoteca
l_nome = Label(framePassivo, text='Hipoteca', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=40)
e_hipoteca = Entry(framePassivo, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_hipoteca.place(x=10, y=65)

# Empréstimos de Carro
l_nome = Label(framePassivo, text='Empréstimos de Carro', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=105)
e_emprestimos_carro = Entry(framePassivo, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_emprestimos_carro.place(x=10, y=125)

# Empréstimos Estudantis
l_nome = Label(framePassivo, text='Empréstimos Estudantis', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=165)
e_emprestimos_estudantis = Entry(framePassivo, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_emprestimos_estudantis.place(x=10, y=195)

# Outras Dívidas
l_nome = Label(framePassivo, text='Outras Dívidas', anchor=E, font=('Verdana,9'), bg=co9, fg=co0)
l_nome.place(x=10, y=230)
e_outros_dividas = Entry(framePassivo, width=10, font=('Ivy,12'), justify='center', relief='solid')
e_outros_dividas.place(x=10, y=255)

# resultado
l_resultado = Label(framedResultado, text='R${:,.2f}'.format(0), padx=10, width=15, anchor=NE, font=('Verdana 25 bold'), bg=co3, fg=co1)
l_resultado.place(x=0, y=7)

botao_calcular = Button(framePassivo, command=calcularvalor, text='Calcular'.upper(), padx=10, width=12, anchor='center', font=('Ivy 9 bold'), bg=co1, fg=co0)
botao_calcular.place(x=10, y=310)

janela.mainloop()