# Contact book with search functionality and basic console interface

contacts = {}

def add_contact():
    name = input("Enter the name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    number = input("Enter the number: ")
    contacts[name] = number
    print("Contact added.")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Contact found: {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    while True:
        choice = input("1: Add contact, 2: Search contact, 3: Exit: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            break
        else:
            print("Invalid option.")

main()
