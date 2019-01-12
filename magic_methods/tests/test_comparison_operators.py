from ..comparison_operators import Number as N


def test_lt():
    assert N(5) < N(7)


def test_gt():
    assert N(7) > N(5)


def test_eq():
    assert N(7) == N(7)


def test_ne():
    assert N(7) != N(8)


def test_le():
    assert N(7) <= N(8)
    assert N(8) <= N(8)


def test_ge():
    assert N(7) >= N(5)
    assert N(8) >= N(8)
