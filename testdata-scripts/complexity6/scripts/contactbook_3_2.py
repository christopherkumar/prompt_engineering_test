# Improved contact management with error handling and validation

contacts = []

def add_contact(name, number):
    if not name or not number:
        print("Name and number cannot be empty.")
        return
    if find_contact(name):
        print("Contact already exists.")
        return
    contacts.append({'name': name, 'number': number})

def find_contact(name):
    return next((contact for contact in contacts if contact['name'] == name), None)

def delete_contact(name):
    contact = find_contact(name)
    if contact:
        contacts.remove(contact)
    else:
        print("Contact not found.")

def list_contacts():
    for contact in contacts:
        print(f"{contact['name']} - {contact['number']}")

add_contact('John Doe', '1234567890')
list_contacts()
