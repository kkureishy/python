#global variables for height and weight conversion (1 pound = 0.453592 kilograms) (1 inch = 0.0254 meters)
CONVERSIONWEIGHT = 0.453592
CONVERSIONHEIGHT = 0.0254
#function to caluclate bmi with height and weight as paramters
def bmi(w,h):
    #converting lbs and inches to kg and m
    w = w*CONVERSIONWEIGHT
    h = h * CONVERSIONHEIGHT
    #bmi formula
    formula = w / (h**2)
    #display bmi to user
    print(f"Your BMI is: {formula:,.2f}")
    #bmi categories
    if formula >= 30: # if bmi greater than or equal to 30 than obese
        print("You are in the obese category")
    elif (formula >= 25) and (formula <29.9): # if bmi greater than or equal to 25 and less than 29.9 than overweight
        print("You are in the overweight category")
    elif (formula >= 18.5) and (formula < 24.9): #if bmi greater than or equal to 18.5 and less than 24.9 than normal weight
        print("You are in the normal weight category")
    else: #everything else is underweight
        print("You are in the underweight category")
#outside of function user inputs height and weight
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter yor height in inches: "))
# function then called
bmi(weight,height)