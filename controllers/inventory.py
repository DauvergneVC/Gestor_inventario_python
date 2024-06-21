import tkinter as tk
from tkinter import messagebox
# Db operations
from database.operations import obtenerInventario,delete, obtenerIdPersona, add, modify


def getInventory(user, ventana_dashboard):
    etiqueta_item = tk.Label(ventana_dashboard, text="")
    etiqueta_item.pack()
    
    inventory = obtenerInventario(user)
    
    if inventory == "":
        etiqueta_item = tk.Label(ventana_dashboard, text="No hay inventario guardado")
    
    else:
        for item in inventory:
            etiqueta_item = tk.Label(ventana_dashboard, text=item)
            etiqueta_item.pack()
    
    
    
def addItem(user, name, brand, amount, ventana_dashboard):
    id = obtenerIdPersona(user)
    add(id, name, brand, amount)
    getInventory(user, ventana_dashboard)
    messagebox.showinfo("Exito", "Producto agregado con exito")

def delItem(id, user, ventana_dashboard):
    delete(id)
    getInventory(user, ventana_dashboard)
    messagebox.showinfo("Exito", "El producto con la id: '{0}' ha sido eliminado".format(id))


def edItem(id, newName, newBrand, newAmount, user, ventana_dashboard):
    modify(id, newName, newBrand, newAmount)
    getInventory(user, ventana_dashboard)
    messagebox.showinfo("Exito", "El producto con la id: '{0}' ha sido modificado".format(id))