my_dict = {
    3: "three",
    5: "five",
    9: "nine",
    2: "two",
    1:  "one", 
    4: "four"
}

#only works with keys
print(3 in my_dict)

#to check for values
print("three" not in my_dict.values())

# returns count of key value pairs
print(len(my_dict))


#sorts keys

print(sorted(my_dict))
print(my_dict)
