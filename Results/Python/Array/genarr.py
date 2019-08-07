def genLinearArr( n, o=0 ):
    a = []
    for i in range(n):
        a.append(i)
    return(a)

def genRandomArr( n, s = 0, e = 100 ):
    a = []
    import random
    for i in range(n):
        a.append(random.randint(s,e))
    return(a)