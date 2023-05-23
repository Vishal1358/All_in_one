def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return (arr[mid], mid)

    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_element = 8

result = binary_search(my_list, search_element)

if result:
    print(f"Element {result[0]} found at index {result[1]}.")
else:
    print("Element not found.")
