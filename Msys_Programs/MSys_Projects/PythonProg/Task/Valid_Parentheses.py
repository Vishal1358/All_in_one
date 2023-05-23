# class Solution:
#     def isValid(self, s):
#         stack = []
#         for c in list(s):
#             if c in ["(", "[", "{"]:
#                 stack.append(c)
#             else:
#                 if len(stack) <= 0 or not stack.pop() + c in ["()", "[]", "{}"]:
#                     return False
#         return len(stack) == 0
    
# o = Solution()
# print(o.isValid("{}"))

# class Solution:
#     def isValid(self, s: string) -> bool:
#         while '()' in s or '[]'in s or '{}' in s:
#             s = s.replace('()','').replace('[]','').replace('{}','')
#         return False if len(s) !=0 else True
    
# o = Solution()
# s = input("Enter the string to check: ")
# print(o.isValid(s))

# class Solution:
#     def isValid(self, s: string) -> None:
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('()', '').replace('[]', '').replace('{}', '')
#         if len(s) != 0:
#             print("Invalid brackets!")
#         else:
#             print("Valid brackets!")

# Par = Solution()
# user = input("enter a elements: ")
# Par.isValid(user)





# class ParenthesesChecker:
#     def is_valid(self, s: string) -> bool:
#         # Create an empty stack to store the opening brackets
#         stack = []
        
#         # Loop through each character in the string
#         for bracket in s:
#             # If the character is an opening bracket, push it onto the stack
#             if bracket in ['(', '{', '[']:
#                 stack.append(bracket)
#             else:
#                 # If the character is a closing bracket, check if the stack is empty
#                 if not stack:
#                     # If the stack is empty, there is no matching opening bracket, so the string is invalid
#                     return False
                
#                 # If the stack is not empty, compare the closing bracket to the top of the stack
#                 if bracket == ')' and stack[-1] == '(':
#                     # If the closing bracket matches the top of the stack, pop the opening bracket off the stack
#                     stack.pop()
#                 elif bracket == '}' and stack[-1] == '{':
#                     stack.pop()
#                 elif bracket == ']' and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     # If the closing bracket does not match the top of the stack, the string is invalid
#                     return False
        
#         # If the loop completes without returning False, the string is valid if and only if the stack is empty
#         return not stack
    
    
# ca = ParenthesesChecker()
# print(ca.is_valid("{{{{}}}}"))




# class ValidParentheses:
#     def __init__(self, s):
#         self.s = s

#     def is_valid(self):
#         stack = []
#         brackets = {')': '(', '}': '{', ']': '['}
#         for c in self.s:
#             if c in brackets.values():
#                 stack.append(c)
#             elif c in brackets.keys():
#                 if not stack or stack.pop() != brackets[c]:
#                     return False
#         return not stack

# vp = ValidParentheses("{{{}}}")
# print(vp.is_valid())

# def isValid(s):
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('()', '').replace('[]', '').replace('{}', '')
#         if len(s) != 0:
#             print("Invalid brackets!")
#         else:
#             print("Valid brackets!")
# user = input("enter a elements: ")
# a = isValid(user)

# def validParanrhisis(string):
#     stack = []
#     for i in string:
#         if i in "([{":
#             stack.append(i)
#         else:
#             if stack[-1]+1 in ["()","[]","{}"]:
#                 stack.pop()
#             else:
#                 return False
#     if len(stack) == 0:
#         return True
#     return False

# string = input()

# resu = validParanrhisis(string)

# if resu:
#     print(f"{string} --->valid")
# else:
#     print(f"{string} --->notvalid")




def validParanthesis(string):
    stack = []
    for i in string: 
        if i in "([{":
            stack.append(i)
        else:
            if stack[-1]+i in ['()','[]','{}']:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False
    
string = input("Enter the string: ")
result = validParanthesis (string)

if result:
    print("{string} ----> valid paranthisis")
else:
    print("{string} --> not a valid paranthisis")