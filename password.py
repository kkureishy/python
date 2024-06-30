#main function
def main():
    password = "" #variable to hold password
    valid = False #variable to checks if password is valid
    lowercase = 0 #checks amount of lowercase characters
    uppercase = 0 #checks amount of uppercase characters
    number =0 # checks amount of numbers
    special =0 #checks amount of special characters
    
    #while password is not valid ask user for a valid password
    while valid == False:
        password = input("Input a password: ")
        #look though each character
        for char in password:
            #if a character is lowercase count
            if char.islower():
                lowercase += 1
            #if a character is uppercase count
            if char.isupper():
                uppercase+=1
            #if a character is a number count
            if char.isnumeric():
                number+=1
            #convert character to ascii value to check for specaial characters
            askey = ord(char)
            #if a character is special character count
            if (askey==33) or (askey>=35 and askey<=38) or (askey == 42) or (askey == 64):
                special +=1
        #if password is within length requirments at least one of each: lower case, uppercase, number, and special than password is valid
        if (len(password) >=8 and len(password) <=20) and (lowercase >=1) and (uppercase>=1) and (number>=1) and (special>=1):
            print("Valid Password")
            valid = True
        #if not notify user
        else:
            print("Invalid password")
    
    #set validity to false again
    valid = False
    pass2 = ""
    #user has to input password to be same as earlier password
    while valid == False:
        pass2= input("Enter password again to confirm: ")
        #if equal password confirmed
        if pass2 == password:
            print("Password confirmed")
            valid=True
        #if not password needs to match
        else:
            print("Please enter password again")
main()