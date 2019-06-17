import math

#Модуль длины отрезка
def Leng(xa,ya, xb,yb):
    return(math.sqrt( (xa-xb)**2 + (ya-yb)**2 ))

#Периметр треугольника
def Perim(xa,ya, xb,yb, xc,yc):
    return(Leng(xa,ya, xb,yb) + Leng(xc,yc, xb,yb) + Leng(xa,ya, xc,yc))

#Площадь треугольника
def Area(xa,ya, xb,yb, xc,yc):
    p = Perim(xa,ya, xb,yb, xc,yc)/2
    ab = Leng(xa,ya, xb,yb)
    bc = Leng(xc,yc, xb,yb)
    ac = Leng(xc,yc, xa,ya)
    return(math.sqrt( p*(p-ab)*(p-bc)*(p-ac) ))

#Расстояние от точки до прямой на плоскости
def Dist(xp,yp, xa,ya, xb,yb):
    return(2*Area(xa,ya, xb,yb, xp,yp)/Leng(xa,ya, xb,yb))

#Длины высот в треугольнике: Ha,Hb,Hc
def Altitudes(xa,ya, xb,yb, xc,yc):
    return(Dist(xa,ya, xb,yb, xc,yc), Dist(xb,yb, xa,ya, xc,yc), Dist(xc,yc, xa,ya, xb,yb) )
