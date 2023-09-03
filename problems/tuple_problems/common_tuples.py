def common_elements(tuple1, tuple2):
    commons = []
    for element in tuple2:
        if element in tuple1:
            commons.append(element)
    return tuple(commons)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)


# better way of doing it is using the & operator to find the common ones
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)