import math
def Ln1(x,e):
    #ln(x+1)
    ex = x
    ln = 0
    i = 1
    while math.fabs(ex) >= e:
        ex = ((x ** i) /i) * ((-1)**i) * (-1)
        ln += ex
        i+=1
    return(ln)

print(Ln1(0.5, 0.0000000000000000001))
print(math.log1p(0.5))