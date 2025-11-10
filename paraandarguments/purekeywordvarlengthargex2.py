#program for demonstrating the need of keyword variable length arguments
#thiss program will execute as it is

def dispinfo(**kvr):
    if(len(kvr)!=0):
        for k,v in kvr.items():
            print("\t{}-->{}".format(k,v))
    else:
        print("Not Finding any Keyword Variable Length args")
    print("---------------------------------------------------")
#main program
dispinfo(eno=10,ename="RS",sal=88.44,dsg="Author")
dispinfo(tno=20,tname="KV",sub1="Java",sub2="Python",expe=28)
dispinfo(cno=30,cname="Kv",hb1="Eating",hb2="Sleeping",hb3="Chatting")
dispinfo(a=50,b=60)