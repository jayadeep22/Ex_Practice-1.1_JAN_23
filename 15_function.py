def sample():
    print("hello.")


sample()


# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# def argumentsDemo(fname,lname):
#     print(fname,lname)

# argumentsDemo("ram","dao")


# def argumentsDemo(fname):
#     print(fname)

# argumentsDemo("patil","ram")



#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.


#Arbitrary Arguments, *args
def person(name,*data):
    print(name)
    print(data)

person("jay",20,"mumbai",2023)





# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def person(name,**data):
    print(name)
    print(data)

person("jay",age=20,city="mumbai",year=2023)





# Default Parameter Value
# The following example shows how to use a default parameter value.
def my_function(country = "Enter Correct Country"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function()




# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)







def add(num1,num2):
   x=num1
   y=num2
   result=x+y;
   print(result)

add(num1=10,num2=25)


# Return Values
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))




def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)


sum(5,6,34,38)    


def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1=add_sub(10,4)
result2=add_sub(15,5)
print(result1,result2)

print("****************************************************************************")

y=20
def add(y):
    x=10;
   
    c=x+y
    print(c)

add(30)