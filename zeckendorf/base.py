"""
The mathematical backbone of Zeckendorf: utilities for generating and
working with Zeckendorf representations as streams of integers.
"""


def _fibs_le(n):
    """Iterate over the Fibonacci numbers <= n."""
    cur, nxt = 0, 1
    while cur <= n:
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
    fibs = iter(reversed(tuple(_fibs_le(n))))
    while n > 0:
        fib = next(fibs)
        if fib <= n:
            yield fib
            n -= fib
            next(fibs)  # will always be > n, so we can skip


if __name__ == '__main__':
    # example: print Zeckendorf representations for numbers 0-99
    [print(n, '=', ' + '.join(str(f) for f in zeck(n))) for n in range(100)]
