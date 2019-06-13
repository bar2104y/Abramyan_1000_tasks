def Swap(x,y):
    tmp = x
    y = x
    x = tmp
    del(tmp)
    return x,y

a = 1
b = 2
c = 3
d = 4

a,b = Swap(a, b)
c,d = Swap(c, d)
b,c = Swap(b, c)
print(a,b,c,d)