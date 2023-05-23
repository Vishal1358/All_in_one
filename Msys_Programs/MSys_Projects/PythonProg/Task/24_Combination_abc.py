# 24. You have given a string str1 = "abcbaefabcabchijkl"
# your task is to find the combination of given word without repetition, present in the string , given word 'abc'
# o/p = 7
# explaination :abc, cba,cba,bca, acb,cab, bac

str1 = "abcbaefabcabchijkl"
def combination(string,word):
    count = 0
    for i in range(len(string)):
        new_word = string[i:i+len(word)]
        t = 0
        for j in range(len(new_word)):
            if word[j] in new_word:
                t+=1
            if t==len(word):
                print(new_word)
                count+=1
    return count

str1 = "abcbaefabcabchijkl"
word = "abc"
print(combination(str1,word))