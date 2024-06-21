import tkinter as tk
# Controller
from controllers.inventory import addItem, delItem, edItem

def agregarWindow(user, ventana_dashboard):
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Producto")
    ventana_agregar.geometry("500x300")
    
    etiqueta_titulo = tk.Label(ventana_agregar, text="Agregar Producto", font=("Arial Bold", 12))
    etiqueta_titulo.pack(pady=10)
    
    etiqueta_nombre = tk.Label(ventana_agregar, text="Nombre del producto:")
    etiqueta_nombre.pack(pady=5)
    
    entrada_nombre = tk.Entry(ventana_agregar)
    entrada_nombre.pack(pady=5)
    
    etiqueta_marca = tk.Label(ventana_agregar, text="Marca del producto:")
    etiqueta_marca.pack(pady=5)
    
    entrada_marca = tk.Entry(ventana_agregar)
    entrada_marca.pack(pady=5)
    
    etiqueta_cantidad = tk.Label(ventana_agregar, text="Cantidad:")
    etiqueta_cantidad.pack(pady=5)
    
    entrada_cantidad = tk.Entry(ventana_agregar)
    entrada_cantidad.pack(pady=5)
    
    boton_agregar = tk.Button(ventana_agregar, text="Agregar", command=lambda: addItem(user, entrada_nombre.get(), entrada_marca.get(), entrada_cantidad.get(), ventana_dashboard) )
    boton_agregar.pack(pady=10)


def eliminarWindows(user, ventana_dashboard):
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Producto")
    ventana_eliminar.geometry("500x300")
    
    etiqueta_titulo = tk.Label(ventana_eliminar, text="Eliminar Producto", font=("Arial Bold", 12))
    etiqueta_titulo.pack(pady=10)
    
    etiqueta_id = tk.Label(ventana_eliminar, text="ID del producto:")
    etiqueta_id.pack(pady=5)
    
    entrada_id = tk.Entry(ventana_eliminar)
    entrada_id.pack(pady=5)
    
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=lambda:delItem( entrada_id.get(), user, ventana_dashboard) )
    boton_eliminar.pack(pady=10)
    

def editarWindow(user, ventana_dashboard):
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Producto")
    ventana_editar.geometry("500x400")
    
    etiqueta_titulo = tk.Label(ventana_editar, text="Editar Producto", font=("Arial Bold", 12))
    etiqueta_titulo.pack(pady=10)
    
    etiqueta_id = tk.Label(ventana_editar, text="ID del producto:")
    etiqueta_id.pack(pady=5)
    
    entrada_id = tk.Entry(ventana_editar)
    entrada_id.pack(pady=5)
    
    etiqueta_nombre = tk.Label(ventana_editar, text="Nuevo nombre:")
    etiqueta_nombre.pack(pady=5)
    
    entrada_nombre = tk.Entry(ventana_editar)
    entrada_nombre.pack(pady=5)
    
    etiqueta_marca = tk.Label(ventana_editar, text="Nueva marca:")
    etiqueta_marca.pack(pady=5)
    
    entrada_marca = tk.Entry(ventana_editar)
    entrada_marca.pack(pady=5)
    
    etiqueta_cantidad = tk.Label(ventana_editar, text="Nueva cantidad:")
    etiqueta_cantidad.pack(pady=5)
    
    entrada_cantidad = tk.Entry(ventana_editar)
    entrada_cantidad.pack(pady=5)
    
    boton_editar = tk.Button(ventana_editar, text="Editar", command=lambda: edItem(entrada_id.get(), entrada_nombre.get(), entrada_marca.get(), entrada_cantidad.get(), user, ventana_dashboard))
    boton_editar.pack(pady=10)
    