# Elegant Contact Book System
# A refined contact book system with optimized code structure, error handling, and file-based data persistence.

import json

class Contact:
    """A simple class for holding contact details."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactBook:
    """A class for managing contacts with operations for add, update, delete, and list."""
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return {name: Contact(name, number) for name, number in data.items()}
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump({contact.name: contact.number for contact in self.contacts.values()}, file, indent=4)

    def add_contact(self, name, number):
        """Add a new contact, ensuring no duplicate entries."""
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = Contact(name, number)
        self.save_contacts()

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        self.save_contacts()

    def update_contact(self, name, number):
        """Update an existing contact's number."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name].number = number
        self.save_contacts()

    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts to display.")
        for contact in self.contacts.values():
            print(contact)

# Example usage
def main():
    book = ContactBook()
    try:
        book.add_contact("Dee Reynolds", "123-987-6540")
        book.list_contacts()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
