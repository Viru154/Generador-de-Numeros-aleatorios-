import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def generar_numeros_aleatorios():
    numeros = [random.randint(-10000000, 10000000) for _ in range(1000000)]
    with open("numeros_aleatorios.txt", "w") as archivo:
        archivo.write("\n".join(map(str, numeros)))
    tk.messagebox.showinfo("Generador de Números", "Números aleatorios generados y guardados en el archivo.")

def ordenar_numeros():
    # Automáticamente busca el archivo de texto
    nombre_archivo = "numeros_aleatorios.txt"

    with open(nombre_archivo, "r") as archivo:
        numeros = archivo.readlines()
        numeros = [int(numero.strip()) for numero in numeros]

    # Ordenar números
    tabla_hash = {}
    for numero in numeros:
        tabla_hash[numero] = numero

    numeros_ordenados = [tabla_hash[numero] for numero in sorted(tabla_hash.keys())]

    # Escribir números ordenados en un nuevo archivo de texto
    nombre_archivo_ordenado = "numeros_ordenados.txt"

    with open(nombre_archivo_ordenado, "w") as archivo_ordenado:
        for numero in numeros_ordenados:
            archivo_ordenado.write(str(numero) + "\n")

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Los números han sido ordenados correctamente.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Números")
ventana.geometry("500x200")
ventana.configure(bg="black")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Generador de Números", font=("Comic Sans MS", 22), bg="black", fg="white")
etiqueta.pack()

# Crear botón para generar números aleatorios
boton_generar = tk.Button(ventana, text="Generar números aleatorios", command=generar_numeros_aleatorios)
boton_generar.pack(pady=20)

# Crear botón para ordenar números
boton_ordenar = tk.Button(ventana, text="Ordenar números", command=ordenar_numeros)
boton_ordenar.pack(pady=10)

ventana.mainloop()
