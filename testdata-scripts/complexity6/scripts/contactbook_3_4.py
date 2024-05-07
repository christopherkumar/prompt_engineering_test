# Structured contact book using classes with basic operations

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        if self._find_contact(name) is None:
            self.contacts.append(Contact(name, number))
            print("Contact added.")
        else:
            print("Contact already exists.")

    def _find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}: {contact.number}")

book = ContactBook()
book.add_contact('John Doe', '1234567890')
book.list_contacts()
