from faker import Faker
from faker.providers import DynamicProvider

try: import operator
except ImportError: keyfun= lambda x: x.count # use a lambda if no operator module
else: keyfun= operator.attrgetter("count") # use operator since it's faster than lambda



arch_professions_provider = DynamicProvider(
    provider_name="architectural_profession",
    elements=["arch", "MARCH", "Senior Architect",
              "Intern Architect", "consultant", "za miskę ryzu"]
)

fake = Faker()
fake.add_provider(arch_professions_provider)


class ContactCard:
    def __init__(self, name, surname, mail, phone):
        self.name = name
        self.surname = surname
        self.fullname_len = None
        self.phone = phone
        

    def __str__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name} {self.surname} -> {self.phone}'
    

    def __repr__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name} {self.surname} -> {self.phone}'
    

    def __ge__(self, other, param): #jak rozwinąć taki pomysl?
        return self.param >= other.param
    

    def contact(self):
        return f'Kontaktuje się z: {self.name} {self.surname}, pod numerem: {self.phone}'
    

    @property
    def label_length(self):
        return self.fullname_len
    

    @label_length.setter
    def label_length(self):
        name_len = len(self.name)
        surname_len = len(self.surname)
        self.fullname_len = name_len + surname_len

    
    @staticmethod
    def sort(obj_list, keyfun):
        return obj_list.sort(key=keyfun, reverse=True) # sort in-place


class BusinessCard(ContactCard):
    def __init__(self, company, position, phone_work, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.phone_work = phone_work

    
    def __str__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name} {self.surname} -> {self.phone_work}'
    

    def __repr__(self) -> str: #IDE mi tak wrzuciło, ale po co ta strzałka?
        return f'{self.name} {self.surname} -> {self.phone_work}'
            

    def contact(self):
        return f'Kontaktuje się z: {self.name} {self.surname}, pod numerem: {self.phone_work}'
        
def generate():
    name = fake.first_name()
    surname = fake.last_name()
    mail = fake.email()
    phone = fake.phone_number()
    company = fake.job()
    position = fake.architectural_profession()
    phone_work = fake.phone_number()
    return (name, surname, mail, phone, company, position, phone_work)


def create_contacts(type, number):
    cards = []
    if type == 'B':
        for i in range(number):
            name, surname, mail, phone, company, position, phone_work = generate()
            b_card = BusinessCard(name, surname, mail, phone, company, position, phone_work)
            cards.append(b_card)
    elif type == 'C':
        for i in range(number):
            name, surname, mail, phone, _, _, _ = generate()
            c_card = ContactCard(name, surname, mail, phone)
            cards.append(c_card)
    return cards

print(create_contacts('B', 10))

# class Obj:
#     def __init__(self):
#         self.var_1 = 1
#         self.var_2 = 2


# def return_obj_variable(obj, variable_name):
#     variable_name = operator.attrgetter('var_1')
#     return obj.variable_name

# obj = Obj()

# print(return_obj_variable(obj, 'var_1'))

