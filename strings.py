# Assign a string to a variable
x = 'hello'
y = "hello"

# Printing Strings
print(x)
print(y)

# Multiline String
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#looping a string of character
for i in x:
    print(i)

s = len(x)
print('the length of the string is '+ str(s))

# Check phrase or character in string
if('magna' in a):
    print('Yes magna is present')

#check if a phrase or character is not in string
if('mom' not in a):
    print('No, "mom" is not present')

# string slicing
q = 'my name is bob juniour'
print('the sliced string is '+ q[2:5])

#slice from the begining
q = 'my name is bob juniour'
print('the sliced string is '+ q[:5])

# slice to the end
q = 'my name is bob juniour'
print('the sliced string is '+ q[2:])

# negative slicing 
q = 'my name is bob juniour'
print('the sliced string is '+ q[-5:-1])#it starts from the end

# upper function
m = 'the president'
print(m.upper())

# lower function
m = 'THE PRESIDENT'
print(m.lower())

# remove white space at the begining or the end of a string
print(m.strip())

# replace string
print(m.replace('THE','YOU'))

# split string
a = "Hello, World!"
print(a.split(","))

# string concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# formating strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)

#Escape character
print("We are the so-called \"Vikings\" from the north.")

# \r 	Carriage Return
txt = "Hello\rWorld!"
print(txt) 

#\t 	Tab
txt = "Hello\tWorld!"
print(txt) 

#\ooo 	Octal value
txt = "\110\145\154\154\157"
print(txt) 

#\xhh 	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#Upper case the first letter in this sentence:
#Syntax
#string.capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x) 

'''Make the string lower case
Syntax
string.casefold()
'''
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x) 

#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
#string.center(length, character)
txt = "banana"
x = txt.center(20)
print(x) 

#Using the letter "O" as the padding character:
txt = "banana"
x = txt.center(20, "O")
print(x) 

#String count() Method
#Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) 

#Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x) 

#String encode() Method
#UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x) 

#Syntax
#string.encode(encoding=encoding, errors=errors)
#These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#String find() Method
#Syntax
#string.find(value, start, end)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) 
