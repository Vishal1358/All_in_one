# try:
# except:
# else:
# finally:

while True:
    try:
        num = int(input("plaese enter a number: "))
    except:
        print("That's not a number")
    else:
        print("GOOD JOB YOU ENTERED A NUMBER")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")


# try:
#     num = int(input("plaese enter a number: "))
# except:
#     print("That's not a number")
# else:
#     print("I'M IN THE ELSE")
# finally:
#     print("RUNS NO MATTER WHAT!")