n = int(input())

max1,max2,max3 = -2,-1,0

for i in range(n):
    tmp = int(input())
    if tmp > max1:
        if tmp > max2:
            if tmp >max3:
                max1 = max2
                max2 = max3
                max3 = tmp
            else:
                max1 = max2
                max2 = tmp
        else:
            max1 = tmp

    
print(max1,max2,max3)