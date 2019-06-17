n = int(input('N: '))

maxp = 0

for i in range(n):
    m,v = int(input('m: ')), int(input('v: '))
    if m*v > maxp:
        maxp = m/v
        index = i+1

print(index)