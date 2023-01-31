print("****************************1*Even******************************************")
nums=[3,2,6,8,4,9,17,21,25,28]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)

print("*********************************2**Odd************************************")
# nums=[3,2,6,8,4,9,17,21,25,28]
# odds=list(filter(lambda n:n%2==1,nums))
# print(odds)

double=list(map(lambda y:y*2,evens))
print(double)

print("*********************************2**map add************************************")
a=[10,20,30,40,50]
def incr(n):
    return n+5
result1=map(incr,a)
print(result1)  
for i in result1:
    print(i)

double1=list(map(lambda y:y+5,double))
print(double1)     


print("****************2**map add************************************")

print("****************3**map add************************************")
double3=double1
res = sorted(double3, key=lambda x: x, reverse=True)

print(res)