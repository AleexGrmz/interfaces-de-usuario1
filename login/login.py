#login

from tkinter import* #es un paquete en python
from tkinter import ttk

class login:

    def __init__(self , raiz):
        raiz.title(" Inicio de sesion ")    

        self.usuario = StringVar()
        self.contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding="12 12 12 12") 
        mainFrame.grid(column=0, row=0)

        ttk.Label(mainFrame, text=" Usuario ").grid(column=1, row=0 )
        ttk.Label(mainFrame, text=" Contraseña ").grid(column=1, row=2)

        ttk.Label(mainFrame, text=" ").grid(column=1, row=1)
        ttk.Label(mainFrame, text=" ").grid(column=2, row=1)    

        usuarioEntry = ttk.Entry(mainFrame, width=20, textvariable=self.usuario).grid(column=2, row=0) 
        contraEntry = ttk.Entry(mainFrame, width=20, textvariable=self.contraseña).grid(column=2, row=2)

        ttk.Label(mainFrame, text=" ").grid(column=2, row=3) 
        ttk.Button(mainFrame, text="Ingresar" ).grid(column=2, row=4, sticky= E)