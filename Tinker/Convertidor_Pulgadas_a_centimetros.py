from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana: object
    __pulgadas: object
    __centimetros: object
    def __init__(self):#crea toda la aplicacion
            self.__ventana = Tk()#crea la ventana
            self.__ventana.geometry('290x115')# altura por ancho(tamaño de la ventana)
            self.__ventana.title('Conversor Pulgadas a Centímetros')#titulo de la ventana
            mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")#Frame rectangulo que va estar dentro de la ventana paddiing deja espacio (3 izq 3 derch 12 arriba 12 abajo )
            #ahora todo lo que ponemso adentro va estar en del mainframe
            mainframe.grid(column=0, row=0, sticky=(N, W, E, S))#?
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)
            mainframe['borderwidth'] = 2#ancho de borde de 2 pixeles
            mainframe['relief'] = 'sunken'#le hace sobre salido
            self.__pulgadas = StringVar()#son tipos de datos especiales
            self.__centimetros = StringVar()#son tipos de datos especiales
            self.pulgadasEntry = ttk.Entry(mainframe, width=7, textvariable=self.__pulgadas)#para ingresar las pulgadas
            self.pulgadasEntry.grid(column=2, row=1, sticky=(W, E))
            ttk.Label(mainframe, textvariable=self.__centimetros).grid(column=2, row=2, sticky=(W, E))
            ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=W)#boton calcular
            ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3,sticky=W)#boton salir
            ttk.Label(mainframe, text="pulgadas").grid(column=3, row=1, sticky=W)
            ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
            ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=W)
            for child in mainframe.winfo_children():
                child.grid_configure(padx=5, pady=5)#espacio entre cada uno de los objetos que estan en la ventana
                self.pulgadasEntry.focus()#Asociado al valor de pulgadas, .focus() es
                self.__ventana.mainloop()#loop de la ventana
    def calcular(self):#metodo calcular se ejecuta cuando se toca el boton calcular
        try:
            valor=float(self.pulgadasEntry.get())#valor de el valor que ingreso el usuario porque es un strigvar()
            self.__centimetros.set(2.54*valor)
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')#
            self.__pulgadas.set('')#lo pone en blanco al cuadrito
            self.pulgadasEntry.focus()#permite poner el cursor en el frame
def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()