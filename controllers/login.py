from tkinter import messagebox
# Db operations
from database.operations import loginRelization, existeUsuario
# New window
from GUI.main_window import mainWindow


def login(user, password, window):
    
    if not existeUsuario(user):
        messagebox.showinfo("Problema", "Usuario no se encuentra registrado, registrese antes de continuar")
    
    else:
        if loginRelization(user, password):
            window.destroy()  # Cerrar la ventana actual
            mainWindow(user)
            
        else:
            messagebox.showinfo("Problema", "La contraseña no es correcta")
