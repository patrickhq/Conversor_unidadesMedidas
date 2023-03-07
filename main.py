from tkinter import *
from tkinter import ttk

#Importando Pillow
from PIL import ImageTk, Image


#Cores
cor1 = "#3b3b3b" #Preto / Black
cor2 = "#ffffff" #Branco / White
cor3 = "#48b3e0" #Azul / Blue
cor4 = "#ccc90e" #Amarelo/ Yellow


window = Tk()
window.title("Conversor")
window.geometry("650x260")
window.configure(bg=cor1)


# ------------ Frames para Janela -------------

frame_cima = Frame(window, width=450, height=50, bg=cor2, pady = 0, padx=3, relief="flat")
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(window, width=450, height=220, bg=cor2, pady = 0, padx=3, relief="flat")
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(window, width=198, height=260, bg=cor2, pady = 0, padx=3, relief="flat")
frame_direita.place(x=454, y=2)

# ------------ Estilo para Janela -------------
estilo = ttk.Style(window)
estilo.theme_use("clam")

# ------------ Configurando Frame Cima -------------
l_app_nome = Label(frame_cima,text="Conversor de Unidades", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 15 bold"), bg=cor2, fg=cor3)
l_app_nome.place(x=110, y=10)

# ------------ Configurando Funcionalidade -------------

unidades = {"Massa":[{"kg":1000}, {"hg":100}, {"dag":10}, {"g":1}, {"dg":0.1}, {"cg":0.01}, {"mg":0.001}],
            "Comprimento":[{"km":1000}, {"hm":100}, {"dam":10}, {"m":1}, {"dm":0.1}, {"cm":0.01}, {"mm":0.001}]}



def mostrar_menu(i):

    unidade_de = []
    unidade_para = []
    unidade_valores = []

    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    c_de["values"] = unidade_de
    c_para["values"] = unidade_para

    l_unidade_nome["text"] = i

    def calcular():

        # Obtendo as unidades
        a = c_de.get()
        b = c_para.get()

        # Obtendo o numero
        numero_para_converter = float(e_numero.get())

        dist = unidade_para.index(b) - unidade_de.index(a)

        # multiplicação
        if unidade_para.index(a) <= unidade_de.index(b):

            #verificando a posição das unidades para obter valor da distancia.
            distancia = unidade_para.index(b) - unidade_de.index(a)
            resultado = numero_para_converter * (10**distancia)

            l_resultado["text"] = resultado

        else:
            # verificando a posição das unidades para obter valor da distancia.
            distancia = unidade_para.index(a) - unidade_de.index(b)
            resultado = numero_para_converter / (10 ** distancia)

            l_resultado["text"] = resultado

        # Divisão
        if unidade_para.index(a) > unidade_de.index(b):
            if unidade_para.index(a) <= unidade_de.index(b):
                # verificando a posição das unidades para obter valor da distancia.
                distancia = unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter / (10 ** distancia)

                l_resultado["text"] = resultado

            else:
                # verificando a posição das unidades para obter valor da distancia.
                distancia = unidade_para.index(a) - unidade_de.index(b)
                resultado = numero_para_converter / (10 ** distancia)

                l_resultado["text"] = resultado


    #Criando Label, botão e entrada

    l_info = Label(frame_direita, text="Digite o Numero", width=16, height=2, padx=5, pady=3, relief="flat",
                   anchor="center", font=("Ivy 10 bold"), bg=cor2, fg=cor1)
    l_info.place(x=25, y=110)

    e_numero = Entry(frame_direita, width=9, font=("Ivy 15 bold"), justify="center", relief=SOLID)
    e_numero.place(x=10, y=150)

    b_calcular = Button(frame_direita, command=calcular, text="Calcular", width=8, height=1, relief="raised", anchor="nw",
                        overrelief="ridge", font=("Ivy 10 bold"), bg=cor4, fg="black")
    b_calcular.place(x= 115, y= 150)

    l_resultado = Label(frame_direita, text="000000",width=11, height=1, padx=0, pady=3, relief="groove", anchor="center",
                       font=("Ivy 16 bold"), bg=cor2, fg=cor1)
    l_resultado.place(x=10, y=200)





# ------------ Configurando Frame Esquerda -------------
#Botão Peso/Massa
img_0 = Image.open("Images/weight.png")
img_0 = img_0.resize((45,45), Image.LANCZOS)
img_0 = ImageTk.PhotoImage(img_0)

b_peso = Button(frame_esquerda, command=lambda:mostrar_menu("Massa"), text="Massa", image=img_0, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_peso.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

#Botão Tempo
img_1 = Image.open("Images/time.png")
img_1 = img_1.resize((45,45), Image.LANCZOS)
img_1 = ImageTk.PhotoImage(img_1)

b_tempo = Button(frame_esquerda, command=lambda:mostrar_menu("Tempo"),text="Tempo", image=img_1, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_tempo.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

#Botão Comprimento
img_2 = Image.open("Images/length.png")
img_2 = img_2.resize((45,45), Image.LANCZOS)
img_2 = ImageTk.PhotoImage(img_2)

b_compr = Button(frame_esquerda, command=lambda:mostrar_menu("Comprimento"),text="Comprimento", image=img_2, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_compr.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

#Botão Area
img_3 = Image.open("Images/square.png")
img_3 = img_3.resize((45,45), Image.LANCZOS)
img_3 = ImageTk.PhotoImage(img_3)

b_area = Button(frame_esquerda, text="Área", image=img_3, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_area.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

#Botão Quantidade
img_4 = Image.open("Images/volume.png")
img_4 = img_4.resize((45,45), Image.LANCZOS)
img_4 = ImageTk.PhotoImage(img_4)

b_volume = Button(frame_esquerda, text="Quantidade", image=img_4, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_volume.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

#Botão Velocidade
img_5 = Image.open("Images/speed.png")
img_5 = img_5.resize((45,45), Image.LANCZOS)
img_5 = ImageTk.PhotoImage(img_5)

b_speed = Button(frame_esquerda, text="Velocidade", image=img_5, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_speed.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

#Botão Temperatura
img_6 = Image.open("Images/temperature.png")
img_6 = img_6.resize((45,45), Image.LANCZOS)
img_6 = ImageTk.PhotoImage(img_6)

b_temp = Button(frame_esquerda, text="Temperatura", image=img_6, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_temp.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

#Botão Energia
img_7 = Image.open("Images/energy.png")
img_7 = img_7.resize((45,45), Image.LANCZOS)
img_7 = ImageTk.PhotoImage(img_7)

b_energia = Button(frame_esquerda, text="Energia", image=img_7, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_energia.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

#Botão Pressão
img_8 = Image.open("Images/pressure.png")
img_8 = img_8.resize((45,45), Image.LANCZOS)
img_8 = ImageTk.PhotoImage(img_8)

b_press = Button(frame_esquerda, text="Pressão", image=img_8, compound=LEFT,width=130, height=50, relief="flat", anchor="nw", overrelief="solid", font=("Ivy 10 bold"), bg=cor3, fg=cor2)
b_press.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)


# ------------ Configurando Frame Direita -------------
l_unidade_nome = Label(frame_direita, text="-----", width=16, height=2, padx=0, relief="groove", anchor="center", font=("Ivy 15 bold"), bg=cor2, fg=cor1)
l_unidade_nome.place(x=0, y=0)

l_de = Label(frame_direita, text="De", height=1, padx=3, relief="groove", anchor="center", font=("Ivy 10 bold"), bg=cor2, fg=cor1)
l_de.place(x=10, y=70)
c_de = ttk.Combobox(frame_direita, width=5, justify="center", font=("Ivy 8 bold"))
c_de.place(x=38,y=70)

l_para = Label(frame_direita, text="Para", height=1, padx=3, relief="groove", anchor="center", font=("Ivy 10 bold"), bg=cor2, fg=cor1)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_direita, width=5, justify="center", font=("Ivy 8 bold"))
c_para.place(x=140,y=70)



window.mainloop()