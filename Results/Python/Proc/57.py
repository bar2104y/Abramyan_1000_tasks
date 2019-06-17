import math
def Leng(xa,ya, xb,yb):
    return(math.sqrt( (xa-xb)**2 + (ya-yb)**2 ))

def Perim(xa,ya, xb,yb, xc,yc):
    return(Leng(xa,ya, xb,yb) + Leng(xc,yc, xb,yb) + Leng(xa,ya, xc,yc))

print(Perim(0,0,0,4,3,0))