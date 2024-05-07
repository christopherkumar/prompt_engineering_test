# Professional Contact Management System
# A robust and professional contact management system with full CRUD capabilities, validation, and persistent storage.

import json

class Contact:
    """Encapsulates contact details."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Contact(Name: {self.name}, Number: {self.number})"

class ContactManager:
    """Manages a collection of contacts with functionality to add, update, delete, and search contacts."""
    def __init__(self, filepath='contacts.json'):
        self.filepath = filepath
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """Load contacts from the specified JSON file."""
        try:
            with open(self.filepath) as file:
                contacts_dict = json.load(file)
                return {name: Contact(name, details['number']) for name, details in contacts_dict.items()}
        except FileNotFoundError:
            return {}

    def _save_contacts(self):
        """Save the current contacts to the JSON file."""
        with open(self.filepath, 'w') as file:
            json.dump({contact.name: {'number': contact.number} for contact in self.contacts.values()}, file, indent=4)

    def add_contact(self, name, number):
        """Add a new contact if it doesn't already exist."""
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = Contact(name, number)
        self._save_contacts()

    def update_contact(self, name, number):
        """Update the phone number of an existing contact."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        self.contacts[name].number = number
        self._save_contacts()

    def delete_contact(self, name):
        """Remove a contact by name."""
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        self._save_contacts()

    def search_contact(self, name):
        """Search for a contact by name."""
        return self.contacts.get(name, None)

    def list_contacts(self):
        """List all contacts."""
        for contact in self.contacts.values():
            print(contact)

# Example of usage
def main():
    manager = ContactManager()
    try:
        manager.add_contact("Mac McDonald", "321-654-9870")
        print("Contact list:")
        manager.list_contacts()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
