#main function
def main():
    #empty flower list + empty flower string
    flowerList = []
    flower = ""
    #print number next flower starting at 1
    count =1
    #user inputs flower name until they press done and they stop
    while flower != "done":
        flower = (input("Enter flower name: "))
        flowerList.append(flower)
        flowerList.sort()
    #when done inputed need to be removed from list
    flowerList.remove("done")
    #print out flower name with capitalizartion and number before it
    for i in flowerList:
        print(str(count) + ". " + i.capitalize())
        count +=1
    #user inputs number
    #set random variable to be 0 to have infinetly running loop
    x=0
    while x==0:
        try: #try to have user input number to access flower
            number = int(input("Enter number to access flower: "))
        except ValueError: #if not integer let user know
            print("Invalid input")
        else:#if integer than subtract input by to get python index
            index = number -1
            try:#try to print flower at the index provided
                print(f"Flower found: {flowerList[index].capitalize()}")
            except (IndexError):#if index outside of range of list than let user know
                print("Invalid input")
            else:#if index valid than break out of loop
                break

#call main funciton
main()