# Contact Book with Advanced Search Functionality
# Allows users to search for contacts by name and update or delete directly from the search result.

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a contact if it doesn't exist."""
        if self.find_contact(name):
            print("Contact already exists.")
            return
        self.contacts.append({'name': name, 'number': number})
        print("Contact added.")

    def find_contact(self, name):
        """Find and return a contact by name."""
        return next((contact for contact in self.contacts if contact['name'] == name), None)

    def update_contact(self, name):
        """Update a contact's number after finding it."""
        contact = self.find_contact(name)
        if contact:
            new_number = input(f"Enter new number for {name}: ")
            contact['number'] = new_number
            print("Contact updated.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        """Delete a contact after confirming it exists."""
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def search_and_modify(self):
        """Search for a contact and then update or delete it."""
        name = input("Enter the name of the contact to search: ")
        contact = self.find_contact(name)
        if contact:
            action = input("Found contact. Update (u) or Delete (d)? ")
            if action.lower() == 'u':
                self.update_contact(name)
            elif action.lower() == 'd':
                self.delete_contact(name)
            else:
                print("Invalid action.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        """List all the contacts."""
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(f"{contact['name']}: {contact['number']}")

# Example usage
book = ContactBook()
book.add_contact('Jane Doe', '9876543210')
book.search_and_modify()
