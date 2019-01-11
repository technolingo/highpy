from ..binary_operators import NumberTuple as NT, Number as N


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


def test_modulo():
    a = N(value=7) % N(value=3)
    assert isinstance(a, N)
    assert a.output() == 1
    b = N(value=20) % N(value=7)
    assert isinstance(b, N)
    assert b.output() == 6


def test_power():
    a = N(value=4) ** N(value=2)
    assert isinstance(a, N)
    assert a.output() == 16
    b = N(value=4) ** N(value=0)
    assert isinstance(b, N)
    assert b.output() == 1


def test_left_shift():
    a = N(value=10) << N(value=2)
    assert isinstance(a, N)
    assert a.output() == 40
    b = N(value=10) << N(value=3)
    assert isinstance(b, N)
    assert b.output() == 80


def test_right_shift():
    a = N(value=10) >> N(value=2)
    assert isinstance(a, N)
    assert a.output() == 2
    b = N(value=10) >> N(value=3)
    assert isinstance(b, N)
    assert b.output() == 1


def test_bitwise_and():
    a = N(value=12) & N(value=13)
    assert isinstance(a, N)
    assert a.output() == 12
    b = N(value=5) & N(value=7)
    assert isinstance(b, N)
    assert b.output() == 5


def test_bitwise_xor():
    a = N(value=12) ^ N(value=13)
    assert isinstance(a, N)
    assert a.output() == 1
    b = N(value=5) ^ N(value=7)
    assert isinstance(b, N)
    assert b.output() == 2


def test_bitwise_or():
    a = N(value=12) | N(value=13)
    assert isinstance(a, N)
    assert a.output() == 13
    b = N(value=5) | N(value=7)
    assert isinstance(b, N)
    assert b.output() == 7
