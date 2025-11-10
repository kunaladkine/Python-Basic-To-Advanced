class Factorial:
    def getval(self):
        self.n=int(input("Enter a Number for cal Factorial:"))
    def calfact(self):
        if(self.n<0):
            return ("\t{} is Invalid Input".format(self.n))
        else:
            fact=1
            for i in range(1,self.n+1):
                fact=fact*i
            return ("\t{} is {}".format(self.n,fact))
    def dispresult(self,result):
        print(res)


#main program
fo=Factorial()
fo.getval()
res=fo.calfact()
fo.dispresult(res)