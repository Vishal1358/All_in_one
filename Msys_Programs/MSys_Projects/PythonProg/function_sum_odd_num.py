# sum of odd numbers code

# def sum_odd_num(number):
#     total = 0
#     for num in number:
#         if num % 2 != 0:
#             total += num
#     return total

# print(sum_odd_num([1,2,3,4,5,6,7,8,9]))


# check odd number

def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False
print(is_odd_number(5))
print(is_odd_number(4))
print(is_odd_number(3))
print(is_odd_number(199.99))