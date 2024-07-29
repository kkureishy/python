#import datetime and calender modules
import datetime
from datetime import datetime
import calendar

#main funciton
def main():
    #try to get current year and birth month from user and print calender
    try:
        #using datetime fucntion get current year
        year = datetime.now().year
        #print year
        print(f"Year: {year}")
        #get birth month # from user
        month = int(input("Enter your birth month: "))
        #if month number not real let user know
        if (month <1) or (month>12):
            print("Month number must be 1-12")
        #using calnder function print calender for birth month in current year
        print(calendar.month(year, month))

    #if error notify user
    except Exception as e:
        print(f"Something went wrong: {e}")

main()