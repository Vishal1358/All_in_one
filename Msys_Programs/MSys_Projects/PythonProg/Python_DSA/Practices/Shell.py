def shell(a):
    n = len(a)
    gap = n // 2 
    while gap > 0:
        i = gap
        while i < n:
            temp = a[i]
            j = i - gap
            while j >= 0 and a[j] > temp:
                a[j+gap] = a[j]
                j = j - gap
            a[j+gap] = temp
            i = i+1
        gap = gap//2


A = [5,6,8,9,7,2,3]
print("before sort",A)
shell(A)
print("after sort",A)