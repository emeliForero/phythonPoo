import tkinter as tk
from tkinter import * 


def printText():
    
    changeText.set(firstInput.get())
    firstInput.delete(0, tk.END)

    pass

master = tk.Tk()

changeText = StringVar()

master.title("Git Hub Page")
master.resizable(False, False)
master.iconbitmap("Interfaces\github.ico")

firstFrame = Frame(master, width=400, height=350)
firstFrame.pack()

firstLabel = Label(firstFrame, textvariable=changeText, font=("Comic Sans MS", 16), fg="purple" ).grid(row=1, column=2, padx=20, pady=20)

firstInput = Entry(firstFrame)
firstInput.grid(row=3, column=2, padx=20, pady=20)

secondLabel = Label(firstFrame, text="Print:", font=(11)).grid(row=3, column=1, padx=20, pady=20)

firstButton = Button(master, text="Imprimir", command=printText).pack(pady=20)

master.mainloop()


