a = []
n = 10
for i in range(n):
    a.append(i)

for i in range(int(n/2)):
    tmp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = tmp

print(a)