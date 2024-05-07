
contacts = [{'name': 'John Doe', 'number': '1234567890'}]

def search_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            print(contact)
            break

search_contact('John Doe')
