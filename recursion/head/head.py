

def head(n):

    if n == 0: return

    #we make the recursive function call
    head(n-1)

    print(n)