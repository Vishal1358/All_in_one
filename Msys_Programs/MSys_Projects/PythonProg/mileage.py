age = input("how old are you: ")
if age != "":
	if int(age) >= 18 and int(age) < 21:
		print("You can enter, but need a wristband!")
	elif int(age) >= 21:
		print ("You are good to enter and can drink!")
	else:
		print("you can't came in, little one! : (")
else:
	print("Pleasw enter an age!")