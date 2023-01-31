thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple (String)
thistuple = ("apple")
print(type(thistuple))


#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = list(("apple", "banana", "cherry"))
print(thistuple)
print(type(thistuple))

sample=tuple(thistuple)
print(sample)
print(type(sample))

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,




# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)