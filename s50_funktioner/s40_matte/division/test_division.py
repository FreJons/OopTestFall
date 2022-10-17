import unittest
from division_funk import division

assert(callable(division))
assert(division(6, 2) == 3)
assert(division(100, 4) == 25)
assert(division(40, 4) == 10)