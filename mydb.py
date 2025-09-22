import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password123'
)

conn.execute("create database crm_db")
print("Execution completed")