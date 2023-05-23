def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank You")
            break

test = ask_for_int()
print(test)