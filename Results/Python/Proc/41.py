import math
#from Proc 34
def Fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return(res)

def Sin1(x,e):
    sin = 0
    ex = x
    n = 1
    i = 1
    while ex >= e:
        ex = (x**n)/Fact(n)
        if i % 2 == 1:
            sin += ex
        else: sin -= ex
        i += 1
        n += 2
    return(sin)

print(Sin1(3.14/6,0.00001))
print(math.sin(3.14/6))
    