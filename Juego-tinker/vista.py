
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from ClaseJugador import jugador
import random
class VistaSimon:
    __ventana:object
    __puntaje:int
    __jugador:jugador
    __secuencia:list
    __entrada_secuencia:list
    
    def __init__(self, ventana):
        self.__ventana = tk.Tk()
        self.__ventana.title("PySimon-Game")
        self.puntaje = 0
        self.secuencia = []
        self.entrada_secuencia = []
        self.jugador = None
        self.botones=[]
        self.cargarInterfaz()
    
class SimonGame:
    def __init__(self, master):
        self.__ventana = master
        self.__ventana.title("Simon Game")
        self.canvas = tk.Canvas(self.__ventana, width=400, height=400)
        self.canvas.pack()
        self.secuencia = []
        self.input_secuencia = []
        self.botones = {}
        self.puntaje = 0
        self.cargarPuntajes()
        self.cargarInterfaz()

    def cargarInterfaz(self):
        self.nombre_entry = tk.Entry(self.__ventana)
        self.nombre_entry.pack()
        self.boton_rojo = self.crearBoton("#ff0000", 100, 100)
        self.boton_verde = self.crearBoton("#00ff00", 100, 200)
        self.boton_azul = self.crearBoton("#0000ff", 200, 100)
        self.boton_amarillo = self.crearBoton("#ffff00", 200, 200)

        self.iniciar_button = tk.Button(self.__ventana, text="Iniciar Juego", command=self.iniciarJuego)
        self.iniciar_button.pack()

    def crearBoton(self, color, x, y):
        boton = self.canvas.create_rectangle(x, y, x+100, y+100, fill=color, outline="")
        self.canvas.tag_bind(boton, '<Button-1>', lambda event, c=color: self.gestionarEvento(c))
        self.botones[color] = boton
        return boton

    def iniciarJuego(self):
        nombre = self.nombre_entry.get()
        if nombre:
            fecha = datetime.now()
            self.jugador = jugador(nombre, fecha)
            self.secuencia = []
            self.secuencia_jugador = []
            self.puntaje = 0
            self.generarSecuencia()
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre")

    def generarSecuencia(self):
        color = random.choice(list(self.botones.keys()))
        self.colores.append(color)
        self.mostrarSecuencia()

    def mostrarSecuencia(self):
        for color in self.colores:
            self.canvas.after(1000, lambda color=color: self.cambiarColorBoton(color))
            self.canvas.after(1500, lambda color=color: self.revertirColorBoton(color))

    def cambiarColorBoton(self, color):
        self.canvas.itemconfig(self.botones[color], fill="white")

    def revertirColorBoton(self, color):
        self.canvas.itemconfig(self.botones[color], fill=color)

    def gestionarEvento(self, color):
        self.secuencia_jugador.append(color)
        if len(self.input_secuencia) == len(self.colores):
            self.verificarSecuencia()

    def verificarSecuencia(self):
        if self.secuencia_jugador == self.colores:
            self.puntaje += 1
            self.secuencia_jugador = []
            self.generarSecuencia()
        else:
            self.finJuego()

    def finJuego(self):
        self.jugador.puntaje = self.puntaje
        self.gestorJugadores.agregarJugador(self.jugador)
        self.guardarPuntajes()
        self.mostrarPuntajes()
        self.iniciarJuego()
