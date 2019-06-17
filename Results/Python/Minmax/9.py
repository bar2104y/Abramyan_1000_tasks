n = int(input('N: '))

x = int(input('1: '))
ma = x
first,last = 1,1

for i in range(2,n+1):
    x = int(input(str(i)+': '))
    if x > ma:
        first = i
        ma = x
    if x == ma:
        last = i

print(first,last)