

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

print(shoppingList[-1])

for i, item in enumerate(shoppingList):
    print(f'item: {item} at index: {i}')

#Update/Insert

myList = [1,2,3,4,5,6,7]
print(myList)

myList.insert(0,0)
print(myList)

myList.extend([8,9,19])
print(myList)

myList.append(55)
print(myList)


# how to slice & delelte
print(myList[1:])
print(myList)

itemPoppedOff = myList.pop()
print(itemPoppedOff)
print(myList)

myList.remove(9)
print(myList)

#searching for an element in the list
my_list = [10,20,30,40,50,60,70,80,90]

target =50

if target in my_list:
    print(f'{target} is in the list')
else:
    print(f'{target} is not in the list')

# Linear Search

def linear_search(p_list, p_target):
    for i , value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(my_list, target))