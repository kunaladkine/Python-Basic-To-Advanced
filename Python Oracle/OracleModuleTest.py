'''#Program for Obraining the connection from Oracle db
#OracleConnTestEx1.py
import oracledb as orc # Step-1
try:
    x=orc.connect("system/tiger@localhost/orcl")#Step-2
    print("Python Program from Got Connection from Oracle Data base")
    print("Type of x=",type(x))
except orc.DatabaseError as db:
    print("Problem in Oracle DB:",db)'''

#program for Creating Table employee in Oracle DB
#OracleTableCreateEx.py
import oracledb as orc #Step-1
def tablecreate():
    try:
        conobj=orc.connect("system/tiger@localhost/orcl") #Step-2
        curobj=conobj.cursor() #Step-3
        #step-4
        ctq="create table student3(sno number(2) primary key, name varchar2(10) not null, marks number(5,2) not null)"
        curobj.execute(ctq)
        print("Table Created in Oracle DB Sucessfully--verify") #Step-5
    except orc.DatabaseError as db:
        print("Probelm in Oracle:",db)

#main Program
tablecreate()