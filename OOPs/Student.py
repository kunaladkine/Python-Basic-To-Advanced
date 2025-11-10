class Student:
    def setstudent(self,sno,sname,marks):
        self.sno=sno
        self.name=sname
        self.marks=marks
    def getstuddet(self):
        print("{}\t{}\t{}".format(self.sno,self.name,self.marks))