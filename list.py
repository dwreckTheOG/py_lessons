# list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# list length
print(len(thislist))

# Access List Items
print(thislist[2])
print(thislist[-1])

# Range of Indexes
print(thislist[0:2])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

x = len(thislist)
y = x+1
thislist.insert(y, "mango")
print(thislist)

#Append Items
#To add an item to the end of the list, use the append() method
thislist.append("orange")
print(thislist)

#Extend List
#To append elements from another list to the current list, use the extend() method.
tropical = ["tomato", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.

#The del keyword also removes the specified index
del thislist[0]
print(thislist)

#Clear the List
#The clear() method empties the list.
thislist.clear()
print(thislist)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i=i+1

# List Comprehension
#with for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

# With list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 

'''
Sort List Alphanumerically
List objects have a sort() method that will 
sort the list alphanumerically, ascending, by default
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort Descending
thislist.sort(reverse=True)
print(thislist)

#Copy a List
mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

#Join Two Lists
list1 = thislist + mylist
print(list1)

for item in thislist:
  mylist.append(item)

print(mylist)

