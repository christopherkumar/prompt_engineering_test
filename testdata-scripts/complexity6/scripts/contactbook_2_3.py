# Update a contact's number

contacts = [{'name': 'John Doe', 'number': '1234567890'}]

def update_contact(name, new_number):
    for contact in contacts:
        if contact['name'] == name:
            contact['number'] = new_number
            print(f"Updated contact: {name}")

update_contact('John Doe', '0987654321')
printf(contacts)
