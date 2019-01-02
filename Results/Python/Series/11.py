
k = int(input())
n = int(input())

f = False

for i in range(0,n):
    a = int(input())
    if a < k:
        f = True

print(f)