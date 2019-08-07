n = int(input("N: "))
a = []

for i in range(n): a.append(i)

f = bool(a[0] > 0)

for i in range(1,n):
    if bool(a[0] > 0) == f:
        print(i)
        exit()
    else: f = bool(a[i] > 0)

print(0)

