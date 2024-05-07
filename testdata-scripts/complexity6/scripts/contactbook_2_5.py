# Basic contact book with simple input handling

contacts = []

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts.append({'name': name, 'number': number})
    print("Contact added")

def main():
    while True:
        choice = input("1: Add Contact, 2: Exit: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            break
        else:
            print("Invalid choice")

main();
