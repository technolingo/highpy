from ..inplace_operators import Number as N


def test_number_class():
    a = N(0)
    assert isinstance(a, N)
    assert a.number == 0


def test_iadd():
    a = N(5)
    a += N(2)
    assert a.number == 7


def test_isub():
    a = N(5)
    a -= N(2)
    assert a.number == 3


def test_imul():
    a = N(5)
    a *= N(2)
    assert a.number == 10


def test_itruediv():
    a = N(5)
    a /= N(2)
    assert a.number == 2.5


def test_ifloordiv():
    a = N(5)
    a //= N(2)
    assert a.number == 2


def test_imod():
    a = N(5)
    a %= N(2)
    assert a.number == 1


def test_ipow():
    a = N(5)
    a **= N(2)
    assert a.number == 25


def test_iand():
    a = N(5)
    a &= N(2)
    assert a.number == 0


def test_ior():
    a = N(5)
    a |= N(3)
    assert a.number == 7


def test_ixor():
    a = N(5)
    a ^= N(3)
    assert a.number == 6


def test_ilshift():
    a = N(5)
    a <<= N(2)
    assert a.number == 20


def test_irshift():
    a = N(9)
    a >>= N(3)
    assert a.number == 1
