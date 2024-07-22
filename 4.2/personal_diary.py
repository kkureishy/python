#main function
def main():
    #run program 3 times
    for i in range (3):
        #user inputs date, time, and diary entry
        date = input("Enter the date and time: ")
        diary = input("Diary Entry: ")
        print("")
        #open/create diary and write date and diary entry into it. then close diary
        with open('diary.txt', 'w') as file:
            file.write(f"{date}\n\n{diary}")
            file.close()   
        try: #try to open the diary and read it
            # Open the file in read mode
            read = open('diary.txt', 'r')
            # Read file content
            content = read.read()
            print(content)
            read.close()  # Always close the file
        #file not found notify user
        except FileNotFoundError:
            print("File not found.")
        #if error occured let user know
        except Exception as e:
            print("An error occurred:", e)
        print("")
main()
