age = input("how old are you: ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        # 18-21 wristband
        print("You can enter, but need a wristband!")
    elif age >= 21:
        # 21+ drink, normal entry
        print ("You are good to enter and can drink!")
    else:
        # too young, sorry
        print("you can't came in, little one! : (")
else:
	print("Pleasw enter an age!")