import tkinter as tk
from tkinter import messagebox
# Models
from models.listView import listView
# Db operations
from database.operations import obtenerInventario,delete, obtenerIdPersona, add, modify, existeProducto


def getInventory(window, user):
    inventory = obtenerInventario(user)
    listView(window, inventory)
    
    
    
def addItem(user, name, brand, amount, ventana_dashboard):
    id = obtenerIdPersona(user)
    add(id, name, brand, amount)
    
    getInventory(ventana_dashboard, user)
    messagebox.showinfo("Exito", "Producto agregado con exito")

def delItem(id, user, ventana_dashboard):
    if not existeProducto(id):
        messagebox.showinfo("Problema", "No existe item con la id seleccionada")
    else:
        delete(id)
        
        getInventory(ventana_dashboard, user)
        messagebox.showinfo("Exito", "El producto con la id: '{0}' ha sido eliminado".format(id))


def edItem(id, newName, newBrand, newAmount, user, ventana_dashboard):
    if not existeProducto(id):
        messagebox.showinfo("Problema", "No existe item con la id seleccionada")
    else:
        modify(id, newName, newBrand, newAmount)
        
        getInventory(ventana_dashboard, user)
        messagebox.showinfo("Exito", "El producto con la id: '{0}' ha sido modificado".format(id))