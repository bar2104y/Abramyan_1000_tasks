import math
def RectPS(x1,y1,x2,y2):
    a = math.fabs(x1-x2)
    b = math.fabs(y1-y2)

    global p
    global s

    p = int((a+b)*2)
    s = int(a*b)
