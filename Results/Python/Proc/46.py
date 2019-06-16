#НОД
def GCD2(a,b):
    if b == 0: return(a)
    else:
        r = a % b
        return(GCD2(b,r))

a,b,c,d = 64,48,111,432
print(a,b,'    ', GCD2(a,b))
print(c,d,'    ', GCD2(c,d))
