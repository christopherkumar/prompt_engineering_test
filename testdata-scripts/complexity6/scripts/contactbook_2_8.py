contacts = {'John Doe': '1234567890'}

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")

delete_contact('Jane Doe'))