boolean = True
#ask user to input 2 distinct numbers
print("Input 2 distinct numbers:")
num1 = int(input())
num2 = int(input())
#check to see if both numbers are even
if((num1%2==0) and (num2%2==0)):
    boolean = True
else:
    boolean = False
print("Are both numbers even: " + str(boolean))
#check to see if one number is positive
if((num1>0) or (num2>0)):
    boolean = True
else:
    boolean = False
print("Is at least one number positive: " + str(boolean))
#Check to see if num1 is not 0.
if not num1==0:
    boolean = True
else:
    boolean = False
print("Is the first number not 0: " + str(boolean))
#Check to see if num2 is not 0.
if not num2==0:
    boolean = True
else:
    boolean = False
print("Is the second number not 0: " + str(boolean))
#Check to see if both numbers are greater than 100
if((num1>100) and (num2%2>100)):
    boolean = True
else:
    boolean = False
print("Are both numbers greater than 100: " + str(boolean))
#Check to see if at least one number is a multiple of 3
if((num1%3==0) or (num2%3==0)):
    boolean = True
else:
    boolean = False
print("Is at least one number a multiple of 3: " + str(boolean))
#Check to see if the first number is not divisble by 4
if not num1%4==0:
    boolean = True
else:
    boolean = False
print("Is the first number not a multiple of 4: " + str(boolean))


