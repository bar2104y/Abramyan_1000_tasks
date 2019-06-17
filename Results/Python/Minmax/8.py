n = int(input('N: '))

x = int(input('1: '))
mi = x
last,first = 1,1

for i in range(2,n+1):
    x = int(input(str(i)+': '))
    if x < mi:
        first = i
        mi = x
    if x == mi:
        last = i

print(first,last)