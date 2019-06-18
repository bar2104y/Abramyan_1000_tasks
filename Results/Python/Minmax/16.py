n = int(input('n: '))

ma = 100001
for i in range(1,n):
    x = int(input())
    if x < ma:
        j = i
        ma = x

print(j-1)