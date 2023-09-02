# delete an item
my_dict = {'name': 'Abu', 'age': 31, 'address': 'Denver'}

del my_dict['age']

print(my_dict)

# get deleted item or default if it doesn't exist

my_dict = {'name': 'Abu', 'age': 31, 'address': 'Denver'}

removed_item =  my_dict.pop('age3', None)

print(removed_item)
print(my_dict)

# delete last item

my_dict = {'name': 'Abu', 'age': 31, 'address': 'Denver'}

popped_item =  my_dict.popitem()
print(popped_item)
print(my_dict)

# clear dictionary
my_dict.clear()
print(my_dict)