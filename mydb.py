import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password123'
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS crm_db")
print("Database creation completed")
cursor.close()
conn.close()