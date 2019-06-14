def RingS(r1,r2):
    return(3.14*r1*r1 - 3.14*r2*r2)

print('R1 > R2')
r1 = float(input('R1: '))
r2 = float(input('R2: '))

print(RingS(r1,r2))