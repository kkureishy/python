# Creating and using a Employee SuperClass 🐕
# and a ProductionWorker subclass 🐏🐏🐏
# along with instantiating (making objects)

class Employee:
    # Employee is a Superclass of the ProductionWorker class
    def __init__(self, name, number):
        #properties of employee
        self.name = name
        self.number = number
    
    #getter for name
    def get_name(self):
        return self.name
    
    #getter for number
    def get_number(self):
        return self.number
    
    #setter for name
    def set_name(self, value):
        self.name = value
    
    #setter for number
    def set_number(self, value):
        self.number = value

    #prints employee details
    def __str__(self):
        return f"Name: {self.name}\nEmployee Number: {self.number}"

#subclass of employee
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        #properties of productionworker
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate
    
    #Prints production worker details 
    def __str__(self):
        return super().__str__() + "\nShift: " + self.shift_number + "\nPay Rate: " + str(self.hourly_pay_rate)

    #getter for shift number
    def get_shift_number(self):
        return self.shift_number

    #getter for hourly pay
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
    
    #setter for shift number
    def set_shift_number(self, value):
        self.shift_number = value

    #setter for hourly pay
    def set_hourly_pay_rate(self, value):
        self.hourly_pay_rate = value   

#function to create production worker instance and print detials
def employeeData(n, nb, s, r):
    employee = ProductionWorker(n, nb, s, r)
    print(employee.__str__())

#main functions
def main():
    #empty string variable for shift
    message = ""
    #counter for priting data
    count = 0
    
    print("\n\n")
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    
    #user inputs employee name
    try:
        name = str(input("Enter Employee Name: "))
    except ValueError:
        print("Please enter a name only.")
    else:
        count +=1
    
    #user inputs emplyee number
    try:
        number = int(input("Enter Employee Number: "))
    except ValueError:
        print("Enter only the employee's number")
    else:
        count +=1
    
    #user inputs shift number
    try:
        shift = int(input("Enter Shift Number: "))
    except ValueError:
        print("Enter only the shift number")
    else: #if shift is 1 day if 2 night
        if shift ==1:
            message = "Day"
            count+=1
        elif shift == 2:
            message = "Night"
            count+=1
        else:
            message = "Invalid Shift Number"
    
    #user inputs pay rate
    try:
        rate = int(input("Enter Pay Rate: "))
    except ValueError:
        print("Enter only the pay rate number")
    else:
        count +=1
    
    #if all data inputed correctly print data
    if count == 4:
        print("Details of Employee:")
        print("-------------------------------------------------------")
        worker = employeeData(name, number, message, rate)
    #if not notify user
    else:
        print("User incorrectly inputed one or more data.")
    

main()