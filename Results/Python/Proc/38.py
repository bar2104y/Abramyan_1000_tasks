def Power2(a,n):
    if a == 0: return(1)
    tmp = a    
    for i in range(n-1):
        tmp *= a
    
    if n < 0: tmp = 1/tmp
    return(tmp)

for i in range(-5,6):
    print(i, Power2(2, i))