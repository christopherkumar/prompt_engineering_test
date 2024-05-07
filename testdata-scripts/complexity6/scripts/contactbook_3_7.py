# Enhanced contact book using class structure

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
        if any(contact.name == name for contact in self.contacts):
            print("Contact already exists.")
            return
        self.contacts.append(Contact(name, number))
        print("Contact added.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)

book = ContactBook()
book.add_contact('John Doe', '1234567890')
book.list_contacts()
