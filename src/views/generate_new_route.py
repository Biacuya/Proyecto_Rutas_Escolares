from tkinter import *
import tkinter as tk


def generate_address():
    root = Tk()

    info_address = Frame()
    info_address.config(width="200", height="400")
    info_address.config(bd="2")
    info_address.config(relief="flat")
    info_address.pack(side="left")
    Label(text="Direcciones agregadas", font=("Comic Sans MS", 15)).place(x=20, y=20)

    form_generate_new_route = Frame()
    form_generate_new_route.config(width="400", height="400")
    form_generate_new_route.pack(side="right")


# root.mainloop()
