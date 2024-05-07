# Interactive Command Line Contact Book
# Features a user-friendly command line interface to interact with the contact book.

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        if any(contact.name == name for contact in self.contacts):
            print("Contact already exists.")
        else:
            self.contacts.append(Contact(name, number))
            print("Contact added.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        contact = next((c for c in self.contacts if c.name == name), None)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def run(self):
        while True:
            command = input("Enter command (add, delete, list, quit): ")
            if command == 'add':
                self.add_contact()
            elif command == 'delete':
                self.delete_contact()
            elif command == 'list':
                self.list_contacts()
            elif command == 'quit':
                break
            else:
                print("Invalid command.")

# Example usage
book = ContactBook()
book.run()
