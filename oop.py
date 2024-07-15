# Class definition
class Pet:
    # Class variable
    vet_name = "Dr. Robotnik"
    #private properties
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = "Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter for first_name
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    # Getter for last_name
    def get_owner_last_name(self):
        return self.__owner_last_name

    # Getter for pet_id    
    def get_pet_id(self):
        return self.__pet_id
   
    # Getter for pet_name
    def get_pet_name(self):
        return self.__pet_name

    # Getter for pet_type
    def get_pet_type(self):
        return self.__pet_type

    # Setter for first_name
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    # Setter for last_name
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    # Setter for pet_id  
    def set_pet_id(self, value):
        self.__pet_id = value
    
    # Setter for pet_name  
    def set_pet_name(self, value):
        self.__pet_name = value
    
    # Setter for pet_type
    def set_pet_type(self, value):
        self.__pet_type = value
    
    #verify if a property exists in a pet object
    def check_property(self, property):
        return hasattr(self, property)

    # # Method to print pet info
    def display_pet_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)

# Main function to demonstrate usage of the pet class
def main():
    # Creating an instance of pet
    pet1 = Pet("Kalil", "Kureishy", '009234', "Plunky")
    pet2 = Pet("George", "Carver", '123245', "Greeny", "Fish")
    pet3 = Pet("LeManager", "James", '230609', "LeGoat", "Goat")
    
    #calling setter for pet id
    pet1.set_pet_id("050505")
    print(pet1.get_pet_id())
    
    print("\n\n\n")
    
    #calling function display_pet_info()
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()   
    print("\n\n\n")
    
    #trying to see if a propert exists in class
    try:
        print(pet1.check_property("_Pet__owner_first_name"))
        

    except AttributeError:
        print("This property doesn't exist.")

# Calling the main function
main()