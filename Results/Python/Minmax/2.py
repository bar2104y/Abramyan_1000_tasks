n = int(input('N: '))

a,b = int(input('a: ')), int(input('b: '))
mi = a*b

for i in range(n-1):
    a,b = int(input('a: ')), int(input('b: '))
    mi = min(mi, a*b)

print(mi)