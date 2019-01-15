from ..special_class_methods import Programmer


class TestProgrammer:
    def setup_method(self):
        self.p = Programmer('Zilong', 'Li', 50000)

    def test_programmer(self):
        assert self.p.lastname == 'Li'
        assert self.p.salary == 50000
        self.p.raise_salary()
        assert self.p.salary == 50000 * Programmer.raise_rate

    def test_classmethod(self):
        Programmer.set_raise_rate(1.1)
        assert Programmer.raise_rate == 1.1
        self.p.set_raise_rate(1.2)
        assert Programmer.raise_rate == 1.2
        assert self.p.raise_rate == 1.2

    def test_staticmethod(self):
        assert self.p.convert_to_usd(60000) == 68400
