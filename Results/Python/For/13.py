n = int(input("N: "))
k = 1.0

for i in range(1, n+1):
    if i % 2 == 0:
        k -= 1+i/10
    else:
        k += 1+i/10

print("R = ", k)