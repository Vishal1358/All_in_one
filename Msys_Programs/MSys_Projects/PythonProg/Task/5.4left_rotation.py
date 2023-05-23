# 4.Write Python program to perform left rotation of array elements by two positions.
def left_rotation(lst, rotation):
    return lst[rotation:]+lst[:rotation]

a = [1,2,3,4,5,6,7]
st = 3
print(left_rotation(a,st))