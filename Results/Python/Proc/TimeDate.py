def TimeToHMS(t):
    h = t // 3600
    m = t%3600 // 60
    s = t-h*3600-m*60
    return(h,m,s)

def IncTime(h,m,s,t):
    h += t//3600
    m += t%3600 // 60
    s += t-(t//3600*3600) - (t%3600 // 60)*60
    return(h,m,s)

def IsLeapYear(y):
    if y % 4 != 0: return(False)
    if y%100 == 0 and y%400 != 0: return(False)
    return(True)

def MonthDays(m,y):
    if m == 2:
        return(29 if IsLeapYear(y) else 28 )
    else:
        return (31 if (m%7)%2 != 0 or m == 7 else 30)

def PrevDate(d,m,y):
    if d == 1:
        if m == 1:
            y -= 1
            m = 12
        else:
            m -= 1
        d = MonthDays(m,y)
    else: d -= 1
    return(d,m,y)

def NextDate(d,m,y):
    if d == MonthDays(m,y):
        d = 1
        if m == 12:
            m = 1
            y += 1
        else: m+=1
    else: d += 1
    return(d,m,y)

