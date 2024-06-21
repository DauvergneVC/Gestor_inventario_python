import tkinter as tk
# Controllers
from controllers.inventory import getInventory
# Sub windows
from GUI.sub_windows import agregarWindow, editarWindow, eliminarWindows


def mainWindow(user):
    # Crear la ventana
    ventana_dashboard = tk.Tk()
    ventana_dashboard.title("Dashboard")
    ventana_dashboard.geometry("1280x720")

    etiqueta_titulo = tk.Label(ventana_dashboard, text=f"Bienvenido {user}", font=("Arial Bold", 16))
    etiqueta_titulo.pack(pady=20)

    etiqueta_inventario = tk.Label(ventana_dashboard, text="Inventario", font=("Arial Bold", 14))
    etiqueta_inventario.pack(pady=10)  
    
    # Obtener inventario y mostrarlos
    loadInventory(user, ventana_dashboard)

    frame_botones = tk.Frame(ventana_dashboard, bg="lightblue", padx=10, pady=10, relief=tk.RIDGE, bd=2)
    frame_botones.pack(side=tk.RIGHT, anchor=tk.N, padx=20, pady=20)

    boton_eliminar = tk.Button(frame_botones, text="Eliminar Producto", command=lambda:eliminar(user, ventana_dashboard))
    boton_eliminar.pack(pady=5)

    boton_editar = tk.Button(frame_botones, text="Editar Producto", command=lambda:editar(user, ventana_dashboard))
    boton_editar.pack(pady=5)

    boton_agregar = tk.Button(frame_botones, text="Agregar Producto", command=lambda:agregar(user, ventana_dashboard))
    boton_agregar.pack(pady=5)


# Windows and updates
def eliminar(user, ventana_dashboard):
    eliminarWindows(user, ventana_dashboard)

def editar(user, ventana_dashboard):
    editarWindow(user, ventana_dashboard)

def agregar(user, ventana_dashboard):
    agregarWindow(user, ventana_dashboard)


# Inventory helper
def loadInventory(user, ventana_dashboard):
    getInventory(user, ventana_dashboard)