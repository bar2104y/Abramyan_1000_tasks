a = []
n = int(input("N: " ))
cnt = 0
for i in range(n):
    a.append(i)

for i in range(n):
    if a[n-1-i] % 2 == 0:
        print(a[n-1-i])
        cnt += 1

print("Count:", cnt)