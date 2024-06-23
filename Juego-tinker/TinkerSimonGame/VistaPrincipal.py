from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from VistaInicio import VentanaInicio
class JuegoSimon(VentanaInicio):
    def __init__(self):
        super().__init__()
        self.__NombreJugador = self.getNomb() 
        self.__puntaje = 0
       
        self.__listaSecuenciaRandom = []
    
       
        self.root = tk.Tk()
        self.root.title("Simon-Game")
        self.canvas = tk.Canvas(self.root, width=200, height=300)
        self.canvas.pack()
        
        self.label_puntaje = Label(self.canvas, text="{}: {}".format(self.__NombreJugador,self.__puntaje),font='Arial 10')
        self.label_puntaje.place(x=3, y=0)
    
        # Lista de botones
        self.__botones = []
        
        botonRojo = Button(self.canvas, bg='red', width=10, height=6)
        self.canvas.create_window(60, 80, window=botonRojo)
        self.__botones.append(botonRojo)
        botonRojo.bind("<Button-1>", lambda event: self.secuenciaJugador(event))#lambda captura el evento

        botonAzul = Button(self.canvas, bg='blue', width=10, height=6)
        self.canvas.create_window(150, 80, window=botonAzul)
        self.__botones.append(botonAzul)
        botonAzul.bind("<Button-1>", lambda event: self.secuenciaJugador(event))

        botonAmarillo = Button(self.canvas, bg='yellow', width=10, height=6)
        self.canvas.create_window(60, 190, window=botonAmarillo)
        self.__botones.append(botonAmarillo)
        botonAmarillo.bind("<Button-1>", lambda event: self.secuenciaJugador(event))

        botonVerde = Button(self.canvas, bg='green', width=10, height=6)
        self.canvas.create_window(150, 190, window=botonVerde)
        self.__botones.append(botonVerde)
        botonVerde.bind("<Button-1>", lambda event: self.secuenciaJugador(event))

        botonSTART = Button(self.canvas, text="START", command=lambda: self.ComienzaJuego())
        self.canvas.create_window(150, 270, window=botonSTART)
        
        botonSalir = Button(self.canvas, text="SALIR", command=lambda: self.Salir())
        self.canvas.create_window(100, 270, window=botonSalir)
        
        self.root.mainloop()
    def setControlador(self, controlador):
        self.controlador = controlador
        
    def ComienzaJuego(self):
        self.controlador.agregarJugador()
        self.secuenciaAleatoria()
        
    def secuenciaAleatoria(self):
        self.__secuenciaJugador=[]
        boton = random.choice(self.__botones)
        color = boton.cget('bg')
        self.__listaSecuenciaRandom.append(color)
    
        for indice,color in enumerate(self.__listaSecuenciaRandom):#toma indice y valor de la lista
            boton = self.obtenerBotonPorColor(color)
            self.canvas.after(indice*1000, lambda b=boton,c=color: self.cambiarColorBoton(b, c))#Dato comprender bien como sirve lambda
    def obtenerBotonPorColor(self, color):
        band=False
        i=0
        pos=0
        while i<len(self.__botones) and not band:
            if self.__botones[i].cget('bg') == color:
                pos=i
                band=True
            else:
                i+=1
        return self.__botones[pos]
    def cambiarColorBoton(self, boton, color):
        boton.config(bg='white')
        boton.after(800, lambda: self.restaurarColor(boton, color))
    
    def restaurarColor(self, boton, color):
        boton.config(bg=color)
    
    def secuenciaJugador(self, event):
        boton_presionado = event.widget
        color_presionado = boton_presionado.cget('bg')
        self.__secuenciaJugador.append(color_presionado)
        coincideColor = True
        i=0
        while (i < len(self.__secuenciaJugador) and coincideColor):
            if self.__secuenciaJugador[i] !=self.__listaSecuenciaRandom[i]:
                coincideColor = False
            else:
                i+=1
        
        if coincideColor:
            if len(self.__secuenciaJugador) == len(self.__listaSecuenciaRandom):#Comprueba que la secuencia de botones(1,2,3) tenga la misma cantidad que la que se genero
                self.__puntaje+=1
                self.MuestraPuntajes()
                self.secuenciaAleatoria()
        else:#Aca deberia ir la ventana que diga GameOver
            self.__listaSecuenciaRandom=[]
            self.__secuenciaJugador=[]
            self.gameOver()
    
    def MuestraPuntajes(self):
        self.label_puntaje.config(text="{}: {}".format(self.__NombreJugador,self.__puntaje),font='Arial 10') 
        
        
    def gameOver(self):
        self.controlador.ActualizaPuntuacion_GameOver(self.__puntaje)
        messagebox.showinfo("GAME OVER", "Puntaje obtenido: {}".format(self.__puntaje))
        self.__listaSecuenciaRandom = []
        self.__secuenciaJugador = []
        self.__puntaje = 0
    def Salir(self):
        self.controlador.guardarPuntajes()
        self.root.destroy

if __name__=='__main__':
    app=JuegoSimon()