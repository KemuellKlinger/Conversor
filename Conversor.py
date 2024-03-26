#----Interface grafica
# pip install tk

#----Outros componetes
#1 - pip install SpeechRecognition
#2 - pip install pipwin
#3 - pipwin install pyaudio

#----Somente caso realmente não funcione
#4 - pip install setuptools

import speech_recognition as sr
from tkinter import *
import os

class Conversor:
    def __init__(self):
        self.mostrar = False
        self.audio = ''
        self.label_saida = Label
        self.JanelaPrincipal()
        
    def JanelaPrincipal(self):
        self.janela = Tk()
        x = self.janela.winfo_screenwidth() // 2 - 350 // 2
        y = self.janela.winfo_screenheight() // 2 - 350 // 2
        self.janela.geometry('{}x{}+{}+{}'.format(350, 350, x, y))
        self.janela.resizable(False,False)

        #----DIVIDAO DA JANELA EM 03 FRAMES

        frame_01 = Frame(self.janela, width=350, height=60, bg="grey")
        frame_01.grid(row=0, column=0)

        frame_02 = Frame(self.janela, width=350, height=60, bg="grey")
        frame_02.grid(row=1, column=0)

        frame_03 = Frame(self.janela, width=350, height=230, bg="grey")
        frame_03.grid(row=2, column=0)

        #----DADOS

        titulo = Label(frame_01, text="Conversor de Audio em Texto", font=('Ivy 13 bold'), bg="grey")
        titulo.place(x=0,y=5)

        informativo = Label(frame_01, text="↓ Clique na imagem para começar ↓", font=('Ivy 10 bold'), bg="grey")
        informativo.place(x=55,y=40)

        img_btn = PhotoImage(file = "imgBotao.png") 

        self.botao_falar = Button(frame_02, image=img_btn, width=100, height=70, command=lambda:self.ouvir())
        self.botao_falar.place(x=125,y=0)

        self.trancricao = LabelFrame(frame_03, text="transcrição", bg="darkgrey", width=300, height=200)
        self.trancricao.place(x=25,y=15)

        self.label_saida = Label(self.trancricao, bg="darkgrey")
        self.label_saida.place(x=25,y=15)

        self.janela.mainloop()

    def exluir(self):   
        if self.mostrar == True:
            self.labelErro.destroy()
        else:
            self.mostrar = False

    def ouvir(self):
    
        self.exluir()

        #----Inicializar o reconhecedor
        self.microfone = sr.Recognizer()

        #----Capturar áudio do microfone e guarda na variavel
        try:
            with sr.Microphone() as source:
                # self.microfone.adjust_for_ambient_noise(source)
                self.audio = self.microfone.listen(source)

        except BaseException as erro:
            self.labelErro = Label(self.trancricao, text=f"Erro: {erro}", 
                            font=('Ivy 10 bold'),  bg="darkgrey", anchor=W, justify=LEFT, wraplength=250)
            self.labelErro.place(x=25,y=15)
            
        #----Tentar transcrever o áudio em texto
        try:
            if self.audio:
                falaConvertida = self.microfone.recognize_google(self.audio, language="pt-BR")
                texto = StringVar()
                texto.set(str(falaConvertida))
            else:
                print("Sem audio para transcrever")

            if self.label_saida:
                self.label_saida.destroy()
                self.label_saida = Label(self.trancricao, textvariable=texto, bg="darkgrey", 
                            font=('Ivy 10 bold'), anchor=W, justify=LEFT, wraplength=250)
                self.label_saida.place(x=25,y=15)

        except sr.UnknownValueError:
            self.mostrar  = True

            self.labelErro = Label(self.trancricao, text="Não foi possível entender o áudio", 
                            font=('Ivy 10 bold'),  bg="darkgrey", anchor=W, justify=LEFT, wraplength=250)
            self.labelErro.place(x=25,y=15)
            
        except sr.RequestError as e:
            self.mostrar  = True

            erro = f"Erro ao solicitar resultados da API de reconhecimento de fala; {e}"
            self.labelErro = Label(self.trancricao, text=erro,  bg="darkgrey",
                            font=('Ivy 10 bold'), anchor=W, justify=LEFT, wraplength=250)
            self.labelErro.place(x=25,y=15)

if __name__ == "__main__":        
    app = Conversor()

    