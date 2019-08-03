a = []
n = int(input("N: " ))
cnt = 0
for i in range(n):
    a.append(i)

for i in range(n):
    if a[i] % 2 == 1:
        print(a[i])
        cnt += 1

print("Count:", cnt)