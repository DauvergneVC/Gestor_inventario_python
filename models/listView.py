import tkinter as tk
from tkinter import ttk

# Global
lista = None

    
# Funciones para cargar y vaciar datos
def cargar_datos(lista, items):
    for fila in list(items):
        lista.insert("", tk.END, values=fila)
        
def vaciar_lista(lista):
        lista.delete(*lista.get_children())


def listView(window, items):
    global lista  # Acceso a la variable global

    # Verificar si el widget Treeview existe
    if lista is None:
        # Si no existe, crearlo
        lista = ttk.Treeview(window, show="headings", columns=("Columna 1", "Columna 2", "Columna 3", "Columna 4"))
        lista.heading("Columna 1", text="Id producto")
        lista.heading("Columna 2", text="Nombre producto")
        lista.heading("Columna 3", text="Marca producto")
        lista.heading("Columna 4", text="Cantidad producto")
        lista.pack()
    
    vaciar_lista(lista)
    
    cargar_datos(lista, items)
    