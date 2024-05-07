# Basic contact book script

contacts = []

def add_contact(name, number):
    contacts.append({'name': name, 'number': number})
    print(f"Contact added: {name}")

def list_contacts():
    print("Contacts list:")
    for contact in contacts:
        print(contact)
()
()
()
()
add_contact('John Doe', '1234567890')
list_contacts()
