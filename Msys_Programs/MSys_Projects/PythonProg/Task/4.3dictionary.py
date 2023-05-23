numbers = [4,5,7,2,9,8] 
odd = []
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
result = dict({"even":even,"odd":odd})
print(result)