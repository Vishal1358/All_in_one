def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if l[j] < l[position]:
                position = j
        temp = l[i]
        l[i] = l[position]
        l[position] = temp

def bubble_sort(l):
    n = len(l)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i+1], l[i]


l = [2,3,-5,-7,9,4,6,-1,-8,0]
# selection_sort(l)
bubble_sort(l)
print(l)

