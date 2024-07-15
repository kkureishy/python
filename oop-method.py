# Class definition
class Pet:
    # Class variable
    vet_name = "Dr. Robotnik"

    def __init__(self, kind, breed, name):
        # Instance variables
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter for kind
    def get_kind(self):
        return self.__kind
    
    # Getter for breed
    def get_breed(self):
        return self.__breed

    # Getter for name    
    def get_name(self):
        return self.__name
    
    # Setter for kind
    def set_kind(self, value):
        self.__kind = value
    
    # Setter for breed
    def set_breed(self, value):
        self.__breed = value

    # Setter for name
    def set_name(self, value):
        self.__name = value
    
    # Method to print basic info about the pet
    def print_details(self):
        print(f"Pet Kind: {self.__kind}")
        print(f"Pet Breed: {self.__breed}")
        print(f"Pet Name: {self.__name}")
        print("")

# Main function to demonstrate usage of the pet class
def main():
    # Creating an instance of pet
    pet1 = Pet("Dog", "Alien", "Lockjaw")
    pet2 = Pet("Cat", "Orange", "Greeny")
    pet3 = Pet("Goat", "Mountain", "LeGoat")
    
    print("\n\n\n")
    
    #call details of pet
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()   
    print("\n\n\n")

    #try to determine if the attribute exists
    try:
        print(pet1.__name__)
    except AttributeError:
        print("Attribute does not exist")

# Calling the main function
main()