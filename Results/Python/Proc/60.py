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

def Dist(xp,yp, xa,ya, xb,yb):
    return(2*Area(xa,ya, xb,yb, xp,yp)/Leng(xa,ya, xb,yb))

#return ha,hb,hc
def Altitudes(xa,ya, xb,yb, xc,yc):
    return(Dist(xa,ya, xb,yb, xc,yc), Dist(xb,yb, xa,ya, xc,yc), Dist(xc,yc, xa,ya, xb,yb) )

print(Altitudes(0,0, 0,3, 4,3))