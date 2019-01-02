n = int(input("N: "))
a = int(input())

f = True

for i in range(1, n):
    tmp = a
    a = int(input())
    if a < tmp:
        f = False

print(f)