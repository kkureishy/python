#importing random and math module to get random number and absolute value functions
import math
from random import random, randrange, randint

#generate random number
x = randrange(1, 101)
#print(x)

#main funciton
def main():
    #variable for the number the user guesses
    guess = 0
    #caculate difference between guess and actual number
    difference = 0
    #as long as the user doesn't guess random number continue to guess 
    while guess != x:
        #user should only guess an integer
        try:
            guess = int(input("Guess the random number between 1 and 100: "))
        #if not ask user to enter an integer
        except ValueError:
            print("Enter an integer.")
        #if user enters an integer then game continues
        else:
            #finding the absolute difference between guess and actual number
            difference = abs(guess - x)
            #if guess corectly let user know
            if difference == 0:
                print("You guess correctly")
            #if guess within 5 say very hot
            elif difference <= 5:
                print("Very Hot")
            #if guess within 5 say hot
            elif difference <= 15:
                print("Hot")
            #if guess within 5 say cool
            elif difference < 25:
                print("Cool")
            #if guess within 5 say cold
            else:
                print("Cold")

#run main
main()
