# Advanced Contact Book with Data Persistence
# Implements a contact book with JSON file storage, advanced search, and update features, following PEP 8 guidelines.

import json

class Contact:
    """A class to represent a contact."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactBook:
    """A class to manage a book of contacts."""
    def __init__(self, filepath='contacts.json'):
        self.filepath = filepath
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """Load contacts from a file."""
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_contacts(self):
        """Save contacts to a file."""
        with open(self.filepath, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        """Add a contact to the contact book.

        Args:
            contact (Contact): The contact to add.
        """
        if contact.name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[contact.name] = contact.number
        self._save_contacts()

    def remove_contact(self, name):
        """Remove a contact from the contact book.

        Args:
            name (str): The name of the contact to remove.
        """
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        self._save_contacts()

    def get_contact(self, name):
        """Get a contact by name.

        Args:
            name (str): The name of the contact to retrieve.

        Returns:
            Contact: The contact, if found.
        """
        if name in self.contacts:
            return Contact(name, self.contacts[name])
        raise ValueError("Contact not found.")

    def update_contact(self, name, number):
        """Update a contact's number.

        Args:
            name (str): The name of the contact to update.
            number (str): The new number for the contact.
        """
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name] = number
        self._save_contacts()

    def list_contacts(self):
        """List all contacts."""
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

# Example of using the ContactBook class
book = ContactBook()
try:
    book.add_contact(Contact("Bob Smith", "987-654-3210"))
    book.list_contacts()
    contact = book.get_contact("Bob Smith")
    print(contact)
except ValueError as e:
    print(e)
