def RootCount(a,b,c):
    d = b*b - (4*a*c)
    if d > 0: return(2)
    elif d == 0: return(1)
    else: return(0)

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
print('A*x^2+B*x+C = 0 имеет', RootCount(a,b,c), 'корня(ей)')