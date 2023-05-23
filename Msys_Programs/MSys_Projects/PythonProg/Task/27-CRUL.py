simulated = ['CCRLU', 'CRLCUC', 'CCCC']
avl = 0
nc = 0
for i in simulated:
    for j in i:
        if j == "C" :
            if avl == 0 :
                nc += 1
            else:
                avl += 1
        elif j == "R":
            avl -= 1
        elif j == "L":
            avl -= 1
        elif j == "U":
            avl += 1
    print(nc)

    nc = 0
    avl = 0