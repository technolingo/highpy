from collections import Generator


class Fibonacci(Generator):
    def __init__(self) -> None:
        self.a, self.b = 0, 1

    def send(self, value):
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

    def throw(self, typ=None, val=None, tb=None):
        if typ is not None:
            raise typ
        raise StopIteration


g = Fibonacci()

# print(next(g))
# print(next(g))
# print(g.__next__())
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    if i > 50:
        g.throw()
    print(i)
