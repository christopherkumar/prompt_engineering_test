# Contact Book with OOP Principles
# Implements a contact book using object-oriented programming principles, providing a clean and maintainable structure.

class Contact:
    """Represents a contact in the contact book."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name} ({self.number})"

class ContactBook:
    """Manages a collection of contacts."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a contact to the book, ensuring it does not already exist."""
        if not self._contact_exists(name):
            self.contacts.append(Contact(name, number))
            print("Contact added.")
        else:
            print("Contact already exists.")

    def _contact_exists(self, name):
        """Check if a contact exists in the book by name."""
        return any(contact.name == name for contact in self.contacts)

    def find_contact(self, name):
        """Find and return a contact by name."""
        return next((contact for contact in self.contacts if contact.name == name), None)

    def update_contact(self, name, new_number):
        """Update the number of an existing contact."""
        contact = self.find_contact(name)
        if contact:
            contact.number = new_number
            print("Contact updated.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        """Delete a contact from the book by name."""
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """Display all contacts in the book."""
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact)

# Example usage
book = ContactBook()
book.add_contact('Sarah Connor', '5550123')
book.list_contacts()
