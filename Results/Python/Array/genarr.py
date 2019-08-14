def genLinearArr( n, offset=0 ):
    a = []
    for i in range(n):
        a.append(i+offset)
    return(a)

def genRandomArr( n, s = 0, e = 100 ):
    a = []
    import random
    for i in range(n):
        a.append(random.randint(s,e))
    return(a)