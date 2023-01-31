thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


#Add Sets
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)



thisdict =	{
  "brand": "Ford",
  "year": 1964,
  "model": "Mustang"
  
}
thisdict.popitem()
print(thisdict)
