a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])

#String Length
a = "Hello, World!"
print(len(a))

#String Methods
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))
print(a.split("o"))

#Check String
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
y = "ain" not in txt
print(x)
print(y)

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
age =36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."