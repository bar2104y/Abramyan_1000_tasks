import math
#from Proc 34
def Fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return(res)

def Cos1(x,e):
    cos = 0
    ex = x
    n = 0
    i = 1
    while ex >= e:
        ex = (x**n)/Fact(n)
        if i % 2 == 1:
            cos += ex
        else: cos -= ex
        i += 1
        n += 2
    return(cos)  

print(Cos1(3.14/3,0.0000001))
print(math.cos(3.14/3))