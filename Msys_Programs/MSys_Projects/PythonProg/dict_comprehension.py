# v={num: num**2 for num in [1,2,3,4,5,6]}
# print(v)

# str1= "ABC"
# str2="123"
# combo = {str1[i]: str2[i] for i in range(0,len(str1))}
# print(combo)

# dict_1 = {"name":"vishal","age":"five","gender":"male","mail":"abc@gmail.com","address":"vijayapur"}
# v = {k.upper():i.upper() for k,i in dict_1.items()}
# print(v)

# even or odd 

# v = {num : ("even" if num % 2==0 else "odd") for num in range(1,100)}
# print(v)

# answer = {char:0 for char in 'aeiou'} 
# print(answer)

answer = {count: chr(count) for count in range(65,91)} 
print(answer)