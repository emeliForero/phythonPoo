from datetime import date
from datetime import datetime
import tkinter as tk
from tkinter import * 
from tkinter import ttk



def enviarUsuario():

    contactos = []
    dia = date.today()
    tiempo = datetime.now()

    nombreUsuario = nombre.get()
    contactos.append(f'{dia.strftime("%b-%d-%Y")}')
    contactos.append(f'{tiempo.strftime("%H:%M:%S")}')

    tabla.insert("",END, text=nombreUsuario, values=contactos, tags=('gr',))

    nombreEntrada.delete(0,END)

    pass

ventana = tk.Tk()
ventana.geometry("700x500")
ventana.title("Ingreso Usuarios")
ventana.resizable(False, False)
ventana.iconbitmap("Interfaces\icono.ico")
ventana.config(background = "#FFCCCC")

titulo = Label(text="Formulario de Ingreso Usuarios", font=("Cooper Black", 13), bg="#FFB6C1", fg="black", width="450", height="2")
titulo.pack()

nombreLabel = Label(text="Nombre:", font=("Cooper Black", 10), bg="#FFCCCC")
nombreLabel.place(x=50, y=70)

nombre = StringVar()

nombreEntrada = Entry(textvariable=nombre, font=("Cambria", 10), width="70", bg="#FFE4E1")
nombreEntrada.place(x=50, y=100)

btnRegister = Button(ventana, text="Ingresar", command=enviarUsuario,font=("Cooper Black", 11), width="20", height="2", bg="#FFB6C1")
btnRegister.place(x=250, y=140)

style = ttk.Style(ventana)
style.theme_use("clam")
style.configure("Treeview", background="#FFE4E1", fieldbackground="#FFE4E1", foreground="#FFE4E1")

tabla = ttk.Treeview(ventana, columns="#0, #1")
tabla.tag_configure('gr', background='#FFB6C1')
tabla.place(x=50, y=220)
tabla.heading("#0", text="Nombre", anchor=CENTER)
tabla.heading("#1", text="Fecha", anchor=CENTER)
tabla.heading("#2", text="Hora", anchor=CENTER)

ventana.mainloop()