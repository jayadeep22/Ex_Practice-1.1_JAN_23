print("hello")
print('hello')

a = "Hello"
print(a)


#Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Slicing String

b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5])
#Slice To the End
b = "Hello, World!"
print(b[2:])


#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#Upper Case
a = "Hello, World!"
print(a.upper())
#Lower Case
a = "Hello, World!"
print(a.lower())


#Remove Whitespace
a = "           Hello,      World!         f         "
print(a.strip()) # returns "Hello, World!"


#Replace String#

a = "Hello, World!"
print(a.replace("o", "l"))


#Split String
a = "Hello_ World!"
print(a.split("_")) # returns ['Hello', ' World!']


#String Concatenation

a = "Hello"
b = "5"
c = a + b
print(c)


#String Format
age = 36
txt = "My name {} is John, and I am "
print(txt.format(age))

#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)