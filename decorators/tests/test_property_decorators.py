import pytest

from ..property_decorators import Person


class TestPerson:
    def setup_method(self):
        self.p = Person('Zilong', 'Li')

    def test_fullname_getter(self):
        assert self.p.fullname == 'Zilong Li'

    def test_fullname_setter(self):
        self.p.fullname = 'Tyrion Lannister'
        assert self.p.firstname == 'Tyrion'
        assert self.p.lastname == 'Lannister'
        assert self.p.fullname == 'Tyrion Lannister'

    def test_fullname_deleter(self):
        del self.p.fullname
        assert self.p.firstname is None
        assert self.p.lastname is None
        assert self.p.fullname == 'None None'

    def test_age_getter_normal(self):
        self.p.age = 22
        assert self.p.age == 22
        assert self.p._age == 22

    def test_age_setter_error(self):
        with pytest.raises(ValueError):
            self.p.age = -12
        with pytest.raises(ValueError):
            self.p.age = 160

    def test_age_deleter(self):
        del self.p.age
        assert self.p.age is None
        assert self.p._age is None
