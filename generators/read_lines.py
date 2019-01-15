import os
from typing import Iterator


def first_line(filepath: str) -> str:
    ''' Return the first line of a file. '''
    with open(filepath) as f:
        return f.readline()


dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'sample.txt')
# print(first_line(file_path))


def next_line(filepath: str) -> Iterator[str]:
    ''' a generator that yields the next line in a file. '''
    with open(filepath) as f:
        for line in f.readlines():
            yield line


# print(next(next_line(file_path)))
# print(next(next_line(file_path)))
g = next_line(file_path)
print(next(g))
print(next(g))
print(g.__next__())

# for i in g:
#     print(i)
