# Contact Book with Exception Handling
# Implements add, delete, update, and list functionalities with detailed exception handling.

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a contact, ensuring no duplicates."""
        if self._find_contact(name):
            print("Error: Contact already exists.")
            return
        if not name or not number:
            print("Error: Name and number are required.")
            return
        self.contacts.append(Contact(name, number))
        print("Contact added.")

    def _find_contact(self, name):
        """Internal method to find a contact by name."""
        return next((contact for contact in self.contacts if contact.name == name), None)

    def delete_contact(self, name):
        """Delete a contact by name, if it exists."""
        contact = self._find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted.")
        else:
            print("Error: Contact not found.")

    def update_contact(self, name, number):
        """Update a contact's number, if the contact exists."""
        contact = self._find_contact(name)
        if contact:
            contact.number = number
            print("Contact updated.")
        else:
            print("Error: Contact not found.")

    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact)

# Example usage
book = ContactBook()
book.add_contact('Jane Doe', '9876543210')
book.list_contacts()
