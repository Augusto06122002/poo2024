from tkinter import *
import tkinter as tk
from tkinter import messagebox

class VentanaInicio:
    def __init__(self):
        self.__inicio=Tk()
        self.canvas_inicio = tk.Canvas(self.__inicio, width=300, height=200)
        self.canvas_inicio.pack()

        label_nombre = Label(self.canvas_inicio, text="Ingrese su nombre:")
        self.canvas_inicio.create_window(150, 50, window=label_nombre)

        self.entry_nombre = Entry(self.canvas_inicio)
        self.canvas_inicio.create_window(150, 80, window=self.entry_nombre)

        boton_iniciar = Button(self.canvas_inicio, text="Iniciar Juego", command=self.iniciarJuego)
        self.canvas_inicio.create_window(150, 120, window=boton_iniciar)
        self.__inicio.mainloop()
    def iniciarJuego(self):
        self.__nombre_jugador = self.entry_nombre.get().strip()
        if not self.__nombre_jugador:
            messagebox.showwarning("Advertencia", "Por favor, ingrese su nombre.")
            return
        
        self.__inicio.destroy()
    def getNomb(self):
        return self.__nombre_jugador