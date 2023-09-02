'''
Define a function which takes a 
dictionary as a parameter and returns the key 
with the highest value in a dictionary.
'''

def max_value_key(my_dict:list):
    # TODO
    max_pair = next(iter(my_dict.items()))
    for key,value in my_dict.items():
        if value > max_pair[1]:
            max_pair = (key,value)
    
    return max_pair[0]



my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))



print("-------------------------------------------------")

def max_value_key(my_dict:list):
    return max(my_dict, key=my_dict.get)



my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))