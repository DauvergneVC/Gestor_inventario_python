def getInventario(cn, user):
    inventario = []
    
    cn._open_connection()
    cursor = cn.cursor()
    cursor.execute('SELECT i_id, i_nombre, i_marca, i_cantidad FROM inventario WHERE u_id = (select u_id from usuarios where u_user ="{0}")'.format(user))

    # agregar items a Array
    for item in cursor.fetchall():
        inventario.append(list(item))

    cn.close()
    return inventario
    