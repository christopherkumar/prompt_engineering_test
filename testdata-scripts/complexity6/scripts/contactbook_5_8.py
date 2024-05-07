# Feature-Rich Contact Book Application
# An application providing a comprehensive contact management system, featuring rich functionality including search, update, and deletion, with a clean and intuitive interface.

import json

class Contact:
    """Represents a contact with necessary details."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactBook:
    """A class to manage contact operations like add, search, update, and delete."""
    def __init__(self, file_name='contacts.json'):
        self.file_name = file_name
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """Load contacts from a file, returning a dictionary."""
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_contacts(self):
        """Save the current state of contacts to a file."""
        with open(self.file_name, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, number):
        """Add a new contact to the book, checking for duplicates."""
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = number
        self._save_contacts()

    def delete_contact(self, name):
        """Delete a contact from the book by name."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        self._save_contacts()

    def update_contact(self, name, number):
        """Update the contact's number in the book."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name] = number
        self._save_contacts()

    def find_contact(self, name):
        """Find and return contact details by name."""
        if name in self.contacts:
            return Contact(name, self.contacts[name])
        raise ValueError("Contact not found.")

    def list_contacts(self):
        """List all contacts in the book."""
        if not self.contacts:
            print("No contacts found.")
            return
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

# Example usage
def run():
    contact_book = ContactBook()
    try:
        contact_book.add_contact("Rickety Cricket", "987-123-4567")
        contact_book.list_contacts()
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    run()
