def insert_value_front(input_tuple, value_to_insert):
    # TODO
    newTuple = (1,) + input_tuple
    return newTuple


input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)