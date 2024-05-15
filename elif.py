#ask user for numeric grade
gradeNum = int(input("Enter the numeric grade: "))
gradeLetter = ""
if (gradeNum >= 0) and (gradeNum<=100):     
    if gradeNum>= 90:
        gradeLetter = "A"
    elif gradeNum>=80:
      gradeLetter = "B"
    elif gradeNum >= 70:
        gradeLetter = "C"
    elif gradeNum >= 60:
        gradeLetter = "D"
    else:
        gradeLetter = "F"
    print("The letter grade is: " + gradeLetter)
else:
    print("Numeric grade not in range.")    