import tkinter as tk
from tkinter import *
import random

root= tk.Tk()
root.geometry("230x100")
root.title("Minca")

def minca():
    if random.randint(1,2) == 1:
        window = Toplevel(root)
        window.title("Nie")
        image = PhotoImage(file="dole.png")

        original_image = Label(window, image=image)
        original_image.image = image
        original_image.pack()

    else:
        window = Toplevel(root)
        window.title("Áno")
        image = PhotoImage(file="hore.png")

        original_image = Label(window, image=image)
        original_image.image = image
        original_image.pack()


tlacidlo = tk.Button(root, text="Hoď", command=minca, activebackground="grey", justify="center", bg="lightgrey")
tlacidlo.pack(pady=40)


root.mainloop()