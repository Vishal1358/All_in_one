a = [1,2,3,4,5]
s = len(a)
b = 0
i = 0
while s > i:
    print(a[i])
    # b.append(a)
    b -= (-a[i])
    i+=1
print(b)