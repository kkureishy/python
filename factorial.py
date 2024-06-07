#function to calculate factorial with paramter for number inputed
def factorial(n):
    #if 1 or 0 inputed than factorial is 1
    if (n==1) or (n==0):
        return 1
    #anything else normal factorial calculation
    else:
        #using recursive number is multiplied to call of itself-1 
        return n * factorial(n-1)
#main function
def main():
    #user inputes a non negativ whole number
    x = int(input("Enter a non-negative integer: "))
    #factorial function called
    result = factorial(x)
    #factorial of number is displayed
    print(f"The factorial of {x} is {result}.")
#main function called
main()
     
