import math
def Leng(xa,ya, xb,yb):
    return(math.sqrt( (xa-xb)**2 + (ya-yb)**2 ))

def Perim(xa,ya, xb,yb, xc,yc):
    return(Leng(xa,ya, xb,yb) + Leng(xc,yc, xb,yb) + Leng(xa,ya, xc,yc))

def Area(xa,ya, xb,yb, xc,yc):
    p = Perim(xa,ya, xb,yb, xc,yc)/2
    ab = Leng(xa,ya, xb,yb)
    bc = Leng(xc,yc, xb,yb)
    ac = Leng(xc,yc, xa,ya)
    return(math.sqrt( p*(p-ab)*(p-bc)*(p-ac) ))
