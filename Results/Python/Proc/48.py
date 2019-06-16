def GCD2(a,b):
    if b == 0: return(a)
    else:
        r = a % b
        return(GCD2(b,r))

def LCM2(a,b):
    return(a*b//GCD2(a,b))