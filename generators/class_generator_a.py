from typing import Iterator


class Fibonacci:
    def __init__(self) -> None:
        self.a, self.b = 0, 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val


g = Fibonacci()

print(next(g))
print(next(g))
print(g.__next__())
print(next(g))
print(next(g))
print(next(g))

# for i in g:
#     if i > 50:
#         break
#     print(i)
