from ..unary_operators import Number as N


def test_negative():
    a = -N(5)
    assert isinstance(a, N)
    assert a.number == -5


def test_positive():
    a = +N(-5)
    assert isinstance(a, N)
    assert a.number == 5


def test_absolute():
    a = abs(N(-5))
    assert isinstance(a, N)
    assert a.number == 5


def test_bitwise_invert():
    a = ~N(5)
    assert isinstance(a, N)
    assert a.number == -6


def test_complex():
    a = complex(N(5))
    assert isinstance(a, complex)
    assert a == (5 + 0j)


def test_int():
    a = int(N(5.1))
    assert isinstance(a, int)
    assert a == 5


def test_float():
    a = float(N(5))
    assert isinstance(a, float)
    assert a == 5.0


# === Only available in Python 2 ===
# def test_oct():
#     a = oct(N(5))
#     assert isinstance(a, oct)
#     assert a == '0o5'


# def test_hex():
#     a = hex(N(5))
#     assert isinstance(a, hex)
#     assert a == '0x5'
