def pair_sum(myList, sum):
    output = []

    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                output.append(f'{myList[i]}+{myList[j]}')
    return output

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
