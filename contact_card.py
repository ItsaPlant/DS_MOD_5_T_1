from faker import Faker
from faker.providers import DynamicProvider

arch_professions_provider = DynamicProvider(
    provider_name="architectural_profession",
    elements=["arch", "MARCH", "Senior Architect",
              "Intern Architect", "consultant", "za miskę ryzu"]
)

fake = Faker()
fake.add_provider(arch_professions_provider)


class ContactCard:
    def __init__(self):
        self.name = None
        self.surname = None
        self.fullname_len = None
        
    

    def __str__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name}, {self.surname}, {self.contact}'
    

    def __ge__(self, other, param): #jak rozwinąć taki pomysl?
        return self.param >= other.param


    def generate(self):
        self.name = fake.first_name()
        self.surname = fake.last_name()
        self.company = fake.job()
        self.position = fake.arch_professions_provider()
        self.mail = fake.email()
    

    def contact(self):
        return f'Kontaktuje się z: {self.name} {self.surname}, {self.position}, {self.mail}'
    

    @property
    def full_name(self):
        return f'{self.name} {self.surname}, {self.fullname_len}'
    

    @full_name.setter
    def full_name(self):
        name_len = len(self.name)
        surname_len = len(self.surname)
        self.fullname_len = name_len + surname_len


    
    @staticmethod
    def sort(obj_list, param):
        return sorted(obj_list, key=lambda obj: obj.param) #again the idea of param?



class BusinessCard(ContactCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = None
        self.position = None
        self.mail = None
        
"""
Stwórz listę wizytówek, a następnie używając funkcji sorted(), ułóż ją na trzy 
sposoby – według imienia, nazwiska oraz adresu e-mail.
"""
