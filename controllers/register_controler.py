from tkinter import messagebox
# Helpers
from utils.helpers import existeUsuario


def registrar(cn, user, password):
    
    if existeUsuario(cn, user):
        messagebox.showinfo("Problema", "usuario ya se encuentra registrado en la base de datos")
    else:
        cn._open_connection()
        cursor = cn.cursor()

        cursor.execute('INSERT INTO usuarios (u_user, u_contraseña) VALUES (%s,%s)',(user,password))
        
        cn.commit() 
        messagebox.showinfo("Registro Existoso", "Usuario registrado correctamente")
        cn.close()
