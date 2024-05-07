# Optimal Contact Book with Exception Handling
# This script implements a contact book with full exception handling, efficient data management, and comprehensive documentation.

class Contact:
    """Represents a contact with name and number."""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f"Contact(name={self.name}, number={self.number})"

class ContactBook:
    """Manages a list of contacts, allowing for adding, removing, and searching contacts."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a contact if it doesn't exist in the contact book.

        Args:
            name (str): The contact's name.
            number (str): The contact's number.

        Raises:
            ValueError: If the contact already exists.
        """
        if self._find_contact(name):
            raise ValueError("Contact already exists.")
        self.contacts.append(Contact(name, number))

    def _find_contact(self, name):
        """Search for a contact by name.

        Args:
            name (str): The contact's name to search for.

        Returns:
            Contact: The found contact or None if not found.
        """
        return next((contact for contact in self.contacts if contact.name == name), None)

    def remove_contact(self, name):
        """Remove a contact by name from the contact book.

        Args:
            name (str): The contact's name to remove.

        Raises:
            ValueError: If the contact does not exist.
        """
        contact = self._find_contact(name)
        if contact is None:
            raise ValueError("Contact not found.")
        self.contacts.remove(contact)

    def list_contacts(self):
        """Prints all contacts in the contact book."""
        for contact in self.contacts:
            print(contact)

# Example of using the ContactBook class
try:
    book = ContactBook()
    book.add_contact("Alice Johnson", "123-456-7890")
    book.list_contacts()
except ValueError as e:
    print(e)
