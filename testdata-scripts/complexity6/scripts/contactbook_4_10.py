# Enhanced Contact Book with Validation and Persistence
# Provides a complete contact management system with input validation and data persistence through file storage.

import json

class Contact:
    def __init__(self, name, number):
        self.validate(name, number)
        self.name = name
        self.number = number

    @staticmethod
    def validate(name, number):
        if not name or not number:
            raise ValueError("Name and number are required.")
        if not number.isdigit():
            raise ValueError("Number must be numeric.")

    def __str__(self):
        return f"{self.name} - {self.number}"

class ContactBook:
    def __init__(self, file_path='contacts.json'):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                contacts_data = json.load(file)
            return [Contact(name, data['number']) for name, data in contacts_data.items()]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        contacts_data = {contact.name: {'number': contact.number} for contact in self.contacts}
        with open(self.file_path, 'w') as file:
            json.dump(contacts_data, file, indent=2)

    def add_contact(self, name, number):
        if any(contact.name == name for contact in self.contacts):
            print("Contact already exists.")
            return
        try:
            contact = Contact(name, number)
            self.contacts.append(contact)
            self.save_contacts()
            print("Contact added and saved.")
        except ValueError as e:
            print(e)

    def find_contact(self, name):
        return next((contact for contact in self.contacts if contact.name == name), None)

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()
            print("Contact deleted and saved.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact)

# Example usage
book = ContactBook()
book.add_contact('Michael Reese', '987654321')
book.list_contacts()
