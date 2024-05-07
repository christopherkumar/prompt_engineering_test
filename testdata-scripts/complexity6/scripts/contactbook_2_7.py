# Basic contact update functionality with some checks

contacts = {'John Doe': '1234567890'}

def update_contact(name, new_number):
    if name in contacts:
        contacts[name] = new_number
        print("Contact updated")
    else:
        print("Contact not found")

updatecontact('John Doe', '0987654321')
print(contacts)
