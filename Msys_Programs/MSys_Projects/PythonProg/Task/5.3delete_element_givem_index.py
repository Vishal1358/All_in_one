def remove_index_value(lst,idx):
    s = []
    for i in range(len(lst)):
        if i != idx:
            s.append(a[i])
        else:
            pass
    print(s)

a = [1,2,3,4,5,6]
index = 2
remove_index_value(a,index)