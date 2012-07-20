"""
PUBLIC DOMAIN

Lovingly and freely and openly stolen from http://www.pdas.com/programs/fmm.f90

This code currently just contains one adaptation from the FMM collection -- the
numerical bisection optimizer.
"""


from sys import float_info
from math import copysign

class BadBoundsError(Exception): pass
class NoConvergeError(Exception): pass

eps = float_info.epsilon

def zeroin(lower, upper, func, tol, max_eval=25):
    
    a=lower   # initialization
    b=upper
    fa=func(a)
    fb=func(b)
    neval=2
    
    if (fa == 0):
        return a

    if (fb == 0):
        return b
      
    if (fa * fb > 0):
        raise BadBoundsError

    # The trivial cases have now been dealt with. On to the real work...

    c, fc = a, fa
    d = e = b-a
    
    for _eval in range(neval, max_eval+1):
        if (fb>0 and fc>0) or (fb<0 and fc<0):
            c, fc = a, fa  # we insist that b and c straddle the 0
            e = d = b-a

        if abs(fc) < abs(fb):
            a, b, c = b, c, b     # we insist that b be the better
            fa, fb, fc = fb, fc, fb

        tol1 = 2 * eps * abs(b) + 0.5 * tol   # convergence test
        xm = 0.5 * (c - b)
        if abs(xm) <= tol1 or fb == 0:
            # SUCCESS
            return b

        if abs(e) < tol1 or abs(fa) <= abs(fb):
            d = xm   # bisection
            e = d
        else:
            if (a == c):
                s = fb / fa   # linear interpolation
                p = 2 * xm * s
                q = 1 - s
            else:
                q, r, s = fa/fc, fb/fc, fb/fa # inverse quadratic interpolation
                p = s * (2 * xm * q * (q - r) - (b - a) * (r - 1))
                q = (q - 1) * (r - 1) * (s - 1)
                
            if (p > 0):
                q = -q   # adjust signs
            p = abs(p)
              
            if p+p >= (3 * xm * q - abs(tol1 * q)) or p+p >= abs(e*q):
                d = xm   # don't interpolate. Use bisection
                e = d
            else:
                e = d   # OK, use interpolation
                d = p / q

        a = b   # complete step. a becomes the previous iteration
        fa = fb
        
        if (abs(d) > tol1):
            b = b + d
        else: 
            b = b + copysign(tol1, xm)
     
        fb = func(b)   # the newest and best value (we hope)
        neval = neval + 1   # keep count of the function evaluations

    # The loop should never terminate. If it does, return the last iteration
    #  and set errCode to 1
    raise NoConvergeError
        
