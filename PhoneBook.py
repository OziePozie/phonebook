class PhoneBook:
    def __init__(self, tag):
        self.contacts = []
        self.tag = tag

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def filter_by_country(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]

    def filter_by_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]

    def get_contacts(self):
        return self.contacts