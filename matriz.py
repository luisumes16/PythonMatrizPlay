#Esta es una nueva actualizacion
from tkinter import*
from tkinter import ttk
from functools import partial
import random
from tkinter import messagebox
import time


#Vaoy a probar algo nuevo
#Crear una ventana en tkinter
root = Tk()
root.title('TKINTER GAME')
root.geometry("600x500")
root.config(bg="#FFFFFF")

filas = 8
columnas = 8


#Crear una matriz con numeros aleatorios de 3 columnas y 3 filas
matriz = [[random.randint(0,11) for x in range(columnas)] for y in range(filas)]
#label = Label(root, text = "Hola mundo " )
#label.grid(row = 1, column = 0)
#label.config(bg = "#070D0F")

#crear una matriz vacia
anulados=[]

def nuevo_click(i, j):
    sumatoria = 0
    print(str(i) + " " + str(j))
    if [i, j] in anulados:
        print('Existe en la matriz')
        messagebox.showinfo(message="No puedes seleccionar este numero", title="Incorrecto")
    else:
        
    
        btnLista[i][j].config(bg = "#FFFFFF", relief = "solid", fg = "red")
        
        if i +1 >= filas:
            print("No se puede abajo")
        else:
            print(columnas)
            print(j)
            btnLista[i+1][j].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es AC" + str(matriz[i+1][j]))
            sumatoria = sumatoria + matriz[i+1][j]
            print("LA SUMATORIA ES " + str(sumatoria))
            if j+1 >= columnas:
                print("No se puede abajo derecha")
            else:  
                btnLista[i+1][j+1].config(bg = "#FFFFFF", relief = "solid", fg = "blue") 
                print("El numero es AD" + str(matriz[i+1][j+1]))
                sumatoria = sumatoria + matriz[i+1][j+1]
                print("LA SUMATORIA ES " + str(sumatoria))
            
            if j-1 < 0:
                print("No se puede abajo izquierda")
            else: 
                btnLista[i+1][j-1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
                print("El numero es AI" + str(matriz[i+1][j-1]))
                sumatoria = sumatoria + matriz[i+1][j-1]
                print("LA SUMATORIA ES " + str(sumatoria))
        
        if i -1 <= 0:
            print("No se puede arriba")
        else:
            print(filas)
            print(i)
            btnLista[i-1][j].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es " + str(matriz[i-1][j]))
            sumatoria = sumatoria + matriz[i-1][j]
            print("LA SUMATORIA ES " + str(sumatoria))
            if j+1 >= columnas:
                print("No se puede arriba derecha")
            else:  
                btnLista[i-1][j+1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
                print("El numero es " + str(matriz[i-1][j+1]))
                sumatoria = sumatoria + matriz[i-1][j+1]
                print("LA SUMATORIA ES " + str(sumatoria))
            
            if j-1 < 0:
                print("No se puede arriba izquierda")
            else: 
                btnLista[i-1][j-1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
                print("El numero es " + str(matriz[i-1][j-1]))
                sumatoria = sumatoria + matriz[i-1][j-1]
                print("LA SUMATORIA ES " + str(sumatoria))
                
        
                
        if j <= 0:
            print("No se puede a la izquierda")      
        else:
            btnLista[i][j-1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es izquierda" + str(matriz[i][j-1]))
            sumatoria = sumatoria + matriz[i][j-1]
            print("LA SUMATORIA ES " + str(sumatoria))
        
        print(columnas )
        print(j)
        if j+1 >= columnas:
            print("No se puede a la derecha")
        else:
            btnLista[i][j+1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es derecha" + str(matriz[i][j+1]))
            sumatoria = sumatoria + matriz[i][j+1]
            print("LA SUMATORIA ES " + str(sumatoria))

        print("CONSULTAS")
        
        print(anulados)
        print("LA SUMATORIA ES " + str(sumatoria))
        
        anulados.append([i,j])
        
        print(anulados)

        
        inicio = time.time()
        print(inicio)
        respuesta = input('Ingresa la respuesta \n')
        final = time.time()
        tiempo = round(final-inicio, 0)
        print(respuesta)
        print("Te has tardado " + str(tiempo))
    
    
    
    


    
    
     
    
    #btnLista[i-1][j].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
    
    
        
    

#Crear un boton que diga, seleccion

    
    
    
    
    
    
    


print(matriz)


btnLista= []

def generarMatriz():
    posicionX =.2
    posicionY = .2
    for i in range(filas):
        btnLista.append([])
        for j in range(columnas):
            #Crear un label en la matriz
            #label2 = Label(root, text=matriz[i][j], font=("Arial", 20, "bold"), bg="#070D0F", fg="white")
            #label2.grid(row = i, column = j)
            #label2.place(relx=posicionX, rely=posicionY)
            #label2.config(bg = "#070D0F")
            
            btnLista[i].append(Button(root, text = matriz[i][j], command=partial(nuevo_click, i,j) ))
            btnLista[i][j].config(bg = "#FFFFFF", relief = "solid", fg = "white")
            btnLista[i][j].place(relx = 0.1 *j, rely = 0.1 + 0.1*i, relwidth = 0.1, relheight = 0.1)
            
            posicionX+=0.1
        posicionY+=0.1
        posicionX = .2

generarMatriz()
    
    
    

boton = ttk.Button(text="Creacion", command=generarMatriz)
boton.place(x=5, y=5)



root.mainloop()