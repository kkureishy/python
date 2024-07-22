#main function
def main():
    #total amount of sales
    total = 0
    #count number of lines
    count = 0
    try: #try to open file
        # Open the file in read mode
        directory = open('/Users/kalilk/Python/PE2 4/4.3/sales_totals.txt', 'r')
        # Read file content
        for i in directory:
            #print each line
            print(f"${i}", end = "")
            #count tota;
            total += float(i)
            #count line
            count+=1
        directory.close()  # Always close the file
    #if file not found notify
    except FileNotFoundError:
        print("File not found.")
    #if exception error notify
    except Exception as e:
        print("An error occurred:", e)
    #if values non numerical notify
    except ValueError:
        print("Non numerical value found in the file.")
    #print total
    print(f"Total sales = ${total}")
    #print number of entries
    print(f"Number of entries: {count}")
    #calculate average and print
    avg = total/count
    print(f"Average: {avg}")
#call main function
main()