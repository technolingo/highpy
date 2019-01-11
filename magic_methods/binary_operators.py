class NumberTuple:
    def __init__(self, *args, **kwargs):
        if len(args) == 0 or not isinstance(args, tuple):
            self.numbers = (0, 0)
        else:
            self.numbers = args

    def output(self):
        return self.numbers

    def __add__(self, other):
        # (1, 3) + (2, 5) = (3, 8)
        result = tuple(x + y for x, y in zip(self.numbers, other.numbers))
        return NumberTuple(*result)

    def __sub__(self, other):
        result = tuple(x - y for x, y in zip(self.numbers, other.numbers))
        return NumberTuple(*result)

    def __mul__(self, other):
        result = tuple(x * y for x, y in zip(self.numbers, other.numbers))
        return NumberTuple(*result)

    def __truediv__(self, other):
        result = tuple(x / y for x, y in zip(self.numbers, other.numbers))
        return NumberTuple(*result)

    def __floordiv__(self, other):
        result = tuple(x // y for x, y in zip(self.numbers, other.numbers))
        return NumberTuple(*result)


class Number:
    def __init__(self, *args, **kwargs):
        self.value = kwargs.get('value', 0)

    def output(self):
        return self.value

    def __mod__(self, other):
        return Number(value=self.value % other.value)

    def __pow__(self, other):
        return Number(value=self.value ** other.value)

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __and__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __or__(self, other):
        pass
