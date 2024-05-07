# Comprehensive Contact Management System
# Supports addition, deletion, updating, searching, and listing of contacts with full input validation and exception handling.

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        """Add a contact after validating input."""
        try:
            name = input("Enter contact name: ").strip()
            if not name:
                raise ValueError("Contact name cannot be empty.")
            number = input("Enter contact number: ").strip()
            if not number.isdigit():
                raise ValueError("Contact number must be numeric.")
            if name in self.contacts:
                raise ValueError("Contact already exists.")
            self.contacts[name] = number
            print("Contact added successfully.")
        except ValueError as e:
            print(e)

    def delete_contact(self):
        """Delete a contact after validating existence."""
        name = input("Enter contact name to delete: ").strip()
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def update_contact(self):
        """Update a contact's number after validating."""
        name = input("Enter contact name to update: ").strip()
        if name in self.contacts:
            number = input("Enter new contact number: ").strip()
            if number.isdigit():
                self.contacts[name] = number
                print("Contact updated successfully.")
            else:
                print("Invalid number. Update failed.")
        else:
            print("Contact not found.")

    def search_contact(self):
        """Search and display a contact."""
        name = input("Enter contact name to search: ").strip()
        if name in self.contacts:
            print(f"Found contact: {name}, Number: {self.contacts[name]}")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("No contacts to display.")
        else:
            for name, number in self.contacts.items():
                print(f"{name}: {number}")

# Example usage
manager = ContactManager()
manager.add_contact()
manager.list_contacts()
