import unittest
from upphojt_funk import upphöjt


assert(callable(upphöjt))
assert(upphöjt(2, 2) == 4)
assert(upphöjt(5, 6) == 15625)
assert(upphöjt(2, 6) == 64)