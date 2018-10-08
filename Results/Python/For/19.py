print("!N")
n = int(input("N: "))
k = 1

for i in range(1, n+1):
    k *= i

print("!N = ", k)