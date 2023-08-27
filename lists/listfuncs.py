# List operations/functions

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# to repeat a set in a list
a = [0,1]
a = a*4 #this will result in [0,1,0,1]
print(a)


# to get a count of the list
a = [0,1,2,3,4,5,6]
print(f'{len(a)} is the length')

# max element
print(f'{max(a)} is the max in the list')

#
print(f'{sum(a)} is the sum in the list')

'''
list()
'''

myList = list()

while(True):
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    myList.append(value)

average = sum(myList)/len(myList)

print('Average:', average)