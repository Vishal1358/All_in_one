def none_replace(lst):
    recent_value = None
    for i in range(len(lst)):
        if lst[i] is None:
            lst[i] = recent_value
        else:
            recent_value = lst[i]

    print(lst)

lst = [1,None,None,3,None,4] 
none_replace(lst)