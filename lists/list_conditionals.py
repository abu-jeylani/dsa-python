'''
 only puts in new array if it matches
'''
prev_list = [-1,10,-20,2,-90, 60, 45,20]
new_list = [item*item for item in prev_list if item > 0 ]
print(new_list)

sentence = 'My name is Mohamed'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('a'))

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

'''
This approach gives it the ability to have an else
'''
prev_list = [-1,10,-20,2,-90, 60, 45,20]
new_list = [item if item>0 else 0 for item in prev_list]
print(new_list)