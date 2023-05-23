def reverse_string(s):
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)

s = "adfw$vf&yvy*ugv%uy"
print(reverse_string(s))
