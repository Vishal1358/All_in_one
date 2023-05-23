# # a = int(input("how many number you want gave here: "))
# a = [78754546546,9995555999,8000025256]
# a.sort()
# no_list = []
# for i in a:
#     no_list.append("+91"+str(i))
# print(no_list)

def standardize_mobile_numbers(n):
    n.sort()
    n_list = []
    for i in n:
        n_list.append("+91"+str(i))
    return n_list

a = [7875454654,9995555999,8000025256]
print(standardize_mobile_numbers(a))