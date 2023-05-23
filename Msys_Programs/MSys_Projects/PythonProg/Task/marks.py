marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:                        # checking wether user has sent valid input or not
    print("Invalid marks entered. Please enter marks between 0 and 100.")   # if its greater than       100 it will print the message
else:                                                           # otherwise it will check for Grades
    if marks >= 90:                                    # range in between (91-100) printing grade – A1
        grade = "A1"
    elif marks >= 81:                                # range in between (81-90) printing grade – A2
        grade = "A2"
    elif marks >= 71:                                # range in between (71-80) printing grade – B1
        grade = "B1"
    elif marks >= 61:                                # range in between (61-70)printing grade – B2
        grade = "B2"
    elif marks >= 51:                               # range in between (51-60) printing grade – C1
        grade = "C1"
    elif marks >= 40:                                # range in between (40-50) printing grade – C2
        grade = "C2"
    else:
        grade = "Fail"                              # less than 40 it will print "Fail"
        
    print("Your grade is:", grade)
