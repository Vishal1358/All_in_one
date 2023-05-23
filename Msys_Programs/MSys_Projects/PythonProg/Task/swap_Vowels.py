def reverse_vowel(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] in vowels:
            j -= 1
        else:
            i += 1
    return ''.join(s)
s = 'Hello'
reversed_vowels = reverse_vowel(s)
print(reversed_vowels)  # output: Holle

# def reverse_vowel(s):
#     vowels = []
#     for char in s:
#         if char in "aeiouAEIOU":
#             vowels.append(char)
#     vowels.reverse()
#     new_string = ""
#     for char in s:
#         if char in "aeiouAEIOU":
#             new_string += vowels.pop(0)
#         else:
#             new_string += char
#     return new_string

# print(reverse_vowel("Hello")) # Output: Holle
# print(reverse_vowel("Python")) # Output: Python
# print(reverse_vowel("Algorithme")) # Output: elgirothmA
