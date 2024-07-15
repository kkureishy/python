# Define a exception for non numeric inputs
class NotNumericError(Exception):
    def __init__(self, message):
        self.message = message

#function to see if number is numeric
def input_number(i):
        if i.isnumeric() == False:
            raise NotNumericError("Not numeric error occurred")    

# user trys to input number
x = 0
while x == 0:
    try:
        inp = (input("Enter a number: "))
        input_number(inp)
    #if not numeric let user know
    except NotNumericError as e:
        print(f"Caught an error: {e.message}")
        pass
    #at the end lend user know the program is over
    else:
         print(f"{inp}")
         x =2
    finally:
        if x ==0:
             pass
        else:
            print("Execution completed.")
            break
