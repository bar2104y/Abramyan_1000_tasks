def GCD2(a,b):
    if b == 0: return(a)
    else:
        r = a % b
        return(GCD2(b,r))

def GCD3(a,b,c):
    return(GCD2(GCD2(a,b),c))