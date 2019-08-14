a = [9,8,7,6,4,2,1]
b = [65,62,55,11]
c = [99,88,77]

if a[0] > b[0]:
    if a[0] > c[0]:
        d = a
        if b[0] > c[0]:
            d += b+c
        else:
            d += c+b
    else:
        d = c
        if a[0] > b[0]:
            d += a+b
        else:
            d += b+a
elif b[0] > c[0]:
    d = b
    if a[0] > c[0]:
        d += a+c
    else:
        d += c+a
else:
    d = c
    if a[0] > b[0]:
        d += a+b
    else:
        d += b+a

print(d)