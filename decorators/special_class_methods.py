class Programmer:
    raise_rate = 1.05

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def raise_salary(self):
        self.salary = int(self.salary * self.raise_rate)

    @classmethod
    def set_raise_rate(cls, rate):
        cls.raise_rate = rate

    @staticmethod
    def convert_to_usd(euro_amount):
        return euro_amount * 1.14
