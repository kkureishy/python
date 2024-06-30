#main function
def main():
    #ask the user for one character
    user_input = input("Enter a character: ")
    #if user inputs more than one character continue to ask
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    #convert character to ascii value
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")
#run main()
main()