def right_rotate(lst, n):
    return lst[-n:] + lst[:-n]

lst = [10, 20, 30, 40, 50, 60, 70]
n = 6
lst[-n:] + lst[:n]
rotated_list = right_rotate(lst, n)
print(rotated_list)  # Output: [50, 60, 70, 10, 20, 30, 40]
