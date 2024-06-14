import tkinter as tk
from tkinter import messagebox
# Helpers
from utils.helpers import existeUsuario

# Switch Windows


def login(cn, user, password, window):
    
    if not existeUsuario(cn, user):
        messagebox.showinfo("Problema", "Usuario no se encuentra registrado, registrese antes de continuar")
    
    else:
        cn._open_connection()
        cursor = cn.cursor()
        cursor.execute('SELECT u_contraseña FROM usuarios WHERE u_user = "{0}"'.format(user))

        # Estalecer contraseña correcta desde la base de datps
        correctPassword = cursor.fetchone()
        cn.close()
        messagebox.showinfo("Problema", correctPassword)

        # Comparar contraseñas
        if str(correctPassword[0]) == password:
            window.destroy()  # Cerrar la ventana actual
        else:
            messagebox.showinfo("Problema", "La contraseña no es correcta")