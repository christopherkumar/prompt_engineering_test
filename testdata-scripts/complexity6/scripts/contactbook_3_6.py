# Contact book with improved error handling and user interaction

contacts = {}

def add_contact(name, number):
    if name in contacts:
        print("Contact already exists.")
        return
    contacts[name] = number
    print("Contact added.")

def remove_contact(name):
    if name not in contacts:
        print("Contact does not exist.")
        return
    del contacts[name]
    print("Contact removed.")

def print_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    for name, number in contacts.items():
        print(f"{name}: {number}")

def main():
    while True:
        command = input("Enter command (add, remove, list, quit): ")
        if command == 'add':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif command == 'remove':
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif command == 'list':
            print_contacts()
        elif command == 'quit':
            break
        else:
            print("Invalid command.")

main()
