from tkinter import *
from tkinter import ttk
from functools import partial
import random
from tkinter import messagebox
import time

root = Tk()
root.title("matriz aritmetrica")
root.geometry("600x600")
root.config(bg="#FFFFFF") #background - color de fondo - blanco
#messagebox.showinfo(message="Mensaje de prueba", title="prueba")
#Crear una matriz con numeros aleatorios de 3 columas y 3 filas
matriz = [[random.randint(0,11) for x in range(3)] for y in range(5)]
print(matriz)

root.mainloop()





