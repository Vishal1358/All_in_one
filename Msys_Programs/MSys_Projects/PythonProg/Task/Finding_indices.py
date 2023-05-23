# s = input()  # read the string S
# k = input()  # read the string k

# start_index = s.find(k)  # find the starting index of k in s

# if start_index == -1:
#     print((-1, -1))  # k not found, print (-1, -1)
# else:
#     end_index = start_index + len(k) - 1  # calculate the end index of k
#     print((start_index, end_index))  # print the tuple (start_index, end_index)

# S = input()
# k = input()

# start = S.find(k)
# end = start + len(k) - 1

# if start == -1:
#     print((-1, -1))
# else:
#     print((start, end))

# S = input().strip()
# k = input().strip()

# start_index = S.find(k)
# if start_index == -1:
#     print((-1, -1))
# else:
#     end_index = start_index + len(k) - 1
#     print((start_index, end_index))


S = input("Enter string S: ")
k = input("Enter string k: ")

start_index = S.find(k)
if start_index == -1:
    print((-1, -1))
else:
    end_index = start_index + len(k) - 1
    print((start_index, end_index))
    while True:
        start_index = S.find(k, start_index + 1)
        if start_index == -1:
            break
        end_index = start_index + len(k) - 1
        print((start_index, end_index))

