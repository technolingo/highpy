class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not (age >= 0 and age <= 130):
            raise ValueError('Invalid age.')
        self._age = age

    @age.deleter
    def age(self):
        self._age = None

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, fullname):
        if fullname.count(' ') != 1 and len(fullname) < 2:
            raise NotImplementedError()
        self.firstname, self.lastname = fullname.split()

    @fullname.deleter
    def fullname(self):
        self.firstname, self.lastname = None, None

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@email.com'

    def webpage(self):
        return f'westros.com/{self.firstname}-{self.lastname}'


zil = Person('Zilong', 'Li')
zil.fullname = 'Tyrion Lannister'
zil.age = 22

print(zil.age)
print(zil.fullname)
print(zil.email)
print(zil.webpage())
