import tkinter as tk
from tkinter import messagebox

from controllers.register_controler import registrar
from controllers.login_controller import login

def LoginWindow(cn):
  # Definición de la ventana principal
  ventana = tk.Tk()
  ventana.title("Iniciar Sesión")
  ventana.geometry("1280x720")
  
  # Etiqueta de título
  etiqueta_titulo = tk.Label(ventana, text="Inicia sesión en tu cuenta", font=("Arial Bold", 16))
  etiqueta_titulo.pack(pady=20)
  
  # Etiqueta de instrucciones
  etiqueta_instrucciones = tk.Label(ventana, text="Introduce tus credenciales", font=("Arial", 10))
  etiqueta_instrucciones.pack()
  
  # Etiqueta de usuario
  etiqueta_usuario = tk.Label(ventana, text="Usuario:")
  etiqueta_usuario.pack(pady=5)
  # Entrada de usuario
  entrada_usuario = tk.Entry(ventana)
  entrada_usuario.pack()
  
  # Etiqueta de contraseña
  etiqueta_contrasena = tk.Label(ventana, text="Contraseña:")
  etiqueta_contrasena.pack(pady=5)
  # Entrada de contraseña
  entrada_contrasena = tk.Entry(ventana, show="*")
  entrada_contrasena.pack()
  
  # Botón de inicio de sesión
  boton_inicio_sesion = tk.Button(ventana, text="Iniciar sesion", command=lambda: login(cn, entrada_usuario.get(), entrada_contrasena.get(), ventana))
  boton_inicio_sesion.pack(pady=10)
  
  # Botón de registrarse 
  boton_crear_usuario = tk.Button(ventana, text="Registrase", command=lambda: registrar(cn, entrada_usuario.get(), entrada_contrasena.get()))
  boton_crear_usuario.pack(pady=10)
  
  # Recuperar contraseña
  etiqueta_recuperar_contrasena = tk.Label(ventana, text="En caso de haber olvidado su contraseña, por favor póngase en contacto con el administrador", font=("Arial", 8))
  etiqueta_recuperar_contrasena.pack()
  
  
  ventana.mainloop()
