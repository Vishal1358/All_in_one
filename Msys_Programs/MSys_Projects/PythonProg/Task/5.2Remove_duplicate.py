def remove_duplicate(num):
    b = []
    for i in num:
        if i not in b:
            b.append(i)
    print(b)

a = [3,4,6,7,9,4]
remove_duplicate(a)