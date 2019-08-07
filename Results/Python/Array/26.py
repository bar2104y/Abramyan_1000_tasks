n = int(input("N: "))
a = []

for i in range(n): a.append(i)

f = a[0] % 2

for i in range(1,n):
    if a[i] % 2 == f:
        print(i)
        exit()
    else: f = a[i] % 2

print(0)

