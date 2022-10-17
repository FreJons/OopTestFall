import unittest
from addition_funk import addition

assert(callable(addition))
assert(addition(3, 2) == 5)
assert(addition(5, 9) ==14)
assert(addition(2, 6) == 8)