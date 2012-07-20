"""
Public Domain Software
WOOOO HOOOO
go nuts
"""
from sys import float_info
import unittest
from .. import fmm

class testZeroin(unittest.TestCase):

    tol = 0.01
    
    def ok_tol(self, x):
        return 2* (4*fmm.eps*abs(x) + self.tol)
        
    def check(self, f):
        def z(f):
            return fmm.zeroin(1, 10, f, self.tol)
        fz = z(f)
        self.assertLessEqual(abs(f(fz)), self.ok_tol(fz))
        
    def test_linear(self):
        self.check(lambda x: x - 5)
        
    def test_quad(self):
        self.check(lambda x: x**2 - 5)

    def test_cube(self):
        self.check(lambda x: x**3 - 5)
    
    def test_neg_pow(self):
        self.check(lambda x: x**-2 - 0.5)
    
    def test_frac_pow(self):
        self.check(lambda x: x**(5/9.0) - 2)
    
    def test_rational(self):
        self.check(lambda x: x**2/x**3 - 0.5)

    def test_exp(self):
        self.check(lambda x: 2**x - 5)
    
    def test_log(self):
        from math import log
        self.check(lambda x: log(x) - 1)
    
    def test_sin(self):
        from math import sin
        self.check(lambda x: sin(x/9) - 0.5)
    
    def test_bad_bounds(self):
        self.assertRaises(fmm.BadBoundsError,
                          fmm.zeroin, 1, 2, lambda x: x, 0.01)
        self.assertRaises(fmm.BadBoundsError,
                          fmm.zeroin, -1, -2, lambda x: x, 0.01)
    
    def test_non_converge(self):
        import random
        def f(x):
            if abs(x) == 1:
                return x
            return 1
        self.assertRaises(fmm.NoConvergeError,
                          fmm.zeroin, -1, 1, f, 0.01)
    

if __name__ == '__main__':
    unittest.main()
