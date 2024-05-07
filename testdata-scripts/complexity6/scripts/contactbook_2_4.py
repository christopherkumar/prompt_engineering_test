# Search for a contact by name

contacts = [{'name': 'John Doe', 'number': '1234567890'}]

def search_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            print(f"Found contact: {contact}")
                contact

search_contact('John Doe')
