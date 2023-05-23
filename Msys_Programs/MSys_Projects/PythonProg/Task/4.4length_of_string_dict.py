
def word_of_len(text):
    x = text.split()
    word_len = {}
    for i in x:
        word_len[i] = len(i)
    print(word_len)

text = "Be happy"
word_of_len(text)