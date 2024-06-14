import tkinter as tk
from tkinter import messagebox

# Helpers
from utils.helpers import existeUsuario


def registrar(cn, user, password):
    
    messagebox.showinfo("Problema", user)
    
    if existeUsuario(cn, user):
        messagebox.showinfo("Problema", "correo ya se encuentra registrado en la base de datos")
    else:
        cn._open_connection()
        cursor = cn.cursor()

        cursor.execute('INSERT INTO usuarios (u_correo, u_contraseña) VALUES (%s,%s)',(user,password))
        
        cn.commit() 
        messagebox.showinfo("Registro Existoso", "Usuario registrado correctamente :DDD")
        cn.close()
