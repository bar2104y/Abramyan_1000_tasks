n = int(input('N: '))

x = int(input('1: '))
mi = x
index = 1

for i in range(n-1):
    x = int(input(str(i+2)+': '))
    if x < mi:
        index = i+2
        mi = x

print(index, mi)

