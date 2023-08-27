
'''
this makes points to the same object when using another variable to copy the list
'''
myList = [32,4,6,5,7,6,9]
anotherList = myList
myList.sort()
print(anotherList)

''' 
this actually copies it
'''
myList = [32,4,6,5,7,6,9]
anotherList = myList[:]
myList.sort()
print(anotherList)