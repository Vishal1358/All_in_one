# class Age(Exception):
#     pass

# def insurance():
#     age = input()
#     # try:
#     if (age.isnumeric() != True) and (age < 17) and (age > 61) :
#         raise Age("Your age is less than or greate than value")
#     return "You are eligibal for insurance"
#     # except:
#     #     if age.isnumeric():
#     #         return ("Your age is less than or greate than value")
#     #     else:
#     #         return ("Enter a valid age")

# class RaiseException(Exception):
#     pass

# def is_eligible(age):
#     if isinstance(age, int) and (age > 17) and (age < 61):
#         return True
#     else:
#         return False
        
# def checking_age(age):
#     if is_eligible(age):
#         return "You are eligibal for insurance"
#     raise RaiseException("Your age is less than or greate than value")

# A = input()
# print(checking_age(A))

class InvalidMarks(Exception):
    pass

marks = int(input("Enter Marks for student: "))
try:
    if marks >= 0 and marks <= 100:
        print("It is a valid marks")
    else:
        raise InvalidMarks
except InvalidMarks:
    print("Marks should be in between 0 to 100")