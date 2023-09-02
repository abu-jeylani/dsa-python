tuple1 = ('a', 'b', 'c', 'd', 'e')

print('a' in tuple1) # time complexity: O(n)

print(tuple1.index('c')) # time complexity: O(n)

def searchTuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            return f'the {element} is found at {i} index'
    return 'The element is not found'

print(searchTuple(tuple1, 'b'))

print(searchTuple(tuple1, 'f'))
