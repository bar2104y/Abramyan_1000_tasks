n = int(input("N: "))

a = int(input())
m = []

m.append(a)

for i in range(1, n):
    tmp = a
    a = int(input())
    if a != tmp:
        m.append(a)

for tmp in m:
    print(tmp)
