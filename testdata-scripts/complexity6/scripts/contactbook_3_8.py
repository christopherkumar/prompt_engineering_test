# Contact book with file persistence to save contacts between sessions

import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, number):
        if any(contact['name'] == name for contact in self.contacts):
            print("Contact already exists.")
            return
        self.contacts.append({'name': name, 'number': number})
        self.save_contacts()
        print("Contact added.")

    def list_contacts(self):
        for contact in self.contacts:
            print(f"{contact['name']}: {contact['number']}")

book = ContactBook()
book.add_contact('Jane Doe', '0987654321')
book.list_contacts()
