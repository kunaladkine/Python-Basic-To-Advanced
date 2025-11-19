import mysql.connector as mc
conobj=mc.connect(host="localhost",user="system",passwd="tiger")
print("Python Program Got Connection from MySQL")