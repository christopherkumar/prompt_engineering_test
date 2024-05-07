# Contact book

contacts = []

def add_contact():
    """Add a contact to the contact list"""
    name = input("Name: ")
    number = input("Number: ")
    contacts.append({'name': name, 'number': number})
    print("Added contact")

def show_contacts():
    """Display all contacts"""
    if contacts:
        for contact in contacts:
            print(f"{contact['name']}: {contact['number']}")
    else:
        print("No contacts available"

add_contact()
show_contacts()
