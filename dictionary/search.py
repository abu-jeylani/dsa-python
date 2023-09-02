myDict = {'name': 'Abu', 'age': 31, 'address': 'Denver'}

def search(dict, value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'The value does not exist'

print(search(myDict,32))