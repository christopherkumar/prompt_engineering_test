# Comprehensive Contact Book with Advanced Functionality
# A complete contact management system with advanced functionality, input validation, error handling, and persistent storage.

import json

class Contact:
    """Defines a contact with name and number attributes."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactDirectory:
    """Manages a directory of contacts with functionality to add, update, remove, search, and list contacts."""
    def __init__(self, filepath='contacts.json'):
        self.filepath = filepath
        self.directory = self.load_directory()

    def load_directory(self):
        """Load the directory of contacts from a file."""
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_directory(self):
        """Save the current directory of contacts to a file."""
        with open(self.filepath, 'w') as file:
            json.dump(self.directory, file, indent=2)

    def add_contact(self, contact):
        """Add a contact to the directory after ensuring it doesn't already exist."""
        if contact.name in self.directory:
            raise ValueError("Contact already exists.")
        self.directory[contact.name] = contact.number
        self.save_directory()

    def update_contact(self, name, number):
        """Update an existing contact's number in the directory."""
        if name not in self.directory:
            raise ValueError("Contact not found.")
        self.directory[name] = number
        self.save_directory()

    def remove_contact(self, name):
        """Remove a contact from the directory."""
        if name not in self.directory:
            raise ValueError("Contact not found.")
        del self.directory[name]
        self.save_directory()

    def search_contact(self, name):
        """Search for a contact by name in the directory."""
        if name in self.directory:
            return Contact(name, self.directory[name])
        raise ValueError("Contact not found.")

    def list_contacts(self):
        """List all contacts in the directory."""
        if not self.directory:
            print("No contacts found.")
            return
        for name, number in self.directory.items():
            print(f"{name}: {number}")

# Demonstration of usage
def main():
    directory = ContactDirectory()
    try:
        directory.add_contact(Contact("Charlie Kelly", "123-456-7890"))
        directory.list_contacts()
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
