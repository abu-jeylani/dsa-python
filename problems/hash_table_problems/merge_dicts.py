def merge_dicts(dict1 : list, dict2: list):
    # TODO
    new_dict = dict1.copy()

    for key, value in dict2.items():
        new_dict[key] = new_dict.get(key,0) + value
    
    return new_dict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))