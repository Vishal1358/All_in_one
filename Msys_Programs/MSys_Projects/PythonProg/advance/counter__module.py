from collections import Counter

# mylist = [1,1,1,1,1,2,2,2,3,3,3,4,4,4,4]
# mylist = ['a','a','a',5,5,5,5,6]

st = ('sfgjsdfgjsdghjhsgjdfhgsd')
# a = Counter(mylist)
# a = Counter(st)

sen = "How many times does each word show up in this sentence with a word"

a = Counter(sen.lower().split())
print(a)