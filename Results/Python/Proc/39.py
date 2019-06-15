import math
def Power(a,b):
    if a <= 0: return(0)
    return(math.exp(b*math.log(a,math.e)))

def Power2(a,n):
    if a == 0: return(1)
    tmp = a    
    for i in range(n-1):
        tmp *= a
    
    if n < 0: tmp = 1/tmp
    return(tmp)

def Power3(a,b):
    if b % 1 == 0: return(Power2(a,int(b)))
    return(Power(a,b))

a = 0
for i in range(10):
    print(Power3(2,a))
    a+=0.2