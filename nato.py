#dictionary of the nato alphabet with all the nato letters
nato_alphabet = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliette", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", 
"S": "Sierra", 
"T": "Tango", 
"U": "Uniform", 
"V": "Victor", 
"W": "Whiskey", 
"X": "X-Ray", 
"Y": "Yankee", 
"Z": "Zulu", 
}
#fucnction to spell word using nato
def spell_word():
    #user inputs word
    user_word = input("Enter a  word: ")
    #word converted to uppercase
    x = user_word.upper()
    #loop through each letter in word and print the nato word the corresponds with the letter
    for letter in x:
        print(nato_alphabet[letter])
#main function
def main():
    #call spell word function
    spell_word()
#call main function
main()