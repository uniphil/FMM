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
                          fmm.zeroin, 1, 2, lambda x: x, self.tol)
        self.assertRaises(fmm.BadBoundsError,
                          fmm.zeroin, -1, -2, lambda x: x, self.tol)
    
    def test_non_converge_const(self):
        def f(x):
            return x if x == -1 else 1
        self.assertRaises(fmm.NoConvergeError, fmm.zeroin, -1, 1, f, self.tol)
    
    def test_non_converge_rand(self):
        # [x-1 if x<0.5 else x for x in
        #                   [round(random.random(), 3) for r in range(25)]]

        randseq = [-0.712, 0.94, -0.628, -0.724, 0.935, 0.868, -0.744,
                   0.868, -0.993, -0.972, 0.764, -0.589, -0.762, 0.751,
                   0.749, -0.522, -0.565, 0.957, -0.862, 0.748, 0.789,
                   -0.862, -0.731, 0.654, -0.929]
        def f(x):
            if abs(x) == 1:
                return x
            return randseq.pop()
        self.assertRaises(fmm.NoConvergeError, fmm.zeroin, -1, 1, f, self.tol)
    
    def test_few_evals(self):
        "Too few allowed evaluations for convergence"
        f = lambda x: x**3 - 5 # takes > 3 evaluations to converge
        self.assertRaises(fmm.NoConvergeError,
                          fmm.zeroin, 1, 10, f, self.tol, 3)
    

if __name__ == '__main__':
    unittest.main()

