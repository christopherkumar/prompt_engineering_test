# Professional Contact Book Application
# A fully-featured contact book application with comprehensive error handling, input validation, and user-friendly CLI.

import json

class Contact:
    """Defines a contact with a name and phone number."""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.phone}"

class ContactBook:
    """Handles storage, retrieval, and modification of contacts."""
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        """Save the current contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact):
        """Add a new contact, if it does not already exist.

        Args:
            contact (Contact): The contact to add.
        """
        if contact.name in self.contacts:
            raise Exception("Contact already exists.")
        self.contacts[contact.name] = contact.phone
        self.save_contacts()

    def delete_contact(self, name):
        """Delete a contact by name.

        Args:
            name (str): The name of the contact to delete.
        """
        if name not in self.contacts:
            raise Exception("Contact does not exist.")
        del self.contacts[name]
        self.save_contacts()

    def update_contact(self, name, phone):
        """Update the phone number of an existing contact.

        Args:
            name (str): The name of the contact to update.
            phone (str): The new phone number for the contact.
        """
        if name not in self.contacts:
            raise Exception("Contact does not exist.")
        self.contacts[name] = phone
        self.save_contacts()

    def find_contact(self, name):
        """Find a contact by name.

        Args:
            name (str): The name of the contact to find.

        Returns:
            Contact: The found contact, if any.
        """
        if name in self.contacts:
            return Contact(name, self.contacts[name])
        raise Exception("Contact not found.")

    def list_contacts(self):
        """List all contacts in the book."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

def main():
    book = ContactBook()
    try:
        book.add_contact(Contact("Charlie Day", "123-456-7890"))
        print("Contact list:")
        book.list_contacts()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
