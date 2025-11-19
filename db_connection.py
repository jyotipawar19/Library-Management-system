import mysql.connector

def connect():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="root",    
            database="library_management"
        )
        return con
    except mysql.connector.Error as e:
        print("Database Connection Error:", e)
        return None
