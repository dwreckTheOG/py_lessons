# addition
x = 5
y = 3
print(x + y)

# subtraction
x = 5
y = 3
print(x - y)

# Multiplication
x = 5
y = 3
print(x * y)

# Division
x = 5
y = 3
print(x / y)

# Modulus
x = 5
y = 3
print(x % y)
# Exponentiation
x = 5
y = 3
print(x ** y)

# Floor division
#the floor division // rounds the result down to the nearest whole number
x = 15
y = 2
print(x // y)

# Comparison Operators
x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x < y)

x = 5
y = 3
print(x >= y)

x = 5
y = 3
print(x <= y)

# Logical Operators
x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

# Identity Operators
# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Membership Operators
# in
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

# not in
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
