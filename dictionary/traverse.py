myDict = {'name': 'Abu', 'age': 31, 'address': 'Denver'}

def traverse_dict(dict):
    for key in dict: 
        print(key, dict[key])
        
traverse_dict(myDict)