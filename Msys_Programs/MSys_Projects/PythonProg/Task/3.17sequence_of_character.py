def sequence_of_character(sequence,n):
    return sequence[n::]

l = [1,2,3,4,5,6,7,8,9]
s = "123456789"
t = (1,2,3,4,5,6,7,8,9)
print(sequence_of_character(s,3))
print(sequence_of_character(l,3))
print(sequence_of_character(t,3))