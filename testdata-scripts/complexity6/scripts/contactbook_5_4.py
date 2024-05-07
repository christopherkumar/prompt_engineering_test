# Contact Book with Advanced Features
# An advanced contact book with search, edit, delete functionalities, and persistent storage.

import json

class Contact:
    """A class to represent a contact with name and phone number."""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"

class ContactBook:
    """A class to manage contacts with add, search, update, delete, and list functionalities."""
    def __init__(self, storage_file='contact_book.json'):
        self.storage_file = storage_file
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a file."""
        try:
            with open(self.storage_file, 'r') as f:
                return {name: Contact(name, phone) for name, phone in json.load(f).items()}
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        """Save the current contacts to a file."""
        with open(self.storage_file, 'w') as f:
            json.dump({contact.name: contact.phone for contact in self.contacts.values()}, f, indent=4)

    def add_contact(self, name, phone):
        """Add a new contact if not already present."""
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = Contact(name, phone)
        self.save_contacts()

    def find_contact(self, name):
        """Find and return a contact by name."""
        return self.contacts.get(name)

    def update_contact(self, name, phone):
        """Update an existing contact's phone number."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name] = Contact(name, phone)
        self.save_contacts()

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
        else:
            raise ValueError("Contact not found.")

    def list_contacts(self):
        """Print all the contacts."""
        for contact in self.contacts.values():
            print(contact)

# Example usage
def main():
    book = ContactBook()
    try:
        book.add_contact("Dennis Reynolds", "987-654-3210")
        book.list_contacts()
        book.update_contact("Dennis Reynolds", "654-321-0987")
        print("\nAfter update:")
        book.list_contacts()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
