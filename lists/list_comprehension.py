# one way of doing it
prev_list = [1,2,3]
new_list = []

for i in prev_list: 
    multiply_2 = i *2
    new_list.append(multiply_2)

print(new_list)


# one line way of doing it
prev_list = [1,2,3]
new_list = []
new_list = [i for i in prev_list]
print(new_list)

language = 'Python'
new_list = [letter for letter in language]
print(new_list)