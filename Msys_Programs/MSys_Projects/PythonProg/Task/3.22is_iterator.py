# def is_iterator(iterable):
#     if "__iter__" and "__next__" in dir(type(iterable)):
#         return True
#     return False


# a = [123]
# # print(dir(a))
# aa = iter(a)
# print(is_iterator(a))

def is_iterator(iterable):
    if iter(iterable) is iterable:
        return True
    else:        
       return False
print(is_iterator(iter([])))
print(is_iterator([1,2,3]))