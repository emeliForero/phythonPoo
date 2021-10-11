import tkinter as tk
from tkinter import * 
from tkinter import ttk
import requests



def cargarData(data):

    for usuario in data['data']:

        datosUsuarios = []
        idUsuario = usuario['id']
        datosUsuarios.append(f"{usuario['name']}")
        datosUsuarios.append(f"{usuario['email']}")
        tabla.insert("",END, text=idUsuario, values=datosUsuarios, tags=('gr',))

    pass

def consumirApi(idPagina):
    
    r = requests.get(f'https://gorest.co.in/public/v1/users?page={idPagina}')

    return r

def traerUsuarios():

    for item in tabla.get_children():
        tabla.delete(item)

    paginaUsuarios = pagina.get()

    if paginaUsuarios == '':
        paginaUsuarios = 1
        pass

    r = consumirApi(paginaUsuarios)
    data = r.json()

    cargarData(data)
    paginaEntrada.delete(0,END)

    pass


ventana = tk.Tk()
ventana.geometry("700x500")
ventana.title("Lista Usuarios")
ventana.resizable(False, False)
ventana.iconbitmap("Interfaces\contacts.ico")
ventana.config(background = "#D4B1F5")

titulo = Label(text="Lista de Usuarios", font=("Cooper Black", 13), bg="#AB9CDE", fg="black", width="450", height="2")
titulo.pack()

paginaLabel = Label(text="Digite la pagina que desea visualisar:", font=("Cooper Black", 10), bg="#D4B1F5")
paginaLabel.place(x=50, y=70)

pagina = StringVar()

paginaEntrada = Entry(textvariable=pagina, font=("Cambria", 10), width="70", bg="#DBC9ED")
paginaEntrada.place(x=50, y=100)

btnRegister = Button(ventana, text="Ingresar", command=traerUsuarios,font=("Cooper Black", 11), width="20", height="2", bg="#AB9CDE")
btnRegister.place(x=250, y=140)

style = ttk.Style(ventana)
style.theme_use("clam")
style.configure("Treeview", background="#DBC9ED", fieldbackground="#DBC9ED", foreground="#000000", font=("Cambria", 10), anchor=CENTER)

tabla = ttk.Treeview(ventana, columns="#0, #1")
tabla.tag_configure('gr', background='#F3F1F7')
tabla.place(x=50, y=220)
tabla.heading("#0", text="Id", anchor=CENTER)
tabla.heading("#1", text="Nombre", anchor=CENTER)
tabla.heading("#2", text="Email", anchor=CENTER)

ventana.mainloop()