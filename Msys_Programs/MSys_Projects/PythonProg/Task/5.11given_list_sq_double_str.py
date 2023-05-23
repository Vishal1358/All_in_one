def squre_of_int_double_of_str(lst):
    lst1 = []
    for i in lst:
        if type(i) == int:
            lst1.append(i**2)
        else:
            lst1.append(i*2)
    return lst1


a = [8,9,10,"f",5,8,"d"]
print(squre_of_int_double_of_str(a))