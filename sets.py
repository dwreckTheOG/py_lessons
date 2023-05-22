# Example
thisset = {"apple", "banana", "cherry"}

#Get the Length of a Set
print(len(thisset))

#Access Set Items
for i in thisset:
    print(i)

#adding items to a set
thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

#Remove Set Items
#remove()
thisset.remove("banana")
print(thisset) 

#discard()
thisset.discard("apple")
print(thisset) 

#clear()
thisset.clear()
print(thisset) 

# del
thisset = {"apple", "banana", "cherry"}
#del thisset
print(thisset) 

# loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

#Join Sets
#union()
set1  = {'mary','anne','jane'}
set2 = {'john','mike','luke'}
set3 = set1.union(set2)
print(set3)

# update()
set1  = {'mary','anne','jane'}
set2 = {'john','mike','luke'}
set1.update(set2)
print(set1)

#Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 

#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Set add() Method
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
