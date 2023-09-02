myDict = {'name': 'Abu', 'age': 31, 'address': 'Denver'}

#copy 
dict = myDict.copy()

#from keys

newDict = {}.fromkeys([1,2,3],0)

print(newDict)

# get()
print(myDict.get(27))


#items, key value pairs in an array of tuples
print(myDict.items())

#gets keys
print(myDict.keys())

#removes random element in dict
print(myDict.popitem())
print(myDict)

''' set default when you want to add key value to dict
but don't want to overwrite it'''
print(myDict.setdefault('name', 'john'))
print(myDict)
print(myDict.setdefault('name1', 'added'))
print(myDict)


#removes a specific key value pair & returns removed pair
popped = myDict.pop('name1', None)
print(popped)
print(myDict)

#displays a list of values in dictionary
print(myDict.values())

#update method, take one dictionary and add another
newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)
