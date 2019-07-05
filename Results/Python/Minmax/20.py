n = int(input('N: '))
mi = 10001
ma = -10001
mik = 0
mak = 0

for i in range(n):
    x = int(input())
    if x > ma:
        mak = 1
        ma = x
    elif x< mi:
        mik = 1
        mi = x
    elif x == ma:
        mak += 1
    elif x == mi:
        mik += 1

    

print( mak + mik )