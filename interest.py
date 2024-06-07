#function to calculate interest with 3 paramters
def calculate_interest(principal, rate, time):
    #using 3 paramters interest is calulated and returned
    simpleInterest = (principal * rate * time)/100
    return simpleInterest
#outside of funciton user inputs information for each of the 3 paramters
prin = int(input("Enter principal amount: "))
rat = int(input("Enter rate: "))
tim = int(input("Enter time: "))
#interest is called
result = calculate_interest(prin, rat, tim)
#the paramters and calulated interest is printed out
print(f"The simple interest for a principal amount of ${prin:,.2f} at an interest rate of {rat}% over a period of {tim} years is: ${result:,.2f}")
