# Modular Contact Book System
# Divides functionality into separate modules for better organization and maintenance.

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f"Contact(name={self.name}, number={self.number})"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a contact after ensuring it doesn't already exist."""
        if not any(c.name == name for c in self.contacts):
            self.contacts.append(Contact(name, number))
            print("Contact added.")
        else:
            print("Contact already exists.")

    def find_contact(self, name):
        """Find and return a contact by name."""
        return next((c for c in self.contacts if c.name == name), None)

    def update_contact(self, name, number):
        """Update a contact's number if it exists."""
        contact = self.find_contact(name)
        if contact:
            contact.number = number
            print("Contact updated.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        """Delete a contact by name if it exists."""
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """List all contacts."""
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts to display.")

# Example usage
book = ContactBook()
book.add_contact('Emily Clark', '4567890123')
book.list_contacts()
