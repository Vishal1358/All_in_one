lst = ['data','science','artificial', 'intelligence'] 
dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}

result = {}
for i in lst:
    if i in dct:
        result[i] = dct[i]
    else:
        result[i] = len(i)

print(result)
