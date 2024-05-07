# Fully Featured Contact Book
# Implements a contact book with complete CRUD operations, search functionality, and data persistence.

import json

class Contact:
    """Class representing a contact with name and number."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Contact(Name: {self.name}, Number: {self.number})"

class ContactBook:
    """Class managing a collection of contacts with various operations."""
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """Load contacts from a JSON file, returning a dictionary."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_contacts(self):
        """Save the current state of contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, number):
        """Add a new contact to the book, ensuring no duplicates."""
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = number
        self._save_contacts()

    def remove_contact(self, name):
        """Remove a contact by name, if it exists."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        self._save_contacts()

    def update_contact(self, name, number):
        """Update the number of an existing contact."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name] = number
        self._save_contacts()

    def search_contact(self, name):
        """Search for a contact by name and return it."""
        if name in self.contacts:
            return Contact(name, self.contacts[name])
        raise ValueError("Contact not found.")

    def list_contacts(self):
        """Print all stored contacts."""
        if not self.contacts:
            print("No contacts available.")
            return
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

# Example usage
def run():
    book = ContactBook()
    try:
        book.add_contact("Frank Reynolds", "321-654-9870")
        print("All contacts:")
        book.list_contacts()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    run()
