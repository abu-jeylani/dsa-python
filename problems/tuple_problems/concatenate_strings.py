def concatenate_strings(input_tuple):
    string_builder = ''
    for string in input_tuple:
        string_builder += f'{string} '
    return string_builder.removesuffix(" ")




input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)

# other way of doing it is 

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)




input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)