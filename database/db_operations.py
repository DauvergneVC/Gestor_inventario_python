from db_connection import create_connection

cn = create_connection()

def add_item(cn, item):
    cn._open_connection()
    cursor = cn.cursor()
    
    arrayDatos = []
    while (True):
        datos = []
        datos.append(input('Ingrese el nombre del objeto: '))
        datos.append(input('Ingrese la marca del objeto: '))
        datos.append(int(input('Ingrese la cantidad del objeto: ')))
        
        arrayDatos.append(tuple(datos)) 
        datos.clear()
        
        pregunta = input('¿Desea añadir mas elementos? (Y/N)')
        if  str(pregunta).upper()=='N':
            break
    
    cursor.executemany('INSERT INTO inventario (i_nombre, i_marca, i_cantidad) VALUES(%s,%s,%s',arrayDatos)
    cn.commit()    
    
    arrayDatos.clear()
    print('Datos ingresados')
    cn.close()


def read_items(cn):
    query = 'SELECT * FROM population'
    
    cn._open_connection()
    cursor=cn.cursor()
    
    cursor.execute(query)
    
    items = []  
    for fila in cn.fetchall():
        items.append(list(fila))

    cn.close()
    return items


def del_item(cn,item_id):
    cn._open_connection()
    cursor=cn.cursor()
    query= "DELETE FROM inventory WHERE id = %s"
    cursor.execute(query, (item_id,))
    cn.commit()
    print(f"El Producto de ID {item_id} sido eliminado con exito")
    cn.close()

