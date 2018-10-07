print("A < B")
a = int(input("A: "))
b = int(input("B: "))
k = 0

for i in range(a+1, b):
    k += 1
    print(i)

print("K = ", k)