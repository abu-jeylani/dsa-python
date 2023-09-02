def permutation(list1, list2):

    # base case
    if len(list1) != len(list2):
        return False
    
    #sort each list to get in chron order
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else: 
        return False

list1 = [1,2,3]
list2 = [2,1,3]

print(permutation(list1,list2))

list3 = [3,4,5]
list4 = [5,6,6]

print(permutation(list3,list4))