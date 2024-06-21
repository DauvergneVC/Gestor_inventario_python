from tkinter import messagebox
# Db operations
from database.operations import existeUsuario, registerOperation

def register(user, password):
    
    if existeUsuario(user):
        messagebox.showinfo("Problema", "usuario ya se encuentra registrado en la base de datos")
    else:
        registerOperation(user, password)
        messagebox.showinfo("Registro Existoso", "Usuario registrado correctamente")
