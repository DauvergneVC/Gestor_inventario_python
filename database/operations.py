from database.connection import create_connection

cn = create_connection()


# Items operation
def modify(id, newName, newBrand, newAmount):
    cn._open_connection()
    cursor = cn.cursor()
    
    query = """
    UPDATE INVENTARIO SET i_nombre = %s, i_marca = %s, i_cantidad = %s
    WHERE i_id = %s"""
    data = (newName, newBrand, newAmount, id)
    
    cursor.execute(query, data)
    cn.commit()
    
    cn.close()


def add(id, name, brand, amount):
    cn._open_connection()
    cursor = cn.cursor()
    
    insert_query = """
    INSERT INTO INVENTARIO (u_id, i_nombre, i_marca, i_cantidad) VALUES (%s, %s, %s, %s)"""
    data = (id, name, brand, amount)
    
    cursor.execute(insert_query, data)
    cn.commit()
    
    print('Datos ingresados')
    
    cn.close()


def delete(item_id):
    cn._open_connection()
    cursor=cn.cursor()
    
    cursor.execute("DELETE FROM INVENTARIO WHERE i_id = {0}".format(item_id))
    
    cn.commit()
    cn.close()


def obtenerInventario(user):
    inventario = []
    
    cn._open_connection()
    cursor = cn.cursor()
    
    cursor.execute('SELECT i_id, i_nombre, i_marca, i_cantidad FROM INVENTARIO WHERE u_id = (select u_id from USUARIOS where u_user ="{0}")'.format(user))

    # agregar items a Array
    for item in cursor.fetchall():
        inventario.append(list(item))

    cn.close()
    return inventario


# Login operation
def loginRelization(user, password):
    cn._open_connection()
    cursor = cn.cursor()
    
    cursor.execute('SELECT u_contraseña FROM USUARIOS WHERE u_user = "{0}"'.format(user))
    # Estalecer contraseña correcta desde la base de datps
    correctPassword = cursor.fetchone()
    cn.close()
    # Comparar contraseñas
    if str(correctPassword[0]) == password:
        return True
    else:
        return False

# Register operation
def registerOperation(user, password):
    cn._open_connection()
    cursor = cn.cursor()
    
    cursor.execute('INSERT INTO USUARIOS (u_user, u_contraseña) VALUES (%s,%s)',(user,password))
    cn.commit() 
    
    cn.close()
        
        
# Helpers operation
def existeUsuario(user):
    cn._open_connection()
    cursor = cn.cursor()
    cursor.execute('SELECT COUNT(*) FROM USUARIOS WHERE u_user = "{0}"'.format(user))
    
    users = cursor.fetchone()[0]
    
    cn.close()
    
    if users > 0:
        return True
    else:
        return False
    
def existeProducto(id):
    cn._open_connection()
    cursor = cn.cursor()
    cursor.execute('SELECT COUNT(*) FROM INVENTARIO WHERE i_id = "{0}"'.format(id))
    
    items = cursor.fetchone()[0]
    
    cn.close()
    
    if items > 0:
        return True
    else:
        return False
    
def obtenerIdPersona(user):
    id = ""
    
    cn._open_connection()
    cursor = cn.cursor()
    
    cursor.execute('SELECT u_id FROM USUARIOS WHERE u_user = "{0}"'.format(str(user)))
    
    id = cursor.fetchone()[0]
    
    cn.close()
    return id
    