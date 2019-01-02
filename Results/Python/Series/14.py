k = int(input())
a = int(input())

s = 0

while a != 0:
    if a < k:
        s += 1
    a = int(input())
    

print(s)