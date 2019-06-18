n = int(input('N: '))

m = 100001
for i in range(n):
    x= int(input())
    if x > 0:
        m = min( m, x )
    
print( 0 if m == 10001 else m)