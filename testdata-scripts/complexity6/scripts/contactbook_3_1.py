# Contact book implementation using a class for better structure
# Operations like add, delete, and list contacts are included

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        """Add a new contact."""
        if not self._contact_exists(name):
            self.contacts.append({'name': name, 'number': number})
            print("Contact added.")
        else:
            print("Contact already exists.")

    def _contact_exists(self, name):
        """Check if the contact exists."""
        return any(contact['name'] == name for contact in self.contacts)

    def delete_contact(self, name):
        """Delete a contact."""
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        print("Contact deleted.")

    def list_contacts(self):
        """List all contacts."""
        if self.contacts:
            for contact in self.contacts:
                print(f"{contact['name']} - {contact['number']}")
        else:
            print("No contacts found.")

# Usage
book = ContactBook()
book.add_contact('John Doe', '1234567890')
book.list_contacts()
