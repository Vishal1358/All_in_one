def parse_range(lst):
    lst = lst.split(',')
    print(lst)
    result = []
    for i in lst:
        bound = i.split('-')
        print(bound)
        start = int(bound[0])
        end = int(bound[-1])+1
        result += list(range(start,end))
    return result

lst = '1-2,4-4,8-13'
print(parse_range(lst))