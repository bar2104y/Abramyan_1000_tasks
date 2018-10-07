n = int(input("N: "))
k = 0

for i in range(1, 2*n):
    if i % 2 == 1:
        k += i
        print(k)

print("R = ", k)