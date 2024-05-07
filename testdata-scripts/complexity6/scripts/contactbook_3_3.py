# Contact book with basic input validation and error handling

contacts = []

def add_contact():
    name = input("Enter name: ").strip()
    number = input("Enter number: ").strip()
    if not name or not number:
        print("Both name and number are required.")
        return
    contacts.append({'name': name, 'number': number})
    print("Contact added.")

def get_contact(name):
    return next((c for c in contacts if c['name'] == name), None)

def delete_contact():
    name = input("Enter name to delete: ").strip()
    contact = get_contact(name)
    if contact:
        contacts.remove(contact)
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        action = input("1: Add, 2: Delete, 3: Exit: ")
        if action == '1':
            add_contact()
        elif action == '2':
            delete_contact()
        elif action == '3':
            break
        else:
            print("Invalid option.")

main()
