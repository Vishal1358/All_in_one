row = 5
for i in range(row+1):
    for j in range(i):
        if i == j:
            print("",end=" ")
        else:
            print()
    print()