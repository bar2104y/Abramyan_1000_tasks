#0<b
b = int(input('b: '))
n = 10
mi = 10000

for i in range(1,n+1):
    x= int(input())
    if x > b and x < mi:
        j = i
        mi = x
print(j)