#list named time_slots with different times of the day
time_slots= ["Morning", "Midday", "Afternoon", "Evening"]
#empty list named heart_rates
heart_rates = []
#total heart rate initilized to 0
total = 0
#loop iterates over each element in the time_slots list
for time in time_slots:
    #each time of day, user to enter their heart rate converted to an integer and then stored in the heart rate list
    heartRate = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
    #total heart rate counted
    total += heartRate
    heart_rates.append([time,heartRate])
print(str(heart_rates))
#average heart rate calculated and displayed
average = total/4
print("Average heart rate today: " + str(average))
