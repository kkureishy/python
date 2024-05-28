print("")
#get list of all 20 seats
available = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#display seats
print("Available seats: " + str(available))
print("")
#set input variable to 1 because 0 would cause while loop to end
choice = 1
#while choice != 0: #while choice not 0 user inputs a number to purchase a ticket seat
for x in range(len(available)):
    choice = int(input("Select a seat by entering its number.\nTo finish purchase enter 0.\nEnter number: ")) #user imputs seat number
    i=choice
    if choice == 0:
        break
    if ((choice<0) or (choice>20)): # if user choice outside of range(1-20) print seat doesn't exist
        print("\nThat seat doesn't exist. Try again.")
    else: #if choice in range and is available remove the seat
        if i in available:
            available.remove(choice)
        else: # if seat is not available notify user
            print("\nThat seat has already been sold.")
    print("")
    if not available: #if all seats are gone print no more available seats
        print("No more available seats.")
        break
    print("Available seats: " + str(available)) # print all available seats
    print("")