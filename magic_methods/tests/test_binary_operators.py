from ..binary_operators import NumberTuple as NT


def test_addition():
    a = NT(2, 3) + NT(4, 6)
    assert isinstance(a, NT)
    assert a.output() == (6, 9)
    b = NT(1, 2, 3) + NT(4, 5, 6)
    assert isinstance(b, NT)
    assert b.output() == (5, 7, 9)


def test_subtraction():
    a = NT(4, 7) - NT(1, 3)
    assert isinstance(a, NT)
    assert a.output() == (3, 4)
    b = NT(4, 5, 6) - NT(1, 2, 3)
    assert isinstance(b, NT)
    assert b.output() == (3, 3, 3)


def test_division():
    a = NT(4, 6) / NT(1, 3)
    assert isinstance(a, NT)
    assert a.output() == (4, 2)
    b = NT(4, 5, 6) / NT(2, 2, 1)
    assert isinstance(b, NT)
    assert b.output() == (2, 2.5, 6)


def test_floor_division():
    a = NT(4, 6) // NT(1, 3)
    assert isinstance(a, NT)
    assert a.output() == (4, 2)
    b = NT(4, 5, 6) // NT(2, 2, 1)
    assert isinstance(b, NT)
    assert b.output() == (2, 2, 6)
