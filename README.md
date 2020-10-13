# Zeckendorf

The [Zeckendorf representation](https://encyclopediaofmath.org/wiki/Zeckendorf_representation)
of a positive integer is the unique set of non-consecutive Fibonacci
numbers that sum to it. For example:

![12 = 8 + 3 + 1](https://latex.codecogs.com/svg.latex?12=8+3+1)

![75 = 55 + 13 + 5 + 2](https://latex.codecogs.com/svg.latex?75=55+13+5+2)

This package provides a basic utility function `zeck(n)` for generating
a Zeckendorf representation as a stream of integers. In the future, it
will implement functionality to process these representations in various
ways.

The source code is available [here](https://github.com/omaitzen/zeckendorf).

---

This package was made to be a simple practice example while learning how
to properly set up and distribute Python packages. Calculating
Zeckendorf representations has become my go-to exercise when learning a
new programming language, and I thought it would be more fun here than
just making the empty "example-pkg" laid out in the
[PyPUG tutorial](https://packaging.python.org/tutorials/packaging-projects/).
