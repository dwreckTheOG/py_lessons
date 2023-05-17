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
