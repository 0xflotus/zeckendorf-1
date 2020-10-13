Zeckendorf
==========

The `Zeckendorf representation <https://encyclopediaofmath.org/wiki/Zeckendorf_representation>`_
of a positive integer is the unique set of non-consecutive Fibonacci
numbers that sum to it. For example:

* .. image:: https://latex.codecogs.com/svg.latex?12=8+3+1
* .. image:: https://latex.codecogs.com/svg.latex?75=55+13+5+2

This package provides a basic utility function ``zeck(n)`` for
generating a Zeckendorf representation as a stream of integers. In the
future, it will implement functionality to process these representations
in various ways.

The source code is available `here <https://github.com/omaitzen/zeckendorf>`_.

Motivation
----------

This package was made to be a simple practice example while learning how
to properly set up and distribute Python packages. Calculating
Zeckendorf representations has become my go-to exercise when learning a
new programming language, and I thought it would be more fun here than
just making the empty "example-pkg" laid out in the
`PyPUG tutorial <https://packaging.python.org/tutorials/packaging-projects/>`_.

Usage
-----

>>> from zeckendorf import zeck
>>> list(zeck(12))
[8, 3, 1]

TODO
----

* Provide the function ``negazeck(n)`` for generating a unique analogous
  sequence of "negafibonacci" numbers for any integer, using the greedy
  algorithm in `this StackOverflow post <https://stackoverflow.com/questions/41260776/greedy-algorithm-for-finding-a-negafibonacci-representation-of-a-number>`_
* Add ``binary`` module for working with these representations as binary
  codes, including `Fibonacci codes <https://en.wikipedia.org/wiki/Fibonacci_coding>`_
* Turn ``zeck`` and ``negazeck`` into classes with various magic
  methods, including operator overloads using the algorithms in
  `this paper <https://www.math.brown.edu/~jusatine/papers/EAZA.pdf>`_
