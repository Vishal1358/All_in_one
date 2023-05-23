# for num in range(1,21):
#     if num == 4 or num == 13:
#         print (f"{num} is unlucky")

#     elif num % 2 == 0:
#         print(f"{num} is even")

#     else:
#         print(f"{num} is odd")

    


for num in range(1,21):
    if num == 4 or num == 13:
        state = "Unlucky"

    elif num % 2 == 0:
        state = "Even"
        

    else:
        state = "Odd"
    print(f"{num} is {state}")

    