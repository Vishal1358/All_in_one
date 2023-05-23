def sort(lst):
    n = len(lst)
    for i in range(n-1,0,-1):
        for j in range(i):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

lst = [56,2,13,1,78,4,6]
sort(lst)
print(lst)