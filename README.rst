Zeckendorf
==========

The `Zeckendorf representation <https://encyclopediaofmath.org/wiki/Zeckendorf_representation>`_
of a positive integer is the unique set of non-consecutive Fibonacci
numbers that sum to it. For example:

* .. image:: https://latex.codecogs.com/svg.latex?12=8+3+1
* .. image:: https://latex.codecogs.com/svg.latex?75=55+13+5+2

This package provides functionality for generating, interpreting, and
processing Zeckendorf representations in various ways.

The source code is available `here <https://github.com/omaitzen/zeckendorf>`_.

Motivation
----------

This package was made to be a simple practice example while learning how
to properly set up and distribute Python packages. Calculating
Zeckendorf representations has become my go-to exercise when learning a
new programming language, and I thought it would be more fun here than
just making the empty "example-pkg" laid out in the
`PyPUG tutorial <https://packaging.python.org/tutorials/packaging-projects/>`_.

Example Usage
-------------

>>> import zeckendorf
>>> list(zeckendorf.zeck(12))
[8, 3, 1]
>>> zeckendorf.binary.str_fromint(28)
'1001010'

TODO
----

* Turn ``zeck`` and ``negazeck`` into classes with various magic
  methods, including operator overloads using the algorithms in
  `this paper <https://www.math.brown.edu/~jusatine/papers/EAZA.pdf>`_
* Generalize to
  `Ostrowski numeration <https://en.wikipedia.org/wiki/Ostrowski_numeration>`_
  (thanks whirligig)
