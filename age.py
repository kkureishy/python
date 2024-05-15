#ask user for age
age = int(input("How old are you? "))
print("\n")
#determine is user is old enough to drive
if age >=16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")
#determine is user is old enough to vote
if age >= 18:
    print("You can vote.")
else:
    print("You can not vote.")
#determine is user is old enough to buy alchol
if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You can not buy alcohol legally.")
#determine is user is old enough for senior discount
if age >= 65:
    print("You are eligible for the senior discount.")
else:
    print("You are not eligible for the senior discount.")