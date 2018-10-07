n = int(input("N: "))
k = 0

for i in range(0, n+1):
    k += (i+n) ** 2

print("R = ", k)