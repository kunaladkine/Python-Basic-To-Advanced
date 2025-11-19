import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tiger",
    database="college"
)

print("connection done succesfully !")
