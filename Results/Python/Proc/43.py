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