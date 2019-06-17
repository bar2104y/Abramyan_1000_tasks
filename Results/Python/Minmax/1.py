n = int(input('N: '))

x = int(input())
ma, mi = x,x

for i in range(n-1):
    x = int(input())
    ma = max(ma,x)
    mi = min(mi,x)

print(mi, ma)

