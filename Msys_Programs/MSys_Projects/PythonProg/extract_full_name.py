def extract_full_name(lst):
    return list(map(lambda val: {} ,{}.format(val['first'], val['last']), lst))


print(extract_full_name({'first':'vishal','last':'hirandagi'}))