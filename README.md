# Introduction to python
## Python Casting
### Specify a variable type
Casting in python is done using constructor functions like:
* int() -used to construct an integer.
* float() -used to construct a floating point number.
* str() -used to construct a string or character.

## Python Strings
### Single line strings
Single line strings in python are either sorrounded by single or double quotation marks
### Multiline strings
Multiline strings are sorrounded by six single or double quotes
### Strings are Array
Strings in python are arrays of characters.
however python does not have a character data type, so a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the strings.
### Looping a string
You can loop a string of character in python using for loop.
### String Length
You can get the length of a string using the len() function
### Chek String
To check if a certain phrase or character is present in a string, we can use the keyword in.
### Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
## Slicing Strings
### Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
### Slice From the Start
By leaving out the start index, the range will start at the first character
### Slice To the End
By leaving out the end index, the range will go to the end
### Negative Indexing
Use negative indexes to start the slice from the end of the string
## Modify Strings
### Upper Case
The upper() function coverts characters passed to it and convert it to upper case letter.
### Lower Case
The lower() function is used to convert upper case charaters to lower case
### Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
The strip() method removes any whitespace from the beginning or the end.
### Replace String
The replace() method replaces a string with another string.
### Split String
The split() method returns a list where the text between the specified separator becomes the list items.
The split() method splits the string into substrings if it finds instances of the separator
### String Concatenation
To concatenate, or combine, two strings you can use the + operator.
## Format
### String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers.
But we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.
The format() method takes unlimited number of arguments, and are placed into the respective placeholders.
You can use index numbers {0} to be sure the arguments are placed in the correct placeholders.
### Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes.
To fix this problem, use the escape character \"
## Methods
### String Methods
* capitalize()	Converts the first character to upper case
* casefold()	Converts string into lower case
* center()	Returns a centered string
* count()	Returns the number of times a specified value occurs in a string
* encode()	Returns an encoded version of the string
* endswith()	Returns true if the string ends with the specified value
* expandtabs()	Sets the tab size of the string
* find()	Searches the string for a specified value and returns the position of where it was found
* format()	Formats specified values in a string
* format_map()	Formats specified values in a string
* index()	Searches the string for a specified value and returns the position of where it was found
* isalnum()	Returns True if all characters in the string are alphanumeric
* isalpha()	Returns True if all characters in the string are in the alphabet
* isdecimal()	Returns True if all characters in the string are decimals
* isdigit()	Returns True if all characters in the string are digits
* isidentifier()	Returns True if the string is an identifier
* islower()	Returns True if all characters in the string are lower case
* isnumeric()	Returns True if all characters in the string are numeric
* isprintable()	Returns True if all characters in the string are printable
* isspace()	Returns True if all characters in the string are whitespaces
* istitle() 	Returns True if the string follows the rules of a title
* isupper()	Returns True if all characters in the string are upper case
* join()	Joins the elements of an iterable to the end of the string
* ljust()	Returns a left justified version of the string
* lower()	Converts a string into lower case
* lstrip()	Returns a left trim version of the string
* maketrans()	Returns a translation table to be used in translations
* partition()	Returns a tuple where the string is parted into three parts
* replace()	Returns a string where a specified value is replaced with a specified value
* rfind()	Searches the string for a specified value and returns the last position of where it was found
* rindex()	Searches the string for a specified value and returns the last position of where it was found
* rjust()	Returns a right justified version of the string
* rpartition()	Returns a tuple where the string is parted into three parts
* rsplit()	Splits the string at the specified separator, and returns a list
* rstrip()	Returns a right trim version of the string
* split()	Splits the string at the specified separator, and returns a list
* splitlines()	Splits the string at line breaks and returns a list
* startswith()	Returns true if the string starts with the specified value
* strip()	Returns a trimmed version of the string
* swapcase()	Swaps cases, lower case becomes upper case and vice versa
* title()	Converts the first character of each word to upper case
* translate()	Returns a translated string
* upper()	Converts a string into upper case
* zfill()	Fills the string with a specified number of 0 values at the beginning
## Python Booleans
Booleans represent one of two values: True or False.
### Boolean Values
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer.
### Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return
## Operators
Operators are used to perform operations on variables and values.
### Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations.
* (+)   addition
* (-)   subtraction
* (*)   multiplication
* (/) 	Division 	 	
* (%) 	Modulus 	
* (**) 	Exponentiation 		
* (//) 	Floor division
### Assignment Operators
Assignment operators are used to assign values to variables
* = 	x = 5 	x = 5 	
* += 	x += 3 	x = x + 3 	
* -= 	x -= 3 	x = x - 3 	
* *= 	x *= 3 	x = x * 3 	
* /= 	x /= 3 	x = x / 3 	
* %= 	x %= 3 	x = x % 3 	
* //= 	x //= 3 	x = x // 3 	
* **= 	x **= 3 	x = x ** 3 	
* &= 	x &= 3 	x = x & 3 	
* |= 	x |= 3 	x = x | 3 	
* ^= 	x ^= 3 	x = x ^ 3 	
* >>= 	x >>= 3 	x = x >> 3 	
* <<= 	x <<= 3 	x = x << 3
### Comparison Operators

Comparison operators are used to compare two values:
Operator 	Name 	        Example 	
* == 	    Equal 	        x == y 	
* != 	    Not equal 	    x != y 	
* > 	    Greater than 	x > y 	
* < 	    Less than 	    x < y 	
* >= 	    Greater than    x >= y 	
            or equal to
* <= 	    Less than   	x <= y
            or equal to
### Logical Operators
Logical operators are used to combine conditional statements
### Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
## Lists
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data.
### List Length
To determine how many items a list has, use the len() function
### Access List Items
List items are indexed and you can access them by referring to the index number.
