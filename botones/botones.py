from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button (raiz, text="Boton solo texto")
boton.grid()

imagen = PhotoImage(file="11.png")

btnImagen = ttk.Button ( raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button (raiz, text="Boton Combinado", compound="bottom")
btnCombinada.grid()
btnCombinada ['1mage'] = imagen

chkBoton = ttk.Checkbutton (raiz, text="Opcion 1")
chkBoton.grid()
raiz.mainloop ()