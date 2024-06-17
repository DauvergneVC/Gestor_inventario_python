import tkinter as tk

# Controlers
from controllers.inventory_controller import getInventario


def DashboarWindow(cn, usuario):
  #Crear la  ventana
  ventana_dashboard =tk.Tk()
  ventana_dashboard.title("Dashboard")
  ventana_dashboard.geometry("1280x720")

  etiqueta_titulo=tk.Label(ventana_dashboard, text=f"Bienvenido {usuario}",font=("Arial Bold",16))
  etiqueta_titulo.pack(pady=20)

  etiqueta_inventario = tk.Label(ventana_dashboard, text="Inventario", font=("Arial Bold", 14))
  etiqueta_inventario.pack(pady=10)

    # Obtener inventario y mostrarlos
  inventario = getInventario(cn, usuario)
  for item in inventario:
    etiqueta_item = tk.Label(ventana_dashboard, text=item)
    etiqueta_item.pack()
    
  frame_botones = tk.Frame(ventana_dashboard, bg="lightblue", padx=10, pady=10, relief=tk.RIDGE, bd=2)
  frame_botones.pack(side=tk.RIGHT, anchor=tk.N, padx=20, pady=20)
  boton_eliminar = tk.Button(frame_botones, text="Eliminar Producto",command=EliminarProductoWindow)
  boton_eliminar.pack(pady=5)
  boton_editar = tk.Button(frame_botones, text="Editar Producto",command=EditarProductoWindow)
  boton_editar.pack(pady=5)
  boton_agregar = tk.Button(frame_botones, text="Agregar Producto",command=AgregarProductoWindow)
  boton_agregar.pack(pady=5)

  ventana_dashboard.mainloop()
  
def EliminarProductoWindow():
  return""
def AgregarProductoWindow():
  return ""
def EditarProductoWindow():
  return ""