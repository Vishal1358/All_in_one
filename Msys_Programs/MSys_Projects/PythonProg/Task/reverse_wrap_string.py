# def reverse_wrap_string(s, width):
#     s = s.replace(" ", "")
#     s = s[::-1]
    
#     lines = []
#     for i in range(0, len(s)+1, width):
#         lines.append(s[i:i+width])
    
#     #return "\n".join(lines[::-1])
#     print(lines[::-1])

s = "Hello, welcome to this organisation."
width = 3
# result = reverse_wrap_string(s, width)
# print(result)

s = s.replace(" ", "")
for i in range(0, len(s), width):
   print((s[i:i+width])[::-1])