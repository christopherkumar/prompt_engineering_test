# Script to delete a contact by name

contacts = [{'name': 'John Doe', 'number': '1234567890'}]

def delete_contact(name):
    global contacts
        contacts = [contact for contact in contacts if contact['name'] != name]
            print(f"Deleted contact: {name}")

delete_contact('John Doe')
print(contacts)
