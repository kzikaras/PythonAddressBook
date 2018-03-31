
# Define global variables
contactList = []
choice = ""
keepGoing = "yes"
file = open("file.txt", "r+")

# Create a class for contacts
class Contact:
    def __init__(self, firstName, lastName, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone

#define a function to create a new contact
def createContact(first, last, phoneNumber):
    title = Contact(first,last,phoneNumber)
    contactList.append(title)

#define a function to print all contacts
def printContacts():
    for contact in contactList:
        print("First Name: " + contact.firstName)
        print("Last Name: " + contact.lastName)
        print("Phone Number: " + contact.phone)


# prompt user for input
def printMenu():
    userChoice = ""
    print("Select a number:")
    print("1. Add a new contact")
    print("2. Display contacts")
    print("3. Write to file")
    userChoice = input()
    return userChoice

# Main program
while keepGoing == "yes":
    choice = printMenu()
    
    if choice == "1":
        print("Enter the information")
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        phone = input("Enter phone number: ")
        createContact(firstName, lastName, phone)
    elif choice == "2":
        printContacts()
    elif choice == "3":
        for contact in contactList:
            file.write("First Name: " + contact.firstName)
            file.write("Last Name: " + contact.lastName)
            file.write("Phone Number: " + contact.phone)


    keepGoing = input("Keep going? type yes or no: ")



