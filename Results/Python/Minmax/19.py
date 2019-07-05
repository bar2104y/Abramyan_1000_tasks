n = int(input('N: '))
m = 1001
k = 0

for i in range(n):
    x = int(input())
    if x < m:
        k = 1
        m = x
    elif x == m:
        k += 1

    

print(k)