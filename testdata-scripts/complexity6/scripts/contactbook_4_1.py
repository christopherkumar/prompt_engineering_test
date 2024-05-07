# Advanced Contact Book implementation using classes
# Features: Add, delete, update, search, and list contacts

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a new contact if it doesn't already exist."""
        if self.find_contact(name) is None:
            self.contacts.append(Contact(name, number))
            print("Contact added.")
        else:
            print("Contact already exists.")

    def find_contact(self, name):
        """Return a contact by name."""
        return next((contact for contact in self.contacts if contact.name == name), None)

    def delete_contact(self, name):
        """Delete a contact by name."""
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def update_contact(self, name, number):
        """Update the number of an existing contact."""
        contact = self.find_contact(name)
        if contact:
            contact.number = number
            print("Contact updated.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(contact)

# Example usage
book = ContactBook()
book.add_contact('John Doe', '1234567890')
book.list_contacts()
