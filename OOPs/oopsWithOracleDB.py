#program for accepting employee details from kbd and
#save them as record in employee table with class and object
#OopsWithOracleDB.py

import oracledb as orc
class Employee:
    def readempdetails(self):
        self.eno=int(input("Enter Employee No:"))
        self.name=input("Enter Employee Name:")
        self.sal=float(input("Enter Employee Salary:"))
        self.cname=input("Enter Employee Comp Name:")
    def saveempdata(self):
        try:
            con=orc.connect("system/tiger@localhost/orcl")
            cur=con.cursor()
            iq="insert into emp values(%d,'%s',%f,'%s')" %(self.eno,self.name,self.sal,self.cname)
            cur.execute(iq)
            con.commit()
            print("{} record Inserted".format(cur.rowcount))
        except orc.DatabaseError as db:
            print("Probelm in Oracle:",db)

#main program
eo=Employee()
eo.readempdetails()
eo.saveempdata()