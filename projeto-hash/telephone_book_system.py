class PhoneBook:
    def __init__(self, size=100):
        self.size = size
        self.count = 0
        self.contacts = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def load_factor(self):
        return self.count / self.size  # quanto da tabela esta ocupada

    def rehash(self):
        print("\n Rehashing... increasing table size")
        old_contacts = self.contacts
        self.size *= 2
        self.contacts = [[]for _ in range(self.size)]
        self.count = 0
        for contact in old_contacts:
            for name, phone, email in contact:
                self.add(name, phone, email)

    def add(self, name, phone, email):
        if self.load_factor() > 0.85:  # se tiver 70% cheio
            self.rehash()

        index = self.hash_function(name)
        contact = self.contacts[index]
        for i, (k, p, e) in enumerate(contact):
            if k == name:
                contact[i] = (name, phone, email)
                return
        contact.append((name, phone, email))
        self.count += 1

    def remove(self, name):
        index = self.hash_function(name)
        contact = self.contacts[index]
        for i, (k, p, e) in enumerate(contact):
            if k == name:
                contact.pop(i)
                self.count -= 1

    def print_phoneBook(self):
        print("--Telephone Directory--")
        print(f"PhoneBook - (size={self.size}, contacts = {self.count})")
        for index, contact in enumerate(self.contacts):
            print(f"Contact {index}: {contact}")

    def get(self, name):
        index = self.hash_function(name)
        contact = self.contacts[index]
        for i, (key, phone, email) in enumerate(contact):
            if key == name:
                return print(f"Contact with name {name} has a phone: {phone} and a email: {email}")
        return print("Contact not found")


my_telephone_directory = PhoneBook(size=4)

my_telephone_directory.add("Diego", "65996615085", "diego@gmail.com")
my_telephone_directory.add("Sofia", "65996615085", "sofia@gmail.com")
my_telephone_directory.add("maisa", "65996615085", "maisa@gmail.com")
my_telephone_directory.add("lucas", "65996615085", "lucas@gmail.com")
my_telephone_directory.add("bob", "65996615085", "bob@gmail.com")
my_telephone_directory.add("Ana", "1111", "ana@gmail.com")
my_telephone_directory.add("Beto", "2222", "beto@gmail.com")
my_telephone_directory.add("Carlos", "3333", "carlos@gmail.com")


my_telephone_directory.remove("bob")

my_telephone_directory.print_phoneBook()

my_telephone_directory.get("Sofia")
