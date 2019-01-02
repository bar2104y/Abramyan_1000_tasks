n = int(input("N: "))
a = int(input())
k = 0

m = []
for i in range(1, n):
    tmp = int(input())
    if a < tmp:
        m.append(a)
        k += 1
    a = tmp

print("K:", k)
for tmp in m:
    print(tmp)
