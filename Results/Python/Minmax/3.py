n = int(input('N: '))

a,b = int(input('a: ')), int(input('b: '))
ma = a*b

for i in range(n-1):
    a,b = int(input('a: ')), int(input('b: '))
    ma = max(ma, a*b)

print(ma)