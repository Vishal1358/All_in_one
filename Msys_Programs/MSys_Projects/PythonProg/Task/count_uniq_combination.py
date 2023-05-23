str1 = "abcbaefabcabchijkl"
given_word = "abc"
word_len = len(given_word)
result_set = set()

for i in range(len(str1) - word_len + 1):
    window = str1[i:i+word_len]
    if sorted(window) == sorted(given_word):
        result_set.add(window)

print(len(result_set)) # prints 7
print(result_set)
