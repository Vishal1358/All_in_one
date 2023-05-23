l = []
for i in range(1, 7):
    l.append(list("1" * i))
m = 2
k = m -1
for i in range(len(l)-1,-1,-1):
    for j in range(m,k,-1):
        try:
            l[i][j] = 0
        except:
            continue
        k -=1
        if k < 0:
            k = -1
print(*l,sep="\n")