#create lists of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#empty variable for steps and total steps
steps = []
total = 0
#loop to to ask user how many steps they took on each day
#add steps to the the steps list
#add up steps for total
for i in range(len(days)):
    day = days[i]
    step = (input("How many steps did you take on " + day + " "))
    steps.append(step)
    total += int(step)
print("")
#loop print amount of steps taken on each day
for i in range(len(days)):
    day = days[i]
    step = steps[i]
    print("You took " + step + " steps on " + day)
#print total steps
print("Total steps: " + str(total))
#calculate and print average steps
average = round(total / len(steps))
print("Average steps: " + str(average))