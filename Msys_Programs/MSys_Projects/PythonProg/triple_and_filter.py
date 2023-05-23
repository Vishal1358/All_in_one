def triple_and_filter(lst):
    return list(filter(lambda x: x%4==0 , map(lambda x: x*3,lst)))


print(triple_and_filter([6,8,12,18,24]))