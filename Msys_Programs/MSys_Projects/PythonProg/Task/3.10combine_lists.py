# def combine_lists(lst1, lst2):
#     combine_lists = lst1 + lst2
#     return combine_lists
    
def combine_lists(lst1, lst2):
    if len(lst1) > len(lst2):
        for i in range(lst1):
            print(lst1[i] + lst2[i])
    else:        
        for i in range(lst2):
            print(lst1[i] + lst2[i])
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10,11]
print(combine_lists(l1,l2))