#Самое простое решение O = n^2
n = int(input("N: "))

a = [0,1,2,3,4,5,4,6,7,8,9]
n = len(a)

for i in range(n):
    for j in range(i+1,n):
        if a[j] == a[i]:
            print(i,j)
            exit()