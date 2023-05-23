s = "Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331."

s = ''.join(c for c in s if c.isalnum() or c.isspace()).lower()
# print(s)

words = s.split()
palindrome_dict = {}
for word in words:
    if word == word[::-1]:
        if word in palindrome_dict:
            palindrome_dict[word] += 1
        else:
            palindrome_dict[word] = 1

print(palindrome_dict)
