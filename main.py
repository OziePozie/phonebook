from User import User

user1 = User("Daniil")
user2 = User("Timur")

user1.add_friend(user2)
user1.add_phone_book("family")
user1.add_contact("Mom", "+1","12345676890" ,"family")
user1.add_contact("Momф", "+1","12345676890" ,"family")
user2.add_contact("Momф", "+1","12345676890" ,"family")

user1.share_phone_book(user2, "family")

contacts = user2.get_phone_book_contacts("family")

for contact in contacts:
    print(f"{contact.user.name} "
          f"tag:{user1.phone_books['family'].tag} "
          f"name:{contact.name} "
          f"contact: {contact.country_code} "
          f"{contact.phone_number}")