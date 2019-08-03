a = []

n = int(input())
a.append(int(input("A: ")))
a.append(int(input("B: ")))
s = a[0]+a[1]

for i in range(2,n):
    a.append(s)
    s *= 2

print(a)
