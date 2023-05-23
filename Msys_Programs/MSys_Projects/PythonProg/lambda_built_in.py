# print(all([0,1,2,3,4]))
# print(all([char for char in "eio" if char in "aeiou"]))
# print(all([num for num in [4,2,10,6,8] if num % 2 == 0]))

# people = ["Vishal", "Sagar", "Nandu", "Naagendr"]
# print(all([name[0]=='N' for name in people]))
# print([name[0]=='N' for name in people])


nums = [2,21,26,23,10,8]
print(all([num % 2 == 0 for num in nums]))



print(any([num % 2 == 0 for num in nums]))