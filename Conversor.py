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

        mainFrame = ttk.Frame(raiz, padding = "10 10 10 10") #Padding(Izquierda, arriba, derecha, abajo)
        mainFrame.grid(column=0, row=0) 

        piesEntry = ttk.Entry(mainFrame, width=7, textvariable=self.pies) #Caja de texto
        piesEntry.grid(column=1, row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0, sticky=(W, E, N, S))
        #W lo pega a la izquierda, E a la derecha, N arriba y la S abajo
        ttk.Label(mainFrame, text="Son equivalentes a:", padding=(5, 10, 5, 10)).grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2) #Botón

        piesEntry.focus() #Esto hace que en cuando entremos a la ventana ya estemos listos para escribir
        #Hacer la operación presionando <Enter>
        raiz.bind("<Return>", self.calcular)
    
    def calcular(self, *args): #Método del botón
        print("Botón presionar")
        piesUsuario = self.pies.get() #Siempre devuelve una cadena
        print("Pies ingresados: ", piesUsuario)
        try:       
            piesFlotante = float(piesUsuario) #Conversión de cadena a flotante
            metros = piesFlotante * 0.3048
            print("Metros: ", metros)
            self.metros.set(metros)
            #self.pies.set("") #Método para limpiar el Entry después de Calcular
        except:
            print("No es un dato válido.")    
       

if __name__=="__main__":
    print("Este es el archivo principal")
    print("Nada más se mostrará esto si es el principal")
