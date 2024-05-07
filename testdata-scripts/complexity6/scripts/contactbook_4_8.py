# Contact Book with Detailed Documentation and Exception Handling
# This script provides a comprehensive contact management system with thorough documentation for each function.

class ContactBook:
    def __init__(self):
        """Initialize the contact book with an empty list of contacts."""
        self.contacts = []

    def add_contact(self, name, number):
        """Add a new contact to the book after validating non-existence.

        Args:
            name (str): The name of the contact to add.
            number (str): The phone number of the contact to add.

        Returns:
            None
        """
        if any(contact['name'] == name for contact in self.contacts):
            print("Contact already exists.")
            return
        self.contacts.append({'name': name, 'number': number})
        print("Contact added successfully.")

    def delete_contact(self, name):
        """Delete a contact from the book by name.

        Args:
            name (str): The name of the contact to delete.

        Returns:
            None
        """
        contact = next((c for c in self.contacts if c['name'] == name), None)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """List all the contacts in the book.

        Returns:
            None
        """
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(f"{contact['name']}: {contact['number']}")

# Example usage
book = ContactBook()
book.add_contact('John Doe', '1234567890')
book.list_contacts()
