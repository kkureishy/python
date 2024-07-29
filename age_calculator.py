#import datetime module
import datetime
from datetime import datetime

#main funciton
def main():
    #try to get users birthday and print in proper date format
    try:
        today = datetime.today() #get the date of today
        year = int(input("What year were you born: ")) # get users birthyear
        month = int(input("What month number were you born: ")) #get users birth month
        day = int(input("What day of the month were you born: ")) #get users day of birth month
        birthday = datetime(year, month, day) #create daytime object to hold date for birthday
        formatBirth = birthday.strftime("%Y-%m-%d") #format birthdate date as string
        print(formatBirth) # print birthday

        dayDiff = today - birthday # to get days from birthdate subtract from today
        yearDiff = dayDiff.days // 365.2425 #to get years from birthdate divide days by number of days in year
        monthDiff = dayDiff.days // 30.417 #to get months divide days by 30.417
        weekDiff = dayDiff.days // 7 # to get weeks divide days by 7
        hourDiff = dayDiff.days * 24 # to get hours multiple days by 24
        minuteDiff = hourDiff * 60 # to get minutes multiply hours by 60
        secondDiff = minuteDiff * 60 # to get seconds multiply minutes by 60
        #print age of user in years, months, weeks, days, hours, minutes, seconds
        print(f"You are {yearDiff} years , {monthDiff} months, {weekDiff} weeks, {dayDiff.days} days, {hourDiff} hours, {minuteDiff} minutes, and {secondDiff} seconds old.")

    #if an error accounted let user know
    except Exception as e:
        print(f"You entered the date in wrong: {e}") 
        #main()
    
#main function
main()