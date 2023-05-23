a = int(input())
for i in range(a,-(a),-1):
    for j in range(1,abs(i)+1):
        print(" ",end="")
    for k in range(a,abs(i),-1):
        print("* ",end="")
    print()