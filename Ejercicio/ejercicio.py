import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title("Muestra widgets")

frame1 = tk.Frame(raiz)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = tk.Frame(raiz)
frame2.grid(row=0, column=1, padx=10, pady=10)

frame3 = tk.Frame(raiz)
frame3.grid(row=1, column=0, padx=10, pady=10)

frame4 = tk.Frame(raiz)
frame4.grid(row=1, column=1, padx=10, pady=10)

frame5 = tk.Frame(raiz)
frame5.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

tk.Label(frame1, text="Nombre").grid(row=0, column=0, sticky="w")
tk.Label(frame1, text="Ap. Paterno").grid(row=1, column=0, sticky="w")
tk.Label(frame1, text="Ap. Materno").grid(row=2, column=0, sticky="w")
tk.Label(frame1, text="Correo").grid(row=3, column=0, sticky="w")
tk.Label(frame1, text="Movil").grid(row=4, column=0, sticky="w")

txt_nombre = tk.Entry(frame1)
txt_nombre.grid(row=0, column=1)

txt_ap_paterno = tk.Entry(frame1)
txt_ap_paterno.grid(row=1, column=1)

txt_ap_materno = tk.Entry(frame1)
txt_ap_materno.grid(row=2, column=1)

txt_correo = tk.Entry(frame1)
txt_correo.grid(row=3, column=1)

txt_movil = tk.Entry(frame1)
txt_movil.grid(row=4, column=1)

tk.Label(frame2 ).grid(row=0, column=0, sticky="w")

estado_var = tk.StringVar()

estudiante = tk.Radiobutton(frame2, text="Estudiante", variable=estado_var, value="Estudiante")
estudiante.grid(row=1, column=0, sticky="w")

empleado = tk.Radiobutton(frame2, text="Empleado", variable=estado_var, value="Empleado")
empleado.grid(row=2, column=0, sticky="w")

desempleado = tk.Radiobutton(frame2, text="Desempleado", variable=estado_var, value="Desempleado")
desempleado.grid(row=3, column=0, sticky="w")

tk.Label(frame3, text="Aficiones:").grid(row=0, column=0, sticky="w")

leer_var = tk.BooleanVar()
leer = tk.Checkbutton(frame3, text="Leer", variable=leer_var)
leer.grid(row=1, column=0)

musica_var = tk.BooleanVar()
musica = tk.Checkbutton(frame3, text="Música", variable=musica_var)
musica.grid(row=1, column=1)

videojuegos_var = tk.BooleanVar()
videojuegos = tk.Checkbutton(frame3, text="Videojuegos", variable=videojuegos_var)
videojuegos.grid(row=1, column=2)

tk.Label(frame4, text="Estados:").grid(row=0, column=0, sticky="w")

estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]
estados = ttk.Combobox(frame4, values=estados)
estados.grid(row=1, column=0)

guardar = tk.Button(frame5, text="Guardar", width=10)
guardar.pack(side="left", padx=5)

cancelar = tk.Button(frame5, text="Cancelar", width=10)
cancelar.pack(side="left", padx=5)

raiz.mainloop()
