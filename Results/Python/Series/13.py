k = 0

a = int(input())

while a != 0:
    if a > 0 and a % 2 == 0:
        k += a
    a = int(input())
    

print(k)