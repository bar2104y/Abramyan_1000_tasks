import math
def Poewer(a,b):
    if a <= 0: return(0)
    return(math.exp(b*math.log(a,math.e)))

for i in range(-1,11):
    print(Poewer(i,4))