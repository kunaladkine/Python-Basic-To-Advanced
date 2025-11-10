#Probelem Statemenet Solving by Set Function wit Ven Diagrams
#Given
#--------------
# Set of Cricket Player={ "Kolhi", "Rohit", "Travis" }
# Set of Tennis Players={"Rohit", "Rossum", "Travis"}

#q1. find the player names who are playing all the games .

cp={"Kolhi","Rohit","Gil"}
tp={"Rohit","Rossum","Travis"}
print(cp,type(cp),id(cp))
print(tp,type(tp),id(tp))
bothcptp=cp.union(tp)
print(bothcptp)
#or using Bitwise we get same
#it is not using the set data type

bothcptp=cp|tp
print(bothcptp)

#Q2. Find the player name wwho palying both cricket and tennis

bothcptp=cp.intersection(tp)
print(bothcptp)

#bitwise AND ( & )

bothcptp=cp&tp
print(bothcptp)

#Q3 Find the player names who are playing cricket but not tennis
bothcptp=tp.difference(cp)
print(bothcptp)

bothcptp=cp-tp         #arithmetic operator for difference is minus ( -)
print(bothcptp)

#Q4. Find the player names who are playing tennis but not cricket -- arithmetic minus (-)

onlytp=tp.difference(cp)
print(onlytp)

onlytp=tp-cp            #using the arithmetic minus operator
print(onlytp)

#Q5. Find the player names who are EXCUSIBVELY Playing Cricket and Tennis. symmetric_difference()

exclcptp=cp.symmetric_difference(tp)
print(exclcptp)

exclcptp=cp^tp      #bitwise XOR ( ^ )
print(exclcptp)