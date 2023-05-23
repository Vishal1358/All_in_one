a = int(input())
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(" ",end="")
    print("*"*a)
    a+=2