import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tiger",
    database="college"
)

#creating a cursor in the database

cursor=mydb.cursor()
query = "INSERT INTO employee (name, salary) VALUES (%s, %s)"
values = ("Rahul", 35000)

cursor.execute(query, values)
mydb.commit()

cursor.execute("select * from employee")
for  row in cursor:
    print(row)
cursor.close()
mydb.close()
print(cursor.rowcount, "record inserted.")



