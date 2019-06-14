def Sign(x):
    if x < 0: return(-1)
    elif x == 0: return(0)
    else: return (1)

a = int(input('A: '))
b = int(input('B: '))
print(Sign(a)+ Sign(b))