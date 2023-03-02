#App para convertir pies a metros usando Tkinter
#Crhistopher Isram Mancilla Laure
#23 de Febrero del 2023

from tkinter import* #Esta es una forma de importar paquetes de Python 
from tkinter import ttk 

class Conversor:

    #Tipo constructor de la clase
    def __init__(self, raiz): #Self es el predeterminado, raiz es de tkinter
        raiz.title("Pies a metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0) 

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies) #Caja de texto
        piesEntry.grid(column=1, row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a:").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2) #Botón

        #Hacer la operación presionando <Enter>
        raiz.bind("<Return>", self.calcular)
    
    def calcular(self, *args): #Método del botón
        print("Botón presionar")
        piesUsuario = self.pies.get() #Siempre devuelve una cadena
        print("Pies ingresados: ", piesUsuario)
        piesFlotante = float(piesUsuario) #Conversión de cadena a flotante
        metros = piesFlotante * 0.3048
        print("Metros: ", metros)
        self.metros.set(metros)
       

if __name__=="__main__":
    print("Este es el archivo principal")
    print("Nada más se mostrará esto si es el principal")
