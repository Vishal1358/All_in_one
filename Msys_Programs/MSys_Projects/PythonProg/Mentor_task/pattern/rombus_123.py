a = int(input("Enter odd number: "))
d = a//2
e = 1
for i in range(1,a+1):
    for j in range(1,d+1):
        print(" ",end="")
    for k in range(1,e+1):
        print(i,end=" ")
    
    if i <= a//2:
        d -= 1
        e += 2
    else:
        d += 1
        e -= 1
    print()