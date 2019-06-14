def SortInc3(a,b,c):
    if a > b and a > c:
        if b < c: return(a,c,b)
        else: return(a,b,c)
    elif b > a and b > c:
        if a < c: return(b,c,a)
        else: return(b,a,c)
    else:
        if a < b: return(c,b,a)
        else: return(c,a,b)

a = [[1,2,3], [1,3,2],
    [2,1,3], [2,3,1],
    [3,1,2], [3,2,1]]
for i in a:
    print(SortInc3(i[0], i[1], i[2]))
