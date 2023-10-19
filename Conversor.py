#----Interface grafica
# pip install tk

#----Outros componetes
#1 - pip install SpeechRecognition
#2 - pip install pipwin
#3 - pipwin install pyaudio

import speech_recognition as sr
from tkinter import *

janela = Tk()
x = janela.winfo_screenwidth() // 2 - 350 // 2
y = janela.winfo_screenheight() // 2 - 350 // 2
janela.geometry('{}x{}+{}+{}'.format(350, 350, x, y))
janela.resizable(False,False)

#----DIVIDAO DA JANELA EM 03 FRAMES

frame_01 = Frame(janela, width=350, height=60, bg="grey")
frame_01.grid(row=0, column=0)

frame_02 = Frame(janela, width=350, height=60, bg="grey")
frame_02.grid(row=1, column=0)

frame_03 = Frame(janela, width=350, height=230, bg="grey")
frame_03.grid(row=2, column=0)

#----DADOS

titulo = Label(frame_01, text="Conversor de Audio em Texto", font=('Ivy 13 bold'), bg="grey")
titulo.place(x=0,y=5)

informativo = Label(frame_01, text="↓ Clique na imagem para começar ↓", font=('Ivy 10 bold'), bg="grey")
informativo.place(x=55,y=40)

img_btn = PhotoImage(file = "./imgBotao.png") 

botao_falar = Button(frame_02, image=img_btn,width=100, height=70, command=lambda:ouvir())
botao_falar.place(x=125,y=0)

trancricao = LabelFrame(frame_03, text="transcrição", bg="darkgrey", width=300, height=200)
trancricao.place(x=25,y=15)

label_saida = Label(trancricao, bg="darkgrey")
label_saida.place(x=25,y=15)

mostrar = False

def exluir():
    global mostrar, labelErro
   
    if mostrar == True:
        labelErro.destroy()
    else:
        mostrar = False

def ouvir():
    global mostrar, labelErro, label_saida
  
    exluir()

    label_saida.destroy()

    #----Inicializar o reconhecedor
    microfone = sr.Recognizer()

    #----Capturar áudio do microfone e guarda na variavel
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        audio = microfone.listen(source)
        
    #----Tentar transcrever o áudio em texto
    try:
        falaConvertida = microfone.recognize_google(audio, language="pt-BR")
        
        texto = StringVar()
        texto.set(str(falaConvertida))
        
        label_saida = Label(trancricao, textvariable=texto, bg="darkgrey", 
                      font=('Ivy 10 bold'), anchor=W, justify=LEFT, wraplength=250)
        label_saida.place(x=25,y=15)

    except sr.UnknownValueError:
        mostrar  = True

        labelErro = Label(trancricao, text="Não foi possível entender o áudio", 
                          font=('Ivy 10 bold'),  bg="darkgrey", anchor=W, justify=LEFT, wraplength=250)
        labelErro.place(x=25,y=15)
        
    except sr.RequestError as e:
        mostrar  = True

        erro = f"Erro ao solicitar resultados da API de reconhecimento de fala; {e}"
        labelErro = Label(trancricao, text=erro,  bg="darkgrey",
                          font=('Ivy 10 bold'), anchor=W, justify=LEFT, wraplength=250)
        labelErro.place(x=25,y=15)

janela.mainloop()


