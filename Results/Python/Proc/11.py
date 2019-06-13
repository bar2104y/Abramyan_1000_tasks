def MinMax(x,y): 
    if x > y:
        tmp = x
        x = y
        y = tmp
    return(x,y) # x -> Min and y -> Max

a,b,c,d = 6,10,9,4
a,b = MinMax(a,b) # a -> Min, b -> Max
c,d = MinMax(c,d) # c -> Min, d -> Max
mi, t = MinMax(a,c)
t, ma = MinMax(b,d)
del(t)
print(mi,ma)
