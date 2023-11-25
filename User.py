from Contact import Contact
from PhoneBook import PhoneBook


class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.phone_books = {}

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)

    def add_phone_book(self, tag):
        self.phone_books[tag] = PhoneBook(tag)

    def add_contact(self, name, country_code, phone_number, tag):
        contact = Contact(self, name, country_code, phone_number)
        if tag in self.phone_books:
            self.phone_books[tag].add_contact(contact)
        else:
            self.add_phone_book(tag)
            self.phone_books[tag].add_contact(contact)

    def share_phone_book(self, friend, tag):
        if friend not in self.friends:
            print(f"{friend.name} не найден в вашем списке друзей")
            return
        if tag not in self.phone_books:
            print(f"Такой телефонной книжки не существует: '{tag}'.")
            return
        friend.phone_books[tag] = self.phone_books[tag]

    def get_phone_book_contacts(self, tag):
        if tag in self.phone_books:
            return self.phone_books[tag].get_contacts()
        else:
            print(f"Такой телефонной книжки не существует: '{tag}'.")
            return []