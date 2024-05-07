# Contact Book with File Storage
# This version of the contact book saves contacts to a file for persistence between program executions.

import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_contacts(self):
        """Save the current contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, number):
        """Add a new contact if it doesn't exist, then save to file."""
        if name in self.contacts:
            print("Contact already exists.")
            return
        self.contacts[name] = number
        self._save_contacts()
        print("Contact added and saved.")

    def delete_contact(self, name):
        """Delete a contact if it exists, then save changes."""
        if name in self.contacts:
            del self.contacts[name]
            self._save_contacts()
            print("Contact deleted and changes saved.")
        else:
            print("Contact not found.")

    def update_contact(self, name, number):
        """Update a contact's number if it exists, then save changes."""
        if name in self.contacts:
            self.contacts[name] = number
            self._save_contacts()
            print("Contact updated and saved.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts to display.")
            return
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

# Example usage
book = ContactBook()
book.add_contact('John Doe', '1234567890')
book.list_contacts()
