# Class definition for a Person
class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    # Setter for name
    def set_name(self,name):
        self.__name = name
    # Setter for address
    def set_address(self, address):
        self.__address = address
    # Setter for age
    def set_age(self, age):
        self.__age = age
    # Setter for phone
    def set_phone(self, phone):
        self.__phone = phone
    # Getter for name
    def get_name(self):
        return self.__name
    # Getter for address
    def get_address(self):
        return self.__address
    # Getter for age
    def get_age(self):
        return self.__age
    # Getter for phone
    def get_phone(self):
        return self.phone
    # Method to get person's info as a formatted string
    def get_info(self):
        return f"Name: {self.__name}\nAddress: {self.__address}\nAge: {self.__age}\nPhone: {self.__phone}\n"

#main function
def main():
    #create 3 different instances for 3 different people
    person1 = Person("Kalil Kureishy", "The Moon", "19", "410-882-0038")
    person2 = Person("LeCrusher Jamal Green III Jr", "6400 S King Dr, Chicago, Illinois", "15", "312-426-4782")
    person3 = Person("LeDaddy James", "9336 Civic Center Drive, Beverly Hills, CA", "39", "216-771-2323")
    #print the information for 3 different people
    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
#call main function
main()
