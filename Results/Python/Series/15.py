k = int(input("K:"))
a = int(input())

n = 0
i = 1

f = False

while a != 0:
    if a > k and f == False:
        n = i
        f = True
    i += 1
    a = int(input())
    

print(n)