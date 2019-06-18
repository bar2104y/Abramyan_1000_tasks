#0<b<c
b = int(input('B: '))
c = int(input('C: '))
n = 10
ma = 0

for i in range( 1, n+1 ):
    x = int(input())
    if x>b and x<c and x>ma:
        j = i
        ma = x

print(j, ':', ma)