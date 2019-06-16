def IncTime(h,m,s,t):
    h += t//3600
    m += t%3600 // 60
    s += t-(t//3600*3600) - (t%3600 // 60)*60
    return(h,m,s)