def existeUsuario(cn, user):
    
    cn._open_connection()
    cursor = cn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM usuarios WHERE u_correo = "{0}"'.format(user))
    
    users = cursor.fetchone()[0]
    
    cn.close()
    
    if users > 0:
        return True
    else:
        return False