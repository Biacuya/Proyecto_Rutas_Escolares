import tkinter as tk
from tkinter import *
from tkinter import ttk
from add_Address import window_address
from generate_new_route import generate_address


root = tk.Tk()

root.title("Proyecto_Rutas_Escolares")

root.resizable(False, False)

top = Frame(root, width="900", height="100")

top.pack(side="top")

imagen = tk.PhotoImage(file="School-bus.png")

Label(top, image=imagen).place(x=0, y=0)

Label(top, text="Optimizacion de rutas escolares", font=("Comic Sans MS", 20)).place(
    x=190, y=40
)

generate_new_rout = tk.Button(
    top,
    text="Generar nueva ruta",
    command=generate_address,
    activebackground="#FFD8C1",
)

generate_new_rout.place(x=600, y=45)

add_address = Button(
    top,
    text="Agregar direccion",
    command=window_address,
    activebackground="#FFD8C1",
)


add_address.place(x=750, y=45)

left = Frame()

left.pack(side="left")

left.config(width="184", height="500")

left.config(bg="blue")

center = Frame()

center.pack(anchor="center")
center.config(width="716", height="500")
center.config(bg="red")

root.mainloop()
