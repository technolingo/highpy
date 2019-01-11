class Number:
    def __init__(self, number):
        self.number = number

    def __neg__(self):
        return Number(-abs(self.number))

    def __pos__(self):
        return Number(abs(self.number))

    def __abs__(self):
        return self.__pos__()

    def __invert__(self):
        return Number(~self.number)

    def __complex__(self):
        return complex(self.number)

    def __int__(self):
        return int(self.number)

    def __float__(self):
        return float(self.number)

    # === Only available in Python 2 ===
    # def __oct__(self):
    #     return oct(self.number)

    # def __hex__(self):
    #     return hex(self.number)
