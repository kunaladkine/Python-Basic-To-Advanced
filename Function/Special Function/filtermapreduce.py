#accept the list of salaries ranges from 0 to 1000
#obtain the salaries ranges from 0 to 500 from given slalist and give 5& hike
#obtain the salaries ranges from 501 to 1000 from mgiven sallist and give 10% hike
#find total saalary before and after hike whose sal ranges from 0 to 500
#find total saalary before and after hike whose saal ranges fro, 501 to 1000
#find total salary before and after hike whose sal ranges from 501 to 1000

import functools
oldsal=[float(sal) for sal in input("Enter Salary Between 0 to 1000:").split(",") if 0<float(sal)<=1000]
print("Given Sal List is :",oldsal)

sal0_500=list(filter(lambda sal:sal in range(0,501),oldsal))
hikesal0_500=list(map(lambda sal:sal+sal*5/100,sal0_500))
totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500)
tothikesal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal0_500)
print("_"*50)
print("\t\tSalary0-500\t\tHike Salary0-500")
print("="*50)
for old,new in zip(sal0_500,hikesal0_500):
    print("\t\t{}\t\t\t\t{}".format(old,new))
print("_"*50)
print("\t\t{}\t\t\t\t{}".format(totsal0_500,tothikesal0_500))


sal501_1000=list(filter(lambda sal:sal in range(501,10001),oldsal))
hikesal501_1000=list(map(lambda sal:sal+sal*10/100,sal501_1000))
totsal501_1001=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
totsalhike501_1001=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal501_1000)
print("="*50)
print("\t\tSalary501-1000\t\tHike Salary601_1000")
print("="*50)
for old,new in zip(sal501_1000,hikesal501_1000):
    print("\t\t{}\t\t\t\t{}".format(old,new))
print("_"*50)
print("\t\t{}\t\t\t\t{}".format(totsal501_1001,totsalhike501_1001))
print("="*50)
print("\t\t{}\t\t\t\t{}".format(totsal0_500+totsal501_1001,round(tothikesal0_500+tothikesal0_500,2)))
print("="*50)