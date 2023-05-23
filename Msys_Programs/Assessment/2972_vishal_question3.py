'''
"Nitin and his mom went to a park last friday Nitin's Mom obbseved 
that the weather was too cool if we reverse the number then we also get 1331"

o/p = (Nithin - 1 time, mom - 2 time, 1331)
'''

s = "Nitin and his mom went to a park last friday Nitin's Mom obbseved that the weather was too cool if we reverse the number then we also get 1331 then we also get 1331"

s = ''.join(c for c in s if c.isalnum() or c.isspace()).lower()

words = s.split()
palindrome_dict = {}
for word in words:
    if word == word[::-1]:
        if word in palindrome_dict:
            palindrome_dict[word] += 1
        else:
            palindrome_dict[word] = 1

print(palindrome_dict)
