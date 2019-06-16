import math
def Power4(x,a,e):
    res = 1+a*x
    ex = 1
    n = 2
    while math.fabs(ex) >= e:
        ex = a*(a-1) * (x**n)/math.factorial(n)
        res += ex
        n += 1
    return(res)

print(Power4(0.1,2.88,0.00000000000000000001))
print(1.1**2.88)