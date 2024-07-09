import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

# DB config
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def create_connection():
    try:
        cn = mysql.connector.connect(
            host= DB_HOST,
            user= DB_USER,
            password= DB_PASSWORD,
            database= DB_NAME
        )
    except Error as e:
        messagebox.showinfo(f"El error '{e}' ocurrió")

    return cn