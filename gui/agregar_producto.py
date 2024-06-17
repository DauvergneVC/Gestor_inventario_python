import tkinter as tk


def AgregarProductoWindow():
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
    
    boton_agregar = tk.Button(ventana_agregar, text="Agregar", command=lambda: print(f"Producto {entrada_nombre.get()} agregado"))
    boton_agregar.pack(pady=10)
