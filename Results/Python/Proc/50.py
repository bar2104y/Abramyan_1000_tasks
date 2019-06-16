def TimeToHMS(t):
    h = t // 3600
    m = t%3600 // 60
    s = t-h*3600-m*60
    return(h,m,s)

print(TimeToHMS(3675))