class Number:
    def __init__(self, number):
        self.number = number

    def __iadd__(self, other):
        return Number(self.number + other.number)

    def __isub__(self, other):
        return Number(self.number - other.number)

    def __imul__(self, other):
        return Number(self.number * other.number)

    def __itruediv__(self, other):
        return Number(self.number / other.number)

    def __ifloordiv__(self, other):
        return Number(self.number // other.number)

    def __imod__(self, other):
        return Number(self.number % other.number)

    def __ipow__(self, other):
        return Number(self.number ** other.number)

    def __iand__(self, other):
        return Number(self.number & other.number)

    def __ior__(self, other):
        return Number(self.number | other.number)

    def __ixor__(self, other):
        return Number(self.number ^ other.number)

    def __ilshift__(self, other):
        return Number(self.number << other.number)

    def __irshift__(self, other):
        return Number(self.number >> other.number)
