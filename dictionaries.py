#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# dict length
print(len(thisdict))

#accessing items in dict
x = thisdict['model']
print(x)

#using get() method
x = thisdict.get('brand')
print(x)

#getting key in a dict
x = thisdict.keys()
print(x)

# get values in a dict
x = thisdict.values()
print(x)

# getting items from a dict
x = thisdict.items()
print(x)

#change values
thisdict['year'] = 2020
print(thisdict['year'])

thisdict.update({'model': 'saloon'})
print(thisdict)

# adding items
thisdict['color'] = 'red'
print(thisdict)

# reoming items
thisdict.pop('color')
print(thisdict)

# looping a dict
for i in thisdict:
    print(i,'\t' ,thisdict[i])

# loop for values only
for x in thisdict.values():
    print(x)

#loop for keys only
for x in thisdict.keys():
    print(x)

# loop for both keys and valuees
for x,y in thisdict.items():
    print(x, y)

# nested dicts
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily)

#Access Items in Nested Dictionaries
print(myfamily['child2']['name'])

