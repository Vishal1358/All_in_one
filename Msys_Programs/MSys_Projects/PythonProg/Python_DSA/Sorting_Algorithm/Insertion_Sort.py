def insertionsort(a):
    n = len(a)
    for i in range(1,n):
        cvalue = a[i]
        position = i
        while position > 0 and a[position-1] > cvalue:
            a[position] = a[position-1]
            position = position -1
        a[position] = cvalue

a = [5.0,6,8,2,5,4,9]
print("Orignal list\n", a)
insertionsort(a)
print("After insertion sorting\n",a)
