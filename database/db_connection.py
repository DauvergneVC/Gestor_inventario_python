import mysql.connector
from mysql.connector import Error

def create_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME):
    try:
        cn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='VHHmWDiJ',
            database='gestor_inventario'
        )
        print("Conexión a MySQL exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")

    return cn