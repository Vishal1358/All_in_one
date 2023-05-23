a = 8
p = 1
for i in range(a, -(a+1),-1):
    for j in range(1,abs(i) + 1):
        print(" ",end="")
    for k in range(a,abs(i)-1,-1):
        print(str(p)+" ",end="")
    if (i>0):
        p += 1
    else:
        p -= 1
    print()