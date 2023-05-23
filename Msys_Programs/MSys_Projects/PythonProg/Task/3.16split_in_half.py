def split_in_half(lst):
    length = len(lst)//2
    return [lst[:length],lst[length:]]
    
lst1 = [1,2,3,4,5,6,7,8,9]
print(split_in_half(lst1))