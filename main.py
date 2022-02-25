from tkinter import *
from pytube import YouTube

def downYt():
    app = Tk()
    app.title("YouTube Downloader")
    app.geometry("400x250")

    fontePadrao = ('Segoe UI', '12')
    infVidFont = ('Arial', '10')
        
    Label(app, text="Link do Vídeo:", font=fontePadrao).place(x=15, y=10)
    linkVid = Entry(app, width=40, font=fontePadrao)
    linkVid.place(x=17, y=35)

    def downloadYt(link):
        diretorio = 'videos/'

        yt = YouTube(link)

        segundos = yt.length
        minutos = segundos//60
        resto = segundos%60
        min,rst = str(minutos), str(resto)
        tamanho = min+":"+rst
        titulo = yt.title
        views = yt.views

        titulo = "Título: " + str(titulo)
        tamanho = "Duração: " + str(tamanho)
        views = "Visualizações: " + str(views)

        Label(app, text=titulo, font=infVidFont).place(x=15, y=65)
        Label(app, text=tamanho, font=infVidFont).place(x=15, y=85)
        Label(app, text=views, font=infVidFont).place(x=15, y=105)

        ys = yt.streams.get_highest_resolution()
        ys.download(diretorio)

    Button(app, text="Baixar", font=fontePadrao, width=20, command=lambda: downloadYt(linkVid.get())).place(x=191, y=170)
    app.mainloop()

downYt()