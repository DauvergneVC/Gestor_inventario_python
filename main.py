from gui.login import LoginWindow
from database.db_connection import create_connection
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def main():
    # Establecer conexión a la base de datos
    cn = create_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
    # Iniciar la ventana de login
    LoginWindow(cn)

if __name__ == "__main__":
    main()