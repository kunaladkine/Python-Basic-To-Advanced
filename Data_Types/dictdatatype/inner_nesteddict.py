# innterornested dict 16 Combination
# Dict in Dict          #List in List   #set in set     #tuple in tuple
#List in Dict           #Dict in list   #list in set    #set in tuple
#Set in Dict            #set in list    #dict in set    #list in tuple
#tuple in Dict          #tuple in list  #tuple in set   #dict in tuple


print("-"*50)
#dict in dict
d={"sno":100,"name":"RS","mem":{"CM":20,"C++":18},"em":{"CM":70,"C++":80},"ColName":"OU"}
print(d,type(d),id(d))

for k,v in d.items():
    print(k,"-->",v,"-->",type(v),"-->",type(d))

print(d["mem"])

print(d.get("mem"))

for k,v in d["mem"].items():
    print(k,"-->",v)

for k in d.get("em"):
    print(k,d.get("em")[k])

d["mem"]["CM"]=10       #value is updated
print(d.get("mem"))

d.popitem()     #removes the last element from the dict
print(d)
print("-"*50)
#list in dict

d1={"sno":10,"name":"RS","me":[20,30,40],"em":[80,90,40],"cname":"OU"}
print(d1)
print(d1.get("me").append(22))
print(["em"].insert(1,22))
del d1.get("em")[1:]            #removes of values 1 index forward
print(d1)

print("-"*50)
#tuple in dict

d3={"sno":10,"name":"RS","me":(20,18,25),"em":(80,67,78),"cname":"OU"}
print(d3)
for k, v in d.items():
    print(k,"-->",v)

print(d3.get("em")[1:])
print(d3["me"][::2])
print(d3.get("me").count(108))
print(sorted(d3["me"]))
print(d3["em"])
print(d3)
d3["em"]=tuple(sorted(d.get("em"))[::-1])
print(d3)
print("-"*50)

#set in dict ----Possible
dict1={"sno":10,"name":"RS","me":{20,18,25},"em":{80,67,78},"cname":"OU"}
print(dict1)
for k,v in dict1.items():
    print(k,"--->",v)