# Optimized and User-Friendly Contact Book
# An optimized contact book with a user-friendly interface, supporting all CRUD operations, with efficient data storage and retrieval.

import json

class Contact:
    """Class to represent individual contact details."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactBook:
    """Class to manage a book of contacts with efficient and user-friendly operations."""
    def __init__(self, filename='contact_data.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, number):
        """Add a new contact to the book, ensuring no duplicates."""
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = number
        self.save_contacts()

    def delete_contact(self, name):
        """Delete a contact by name, ensuring it exists."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        self.save_contacts()

    def update_contact(self, name, number):
        """Update an existing contact's number."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name] = number
        self.save_contacts()

    def find_contact(self, name):
        """Find a contact by name and return it, if it exists."""
        number = self.contacts.get(name)
        if number:
            return Contact(name, number)
        raise ValueError("Contact not found.")

    def list_contacts(self):
        """List all contacts in the book."""
        if not self.contacts:
            print("No contacts available.")
            return
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

# Demonstration of usage
def main():
    book = ContactBook()
    try:
        book.add_contact("Artemis", "654-321-0987")
        book.list_contacts()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
