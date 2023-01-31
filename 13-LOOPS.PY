# i = 1
# while i < 6:
#   print(i)
  
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
 
#         continue
#     print(i)

# Note that number 3 is missing in the result


# i = 10
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")



#for Loop
# first print then condition check


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break


# first check condition then print

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


# condition value has been skipper
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)