import mysql.connector

def get_db_connection():
    db= mysql.connector.connect(
        host="DB_HOST",
        port=3306,
        user="DB_USER",
        password="DB_PASSWORD",
        database="DB_NAME"
    )

    return db