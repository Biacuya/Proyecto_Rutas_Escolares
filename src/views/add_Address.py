from tkinter import *
import tkinter as tk

root = Tk()

root.title("Agregar direccion")
root.resizable(False,False)
frame = Frame()
frame.config(width=250, height=150)
frame.pack()

Label(frame, text="Ingrese la direccion", font=("Comic Sans MS", 15)).place(x=50, y=30)

address = Entry(frame)

address.place(x=45, y=60)

add = Button(frame, text="Agregar", command="Agregar", activebackground="#FFD8C1")
add.place(x=85, y=100)

root.mainloop()