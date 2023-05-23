strs = ["eat","tea","tan","ate","nat","bat"]

groups = {}
for word in strs:
    sorted_word = ''.join(sorted(word))
    if sorted_word not in groups:
        groups[sorted_word] = [word]
    else:
        groups[sorted_word].append(word)
print(list(groups.values()))

