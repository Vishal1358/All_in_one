n = int(input("Enter a number: "))
p = 1
for i in range(n,-(n+1),-1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(n,i-1,-1):
        print(str(p)+" ",end=" ")
    if(i>0):
        p += 1
    else:
        p -+ 1
    print()