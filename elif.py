#ask user for numeric grade
gradeNum = float(input("Enter the numeric grade: "))

gradeLetter = "" #empty string to hold grade letter
#check to see if numeric grade is in range of 0-100
if (gradeNum >= 0) and (gradeNum<=100):     
    #check to see if numeric grade is an A if it is greater than or equal 90
    if gradeNum>= 90:
        gradeLetter = "A"
    #check to see if numeric grade is an B if it is greater than or equal 80
    elif gradeNum>=80:
      gradeLetter = "B"
    #check to see if numeric grade is an C if it is greater than or equal 70
    elif gradeNum >= 70:
        gradeLetter = "C"
    #check to see if numeric grade is an D if it is greater than or equal 60
    elif gradeNum >= 60:
        gradeLetter = "D"
    #if not any other grade than letter is F
    else:
        gradeLetter = "F"
    #print the grade letter
    print("The letter grade is: " + gradeLetter)
#if not in range than print not in range
else:
    print("Numeric grade not in range.")    