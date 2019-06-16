def GCD2(a,b):
    if b == 0: return(a)
    else:
        r = a % b
        return(GCD2(b,r))

def LCM2(a,b):
    return(a*b//GCD2(a,b))

a,b,c,d = 64,48,111,432
print(a,b,'    ', LCM2(a,b))
print(c,d,'    ', LCM2(c,d))