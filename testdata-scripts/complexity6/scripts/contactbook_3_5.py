# Contact book with basic CRUD operations and console interface

def create_contact(contacts, name, number):
    if name in contacts:
        print("Contact already exists.")
        return
    contacts[name] = number
    print("Contact added.")

def read_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, number in contacts.items():
        print(f"{name}: {number}")

def update_contact(contacts, name, number):
    if name in contacts:
        contacts[name] = number
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

contacts = {}
create_contact(contacts, 'John Doe', '1234567890')
read_contacts(contacts)
