n = int(input('N: '))
m = 0
j1,j2 = 0,0

for i in range(n):
    x = int(input())
    if x > m:
        j1 = i
        m = x
    elif x == m:
        j2 = i

print(j2-j1 if j2>j1 else 0)