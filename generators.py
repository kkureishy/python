#two letter combination function
def two_letter_combinations(list, length):
    #if letter combination is 0 output empty array
    if length == 0:
        yield []#returns empty array to funciton
    #if letter combination is longer than list of characters leave funciton
    elif length > len(list):
        return
    #all else print 2 letter combination
    else:
        #loop the lenght of the list amount of times
        for i in range(len(list)):
            #hold the current charcter in the list
            currentCharacter = list[i]
            #hold remaining characters
            remiaing = list[i+1:]
            #with the remaining characters, and one less length print current character plus next character
            for j in two_letter_combinations(remiaing, length-1):
                yield [currentCharacter] + j #returns current character + the next character and then current + next next character in the next loop and so on, to function

#main function
def main():
    #empty array
    letterList = []
    #have user input 5 characters
    try:
        for i in range(5):
            character = input("Enter a character: ")
            letterList.append(character)
        #sort list and print
        letterList.sort()
        print(letterList)
        #call two letter comb function and print each combination
        for i in two_letter_combinations(letterList, 2):
            print(i)
    except Exception as e:
        print(f"An error occured: {e}")

#call main funciton
main()