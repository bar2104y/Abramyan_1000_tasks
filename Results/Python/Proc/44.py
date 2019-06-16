import math
def Arctg1(x,e):
    #arctg(x+1)
    ex = x
    arctg = x
    i = 1
    while math.fabs(ex) >= e:
        ex = ((x ** (i*2+1)) / (i*2+1) ) * ((-1)**i)
        arctg += ex
        i+=1
    return(arctg)
