mult=lambda x:x*2

print(mult(5))




add=lambda x,y:x+y

print(add(5,55))


print("******************")
def myfunc(n):
  return lambda a : a * n



a = myfunc(2)

print(a(11))



print("*****************")

from functools import reduce
multiply=lambda x,y: x*y
print(multiply(2,3))

print("**************************************************1")

power=lambda x,y: x**y
print(power(2,3))
print("**********************2****************************")


#map and lambda function
some_num=[2,4,6,8]
some_num1=[3,5,7,9]
doublenum=map(lambda x,y:x+y,some_num,some_num1)
print(doublenum)
print(list(doublenum))



string=["my","python"]
cap=map(lambda x:str.upper(x),string)
print(list(cap))

print("****************3**********************************")



#filter

attendence=[36,25,75,14,2,65]

abv_avg_att=filter(lambda x:x<=35,attendence)
print(list(abv_avg_att))


country=["india","uk","us","France","UAE"]
count_cg3=filter(lambda x:len(x)>=3,country)
print(list(count_cg3))



print("****************4**********************************")
db=[4,12,16,8]

red=reduce(lambda a,b:a+b,db)
print(red)

print("****************5**********************************")
a=[10,20,30,40,50]
result=reduce(lambda n,m:n+m,a)
print(result)