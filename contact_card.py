from faker import Faker
from faker.providers import BaseProvider


class ArchitecturalProfessionProvider(BaseProvider):
    def architectural_profession(self):
        return self.random_element(["arch", "MARCH", "Senior Architect", "Intern Architect", "consultant", "za miskę ryzu"])


fake = Faker()
fake.add_provider(ArchitecturalProfessionProvider)


class ContactCard:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'{self.name} {self.surname} -> {self.phone}'

    def __repr__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name} {self.surname} -> {self.phone}'

    def contact(self):
        return f'Kontaktuje się z: {self.name} {self.surname}, pod numerem: {self.phone}'


class BusinessCard(ContactCard):
    def __init__(self, company, position, phone_work, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.phone_work = phone_work

    def __str__(self):
        return f'{self.name} {self.surname} -> {self.phone_work}'
    
    def __repr__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name} {self.surname} -> {self.phone_work}'

    def contact(self):
        return f'Kontaktuje się z: {self.name} {self.surname}, pod numerem: {self.phone_work}'


def generate():
    name = fake.first_name()
    surname = fake.last_name()
    phone = fake.phone_number()
    company = fake.job()
    position = fake.architectural_profession()
    phone_work = fake.phone_number()
    return name, surname, phone, company, position, phone_work


def create_contacts(card_type, number):
    cards = []
    for i in range(number):
        name, surname, phone, company, position, phone_work = generate()
        if card_type == 'B':
            b_card = BusinessCard(company=company, position=position, phone_work=phone_work, name=name, surname=surname, phone=phone)
            cards.append(b_card)
        elif card_type == 'C':
            c_card = ContactCard(name=name, surname=surname, phone=phone)
            cards.append(c_card)
    return cards

if __name__ == "__main__":
    print(create_contacts('B', 10))
