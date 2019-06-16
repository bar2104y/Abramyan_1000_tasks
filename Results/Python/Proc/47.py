def GCD2(a,b):
    if b == 0: return(a)
    else:
        r = a % b
        return(GCD2(b,r))

def Frac1(a,b):
    nod = GCD2(a,b)
    return( str(a//nod) + ' / ' + str(b//nod) )

a,b = 111,423
print(a,'/',b, '=', Frac1(a,b))