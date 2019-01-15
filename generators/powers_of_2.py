from typing import Iterator


def powers_of_two() -> Iterator[int]:
    exponent = 1
    while True:
        yield 2 ** exponent
        exponent += 1


g = powers_of_two()
print(next(g))
print(next(g))
print(g.__next__())

# for i in g:
#     if i > 64:
#         g.throw(ValueError, StopIteration())
#     print(i)
