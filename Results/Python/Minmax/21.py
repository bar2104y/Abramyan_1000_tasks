n = int(input('N: '))
mi = 10001
ma = -10001
s = 0

for i in range(n):
    x = int(input())
    if x > ma: ma = x
    if x < mi: mi = x
    s += x

    
print( (s-ma-mi)/(n-2) )