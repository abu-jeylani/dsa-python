def check_same_frequency(list1, list2):
    # TODO
    def count_elements(lst):
        counter = {}
        for num in lst:
            counter[num] = counter.get(num,0) + 1
        return counter
    return count_elements(list1) == count_elements(list2 )



list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))