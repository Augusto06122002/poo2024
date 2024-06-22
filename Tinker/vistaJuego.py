from tkinter import *
import tkinter as tk
import random

class Aplicacion:
    def __init__(self):
        ventana=Tk()
        ventana.title("probando canvas")
        canvas=tk.Canvas(ventana, width=200, height=300)
        canvas.pack()
        label=Label(canvas, text="Puntaje:")
        label.place(x=3, y=0)
#-----------Botones-----------
        self.__botones=[] #esta lista facilitaria de random con los botones
        self.__listaBotonesClickeados=[] #esta lista almacena los botones que se eligen de manera random

        botonRojo=Button(canvas, bg='red', width=10, height=6)
        canvas.create_window(60,80,window=botonRojo)
        self.__botones.append(botonRojo)
        botonRojo.bind("<Button-1>", lambda event: self.clickeo(event)) #esta linea captura el evento de click y lo manda como parametro a la funcion clickeo

        botonAzul=Button(canvas, bg='skyblue', width=10, height=6)
        canvas.create_window(150,80,window=botonAzul)
        self.__botones.append(botonAzul)
        botonAzul.bind("<Button-1>", lambda event: self.clickeo(event))

        botonAmarillo=Button(canvas, bg='yellow', width=10, height=6)
        canvas.create_window(60,190,window=botonAmarillo)
        self.__botones.append(botonAmarillo)
        botonAmarillo.bind("<Button-1>", lambda event: self.clickeo(event))

        botonVerde=Button(canvas, bg='green', width=10, height=6)
        canvas.create_window(150,190,window=botonVerde)
        self.__botones.append(botonVerde)
        botonVerde.bind("<Button-1>", lambda event: self.clickeo(event))

        botonSTART=Button(canvas, text="START", command=lambda: self.IteracionJuego())
        canvas.create_window(150,270, window=botonSTART)
        botonSalir=Button(canvas, text="SALIR", command=ventana.destroy)
        canvas.create_window(100,270, window=botonSalir)
        ventana.mainloop()
#----------Almacena botones presionados por usuario---------
    def clickeo(self, event):
        boton=event.widget
        self.__listaBotonesClickeados.append(boton)
        print(self.__listaBotonesClickeados)
        return (boton)
#-----------------------------------------------------

    def IteracionJuego(self):
        i=0
        band=False
        botRandom=self.eleccion_botonRandom()

        # while i<len(self.__botones) and band is False:
        #     if botRandom==self.clickeo:
        #         print("correcto")
        #         band=True
        #     botRandom=self.eleccion_botonRandom()



#tengo pensado hacer una comparacion entre 2 listas, utlizando especificamente los colores elegidos


    def eleccion_botonRandom(self):#prueba para cambiar de color un boton al clickear
        boton=random.choice(self.__botones)
        auxColor=boton.cget('bg')
        print (auxColor)
        boton.config(bg='white') #esto le cambia el color al boton random, para que luego el usuario presione ese boton
        boton.after(1000, lambda: self.restaurarColor(boton, auxColor)) #luego de que haya cambiado de color, despues de 2 segundos vuelve a su color original

    def restaurarColor(self, boton, auxColor):
        boton.config(bg=auxColor)
            
#creo que tiene que ser un while, que tenga el tamanio de la listaBotonesCLickeados, ya que asi, se va a ir incrementando a medida que el usuario va acertando botones.
if __name__=='__main__':
    miApp=Aplicacion()