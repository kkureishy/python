#main function
def main():
    #array to hold sorted book titles.
    sorted = []
    #user inputs 10 books and gets added to list
    while len(sorted) != 10:
        title = str(input("Enter a book title: "))
        sorted.append(title)
    #sort list alphabetically
    sorted.sort()
    #print each item in the list with correct captilization
    for i in sorted:
        print(i.title())
main()
