"""
Unit tests for zeckendorf.base.
"""
from zeckendorf import base


def test_zeck():
    assert list(base.zeck(0)) == []
    assert list(base.zeck(1)) == [1]
    assert list(base.zeck(12)) == [8, 3, 1]
    assert list(base.zeck(75)) == [55, 13, 5, 2]


def test():
    test_zeck()


if __name__ == '__main__':
    test()
