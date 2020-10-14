"""
The mathematical backbone of Zeckendorf: utilities for generating and
working with Zeckendorf representations as streams of integers.
"""


def _fibs(*, le=None):
    """
    Iterate over the Fibonacci numbers.

    :param le: if specified, the iterator will stop at the last number
        less than or equal to this value.
    :type le: Optional[int]
    :return: the iterator.
    :rtype: Iterator[int]
    """
    cur, nxt = 0, 1
    while le is None or cur <= le:
        yield cur
        cur, nxt = nxt, cur + nxt


def zeck(n):
    """
    Iterate over the Zeckendorf representation of n.

    :param n: a non-negative integer.
    :type n: int
    :return: an iterator over the Fibonacci numbers in n's Zeckendorf
        representation, from largest to smallest. Passing 0 will return
        an empty iterator.
    :rtype: Iterator[int]

    >>> list(zeck(12))
    [8, 3, 1]
    """
    # use greedy algorithm:
    # keep subtracting and yielding the largest fib <= n until n == 0
    fibs = reversed(tuple(_fibs(le=n)))
    while n > 0:
        fib = next(fibs)
        if fib <= n:
            yield fib
            n -= fib
            next(fibs)  # will always be > n, so we can skip


def _negafibs(*, sandwiching=None):
    """
    Iterate over the Fibonacci numbers.

    :param sandwiching: if specified, the iterator will stop after
        returning a number with a different sign than this and a
        greater absolute value.
    :type sandwiching: Optional[int]
    :return: the iterator.
    :rtype: Iterator[int]
    """
    cur, nxt = 0, 1
    while (
        sandwiching is None
        or abs(cur) <= abs(sandwiching)
        or cur * sandwiching > 0  # cur & sandwiching have same sign
    ):
        yield cur
        cur, nxt = nxt, cur - nxt
    yield cur  # 1 extra with opposite sign, to "sandwich" properly


def negazeck(n):
    """
    Iterate over the nega-Zeckendorf representation of n.

    The nega-Zeckendorf representation is analogous to the regular
    Zeckendorf representation, but using the nega-Fibonacci numbers
    (1, -1, 2, -3, ...). It can represent all integers, negative and
    positive.

    :param n: any integer.
    :type n: int
    :return: an iterator over the nega-Fibonacci numbers in n's
        nega-Zeckendorf representation, from largest to smallest in
        absolute value. Passing 0 will return an empty iterator.
    :rtype: Iterator[int]

    >>> list(negazeck(-17))
    [-21, 5, -1]
    """
    # algorithm thanks to user templatetypedef on stackoverflow:
    # https://stackoverflow.com/a/45248031
    negafibs = reversed(tuple(_negafibs(sandwiching=n)))
    negafib, nxt = next(negafibs), -next(negafibs)
    while n != 0:
        prv, negafib, nxt = -negafib, -nxt, -next(negafibs)
        if prv < n <= nxt or prv >= n > nxt:
            yield negafib
            n -= negafib


if __name__ == '__main__':
    # example: print Zeckendorf representations for numbers 0-99
    [print(n, '=', ' + '.join(str(f) for f in zeck(n))) for n in range(100)]
