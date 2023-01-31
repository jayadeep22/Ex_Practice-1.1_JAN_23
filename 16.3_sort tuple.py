# # Declare a list of tuples
# tuple_list = [("HTML", 15, 'M01'), ("JavaScript", 10, 'M03'), ("Bootstrap", 5, 'M02')]
# # Sort the list based on the first item of the tuple
# sorted_list1 = sorted(tuple_list, key=lambda x: x[0])
# # Print the first sorted list
# print("The sorted list based on the first item:\n", sorted_list1)
# # Sort the list based on the second item of the tuple
# sorted_list2 = sorted(tuple_list, key=lambda x: x[1])
# # Print the second sorted list
# print("The sorted list based on the second item:\n", sorted_list2)
# # Sort the list based on the third item of the tuple
# sorted_list3 = sorted(tuple_list, key=lambda x: x[2])
# # Print the third sorted list
# print("The sorted list based on the third item:\n", sorted_list3)


print("**********************************")
# planets = [("Earth", 3),("Jupiter",5),("Mercury",1), ("Mars",4), ("Neptune",8), ("Saturn", 6), ("Uranus",7), ("Venus",2)]
# print(planets)

# newList = sorted(planets, key = lambda x : x[1],reverse=True)
# print("Reverse sorted list: ",newList)
# print("original list: ", planets)

print("**********************************")
ids = [5, 2, 3, 1, 4]

res = sorted(ids, key=lambda x: x, reverse=True)

print(res)