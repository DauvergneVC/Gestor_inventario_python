class LoginController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def authenticate(self, username, password):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        return user is not None