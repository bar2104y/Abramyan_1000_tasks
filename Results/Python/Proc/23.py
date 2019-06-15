def Quarter(x,y):
    #x,y != 0,0
    if x > 0:
        if y > 0: c = 1
        else: c = 4
    else:
        if y > 0: c = 2
        else: c = 3
    return(c)

print(Quarter(int(input('X: ')), int(input('Y: '))))