# Contact search with basic output formatting

contacts = {'John Doe': '1234567890'}

def search_contact(name):
    if name in contacts:
        print(f"Contact found: {name}, Number: {contacts[name]}")
    else:
        print("Contact not found")
main()
    search_contact('John Doe')
