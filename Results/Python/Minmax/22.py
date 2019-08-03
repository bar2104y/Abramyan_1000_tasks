n = int(input())

min1, min2 = 1000,1001

for i in range(n):
    tmp = int(input())
    if tmp < min2:
        if tmp < min1:
            min2 = min1
            min1 = tmp
        else:
            min2 = tmp

    
print(min1, min2)