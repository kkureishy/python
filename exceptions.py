# Simple Python program to calculate the square of a number
#function to calculated square of a number
def square_number():
    #user inputs a number to square
    number = input("Enter a number to square: ")
    #the number is trying to be being squared
    try:
        squared_number = int(number) ** 2
    except ValueError:
        #if non integer inputed causeing a ValueError than it prints number most be integer
        print("Number must be an integer.")
    else:
        #if no error than number and its square is displayed
        print(f"The square of {number} is {squared_number}.")
#call function
square_number()