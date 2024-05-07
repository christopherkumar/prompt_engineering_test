# Console-based contact book with navigation and error handling

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    if name in contacts:
        print("This contact already exists.")
        return
    number = input("Enter the phone number: ")
    contacts[name] = number
    print("Contact added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for name, number in contacts.items():
        print(f"{name}: {number}")

def main():
    contacts = {}
    while True:
        action = input("Choose an action (add, view, exit): ")
        if action == 'add':
            add_contact(contacts)
        elif action == 'view':
            view_contacts(contacts)
        elif action == 'exit':
            break
        else:
            print("Invalid option. Please choose 'add', 'view', or 'exit'.")

main()
