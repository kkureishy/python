bottle = 100
while bottle >0:
    if bottle ==2:
        print(str(bottle) + " bottles of beer on the wall")
        print(str(bottle) + " bottles of beer\nTake one down, pass it around")
        bottle+=-1
        print(str(bottle) + " bottle of beer on the wall!")
        print("")
    elif bottle == 1:
        print(str(bottle) + " bottle of beer on the wall")
        print(str(bottle) + " bottle of beer\ntake it down, pass it around")
        bottle+=-1
        print("No bottles of beer on the wall!")
        print("")
    else:
        print(str(bottle) + " bottles of beer on the wall")
        print(str(bottle) + " bottles of beer\nTake one down, pass it around")
        bottle+=-1
        print(str(bottle) + " bottles of beer on the wall!")
        print("")
