def alpha(string):
    res = ""
    n = len(string)   #12
    i = 0
    while i < n:
        char = string[i]
        j = i+1
        count = 1
        while j < n and char ==string[j]:
            count +=1
            j += 1
        res += char
        res += str(count)
        i = j
    print(res)

string = "laxminarayan"
print(alpha(string))