import tkinter as tk
# janela
janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('600x430')
# titulo
lblTitulo = tk.Label(janela, text="CALCULADORA",fg="black",
                     font=('Comic Sans MS',20))
lblTitulo.place(x=190,y=20)
# valor 1
lblValor1 = tk.Label(janela, text="Valor 1:",fg="black",
                     font=('Verdana',16))
lblValor1.place(x=100,y=80)
entValor1 = tk.Entry(janela, font=('Verdana',16), width=15)
entValor1.place(x=250,y=80)
# valor 2
lblValor2 = tk.Label(janela, text="Valor 2:",fg="black",
                     font=('Verdana',16))
lblValor2.place(x=100,y=150)
entValor2 = tk.Entry(janela, font=('Arial bold',16), width=15)
entValor2.place(x=250,y=150)
# resultado
lblResult = tk.Label(janela, text="Resultado: ???",fg="black", width=15,
                     font=('Arial bold',16))
lblResult.place(x=250,y=250)
# funções de cálculo disparadas pelos botões
def somar(): # soma dois valores
    resultado = float(entValor1.get()) + float(entValor2.get())
    lblResult["text"] = "Resultado: "+str(resultado)
def subtrair(): # subtrai dos valores
    resultado = float(entValor1.get()) - float(entValor2.get())
    lblResult["text"] = "Resultado: "+str(resultado)
def multiplicar(): # multiplica dois valores
    resultado = float(entValor1.get()) * float(entValor2.get())
    lblResult["text"] = "Resultado: "+str(resultado)
def dividir(): # divide dois valores
    resultado = float(entValor1.get()) / float(entValor2.get())
    lblResult["text"] = "Resultado: "+str(resultado)
def limpar(): # limpa os campos de entrada
    entValor1.delete(0, tk.END)
    entValor2.delete(0, tk.END)
    lblResult["text"] = "Resultado: ???"
# criando botões com as operações
btSomar = tk.Button(janela, text='Somar',width=10, command=somar)
btSubtrair = tk.Button(janela, text='Subtrair',width=10, command=subtrair)
btMultiplicar = tk.Button(janela, text='Multiplicar',width=10, command=multiplicar)
btDividir = tk.Button(janela, text='Dividir',width=10, command=dividir)
btLimpar = tk.Button(janela, text='Limpar',width=10, command=limpar)
btTerminar = tk.Button(janela, text='Fim',width=10, command=janela.destroy)
# posicionando botões
btSomar.place(x=40,y=340)
btSubtrair.place(x=180,y=340)
btMultiplicar.place(x=320,y=340)
btDividir.place(x=460,y=340)
btLimpar.place(x=40,y=380)
btTerminar.place(x=460,y=380)
# exibindo a tela da aplicação
janela.mainloop()