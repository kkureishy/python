#start with bottles at 100
bottle = 100
#loop until all bottles are gone or 0
while bottle >0:
    #when amount of bottles get to 2 make sure the phrasing is grammatically correct (when at 1 bottle say 1 bottle of beer on the wall)
    if bottle ==2:
        print(str(bottle) + " bottles of beer on the wall")
        print(str(bottle) + " bottles of beer\nTake one down, pass it around")
        bottle+=-1 # subtract amount of bottles after taking one
        print(str(bottle) + " bottle of beer on the wall!")
        print("")
    #when amount of bottles get to 1 make sure the phrasing is grammatically correct (when at 1 bottle say 1 bottle of beer on the wall)
    elif bottle == 1:
        print(str(bottle) + " bottle of beer on the wall")
        print(str(bottle) + " bottle of beer\ntake it down, pass it around")
        bottle+=-1 # subtract amount of bottles after taking one
        print("No bottles of beer on the wall!")
        print("")
    #all else print phrase normally
    else:
        print(str(bottle) + " bottles of beer on the wall")
        print(str(bottle) + " bottles of beer\nTake one down, pass it around")
        bottle+=-1 # subtract amount of bottles after taking one
        print(str(bottle) + " bottles of beer on the wall!")
        print("")
