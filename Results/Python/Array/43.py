n = int(input())

#Тут можно либо ввести массив, либо его умно гененрировать
a = [0,1,2,2,3,4,5,5,5,6,7,8,9,9,9,10]
print(a)
n = len(a)

cnt = 1

for i in range(1,n):
    if a[i] != a[i-1]: cnt += 1

print(cnt)