sentence = "I need to work very hard to learn more about algorithms in Python!" 
a = sentence.split()
words = 0
word = 0
for i in a:
    # print(i)
    words += 1
    for j in i:
        if j.isalpha():
 
            word += 1
print(word//words)
# print(word)