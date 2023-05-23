def reverse_words(string):
    words = string.split() # split the string into words
    reversed_words = [word[::-1] for word in words] # reverse each word
    reversed_string = ' '.join(reversed_words) # join the reversed words
    return reversed_string

original_string = 'Hello World'
reversed_string = reverse_words(original_string)
print(reversed_string)
