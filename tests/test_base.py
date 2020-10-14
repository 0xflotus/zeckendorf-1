"""
Unit tests for zeckendorf.base.
"""
from zeckendorf import base


def test_zeck():
    assert list(base.zeck(0)) == []
    assert list(base.zeck(1)) == [1]
    assert list(base.zeck(12)) == [8, 3, 1]
    assert list(base.zeck(75)) == [55, 13, 5, 2]


def test_negazeck():
    assert list(base.negazeck(0)) == []
    assert list(base.negazeck(1)) == [1]
    assert list(base.negazeck(-1)) == [-1]
    assert list(base.negazeck(7)) == [5, 2]
    assert list(base.negazeck(24)) == [34, -8, -3, 1]
    assert list(base.negazeck(-69)) == [-55, -21, 5, 2]


def test():
    test_zeck()
    test_negazeck()


if __name__ == '__main__':
    test()
