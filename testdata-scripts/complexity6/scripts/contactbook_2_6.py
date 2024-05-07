
def add_contact(contacts, name, number):
    contacts[name] = number

def list_contacts(contacts):
    for name, number in contacts.items():
        print(f"{name}: {numer}")

contacts = {}
add_contact(contacts, 'John Doe', '1234567890')
list_contacts(contacts)
