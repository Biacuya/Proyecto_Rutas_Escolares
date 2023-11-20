from tkinter import *
import tkinter as tk

# from home_page import root


def window_address():
    root = tk.Tk()
    ventana = tk.Toplevel(root)

    # Configurar la ventana
    ventana.title("Ventana de ejemplo")

    # Crear un widget Label en la ventana
    etiqueta = tk.Label(ventana, text="¡Hola, esta es una ventana de ejemplo!")
    etiqueta.pack(padx=10, pady=10)
    frame = Frame()
    frame.config(width=250, height=150)
    frame.pack()

    Label(
        frame, text="Ingrese la direccion de la escuela", font=("Comic Sans MS", 15)
    ).place(x=50, y=30)

    Label(
        frame, text="Ingrese su lista de direcciones", font=("Comic Sans MS", 15)
    ).place(x=50, y=10)

    address = Entry(frame)

    address.place(x=45, y=60)

    add = Button(frame, text="Agregar", command="Agregar", activebackground="#FFD8C1")
    add.place(x=85, y=100)

    root.mainloop()
