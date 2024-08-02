#check the system
def check():
    print("Checking the system...")
    try:
        #open/create the file
        file = open("customer_list.txt", 'r')
        #read the file
        lines = file.readlines()
        #close the file
        file.close()
        #return the file
        return lines
    #if file does not exist let user know
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        print("")
        return []
 #create a new entry   
def create():
    print("Creating a new entry...")
    #check that file exists
    customer = check()
    #input customer info
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    #add customer
    customer.append(entry)
    #save customer info to file
    save(customer)

#save customer info
def save(output):
    #open file
    file = open("customer_list.txt", 'w')
    #in file write 
    for line in output:
        file.write(line)
    #close file
    file.close()
    print("File updated.")
    print("")

#read entry
def read():
    print("Reading an entry...")
    #check file
    customer = check()
    #input last name to find
    lname = input("Please enter the last name of the customer: ")
    found = False
    #look through list if lastname found print customer info
    #if not let user know
    for entry in customer:
        if lname in entry:
            print(entry)
            print("")
            found = True
            break
    if not found:
        print("No entry found.")
        print("")

def update():
    #check file
    customer = check()
    #input last name to update customer info
    lname = input("Please enter the last name of the customer to update: ")
    #update customer info
    for i, entry in enumerate(customer):
        if lname in entry:
            fname = input("Please enter the new first name: ")
            lname = input("Please enter the new last name: ")
            phone = input("Please enter the new phone: ")
            email = input("Please enter the new email: ")
            customer[i] = f"{fname}, {lname}, {phone}, {email}\n"
            break
    #save info
    save(customer)

def delete():
    print("Deleting an entry...")
    #check file
    customer = check()
    #input last name to delete customer
    lname = input("Please enter the last name of the customer to delete: ")
    new_customer = [entry for entry in customer if lname not in entry]
    save(new_customer)



def main_menu():
        print("")
        print("Menu:")
        while True:
            try:
                print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
                print("1. Create a new entry")
                print("2. Display an entry by last name")
                print("3. Update an existing entry")
                print("4. Remove an entry")
                print("5. Quit")
                choice = int(input("Please enter the number of your selection: "))
                print("")
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("That is not a valid number. Try again.")
            except ValueError:
                print("That is not a valid number. Try again.")
    
def main():
    while True:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice ==4:
            delete()
        elif choice ==5:
            print("Program Quitted")
            break

main()