def float_range(start,end,step):
    l = []
    while start < end:
        l.append(round(start,2))
        start += step
    print(l)
    
float_range(0,0.1,0.01)