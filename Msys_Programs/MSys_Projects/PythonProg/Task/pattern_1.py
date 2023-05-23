# n = 4 # number of rows

# # print upper half of the pattern
# for i in range(1, n+1):
#     for j in range(i, 1, -1):
#         print(j-1, end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# # print lower half of the pattern
# for i in range(n-1, 0, -1):
#     for j in range(i, 1, -1):
#         print(j-1, end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

n = 5  # number of rows

# upper half of the diamond
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()

# lower half of the diamond
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()
