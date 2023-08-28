
def tail(n):
    #base case
    if n ==0: return
    # first of all we do some operations
    #operation = print()
    print(n)

    tail(n-1)


tail(10)


# the same but different approach

print('starting')

for n in range(5, 0, -1):
    print(n)