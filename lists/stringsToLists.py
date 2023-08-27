
# Strings and Lists

a = 'spam '
b = list(a)
print(b)

# split method
a = 'spam spam spam'
b = a.split()
print(b)

# with delimiter
a = 'spam-spam-spam'
delimiter = '-'
b = a.split(delimiter)
print(b)

# join list of string using the delimiter
print(delimiter.join(b))