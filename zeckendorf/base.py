"""
The Zeckendorf representation of a positive integer is the unique set of
non-consecutive Fibonacci numbers that sum to it.

>>> list(zeck(12))
[8, 3, 1]
"""

__all__ = ['zeck']


def fibs_le(n):
    """
    Iterate over the Fibonacci numbers <= n.
    """
    cur, nxt = 0, 1
    while cur <= n:
        yield cur
        cur, nxt = nxt, cur + nxt


def zeck(n):
    """
    Iterate over the Zeckendorf representation of n.
    """
    # use greedy algorithm:
    # keep subtracting and yielding the largest fib <= n until n == 0
    fibs = iter(reversed(tuple(fibs_le(n))))
    while n > 0:
        fib = next(fibs)
        if fib <= n:
            yield fib
            n -= fib
            next(fibs)  # skip the next one so we don't get consecutives


if __name__ == '__main__':
    # example: print Zeckendorf representations for numbers 0-99
    [print(n, '=', ' + '.join(str(f) for f in zeck(n))) for n in range(100)]
