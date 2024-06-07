#creating furnction for the song humpty dumpty with 8 paramters
def custom_song(firstName, lastName, verb, noun, adj, person1, animal, person2):
    for i in range(3): #the song repats itself 3 times 
        #priting out the song lyrics but the paramters are replaceing some of the lyrics using f strings
        print("\n\n")
        print(f"{firstName} {lastName} {verb} on a {noun}")
        print(f"{firstName} {lastName} had a {adj} fall")
        print(f"All the {person1}'s {animal} and all the {person1}'s {person2}")
        print(f"Couldn't put {firstName} together again")
#outside of fucntion user unputs something for each of the 8 variables
input_FN = input("Enter a first name: ")
input_LN = input("Enter a last name: ")
input_V = input("Enter a verb(past tense): ")
input_noun = input("Enter a noun: ")
input_adjective = input("Enter an adjective: ")
input_p1 = input("Enter a person: ")
input_animal = input("Enter an animal(plural): ")
input_p2 = input("Enter another person(plural): ")
#calling the function to create the song
custom_song(input_FN,input_LN,input_V,input_noun,input_adjective,input_p1,input_animal,input_p2)