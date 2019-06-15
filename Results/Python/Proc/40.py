#from Proc 34
def Fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return(res)

def Exp1(x,e):
    n = 1
    ex = x
    res = 0
    while ex > e:
        ex = (x**n) / Fact(n)
        n += 1
        res += ex
    
    return(res)