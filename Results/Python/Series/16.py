k = int(input("K:"))
a = int(input())

n = 0
i = 1

while a != 0:
    if a > k:
        n = i
    i += 1
    a = int(input())
    

print(n)