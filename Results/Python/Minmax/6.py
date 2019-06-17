n = int(input('N: '))

x = int(input('1: '))
ma,mi = x,x
mai,mii = 1,1

for i in range(2,n+1):
    x = int(input(str(i)+': '))
    if x >= ma:
        ma = x
        mai = i
    if x < mi:
        mii = i
        mi = x

print('Min:', mii, mi)
print('Max:', mai, ma)