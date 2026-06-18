import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",               
        password="mysql@8971494596",   # <--- Put your actual MySQL password here
        database="medical_db",
        cursorclass=pymysql.cursors.DictCursor
    )