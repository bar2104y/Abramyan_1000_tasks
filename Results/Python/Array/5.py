a = []
n = int(input())

a.append(1)
a.append(1)
for i in range(2, n):
    a.append(a[i-2]+a[i-1])

print(a)