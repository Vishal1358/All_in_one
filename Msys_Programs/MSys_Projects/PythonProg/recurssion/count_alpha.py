st = "aabccc1ddadd2222"
s1 = ""
n = len(st)
i = 0
while n > i:
    c = 0
    s2 = st[i]
    if s2.isdigit():
        s1 += s2
        i += 1
    else:
        c += 1
        j = i+1
        while j < n and s2 == st[j]:
            c +=1
            j +=1
        s1 += s2
        s1 += str(c)
        i = j
print(s1)