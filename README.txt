Forsyth Malcolm Moler

A collection of procedures for numerical computation. Originally published in
"Computer Methods for Mathematical Computations" by George E. Forsythe,
Michael A. Malcolm, and Cleve B. Moler. Prentice-Hall, 1977.

Currently only the bisection optimizer is implemented, but I hope one day to
port all the subroutines. The bisection optimizer is actually credited to
Richard Brent in my source (http://www.pdas.com/programs/fmm.f90)

Adding to that revision history (RLC = Ralph L. Carmichael, PS = Philip
Schleihauf):
!   DATE  VERS PERSON STATEMENT OF CHANGES
!   1977   1.0   FMM  Original publication
! 07Jul83  1.1   RLC  Mods for Fortran77
! 09Jul89  1.2   RLC  Added SEVAL3, IMPLICIT NONE
! 17Apr91  1.3   RLC  Fortran 90 style loops
! 10May92  1.4   RLC  Fortran 90 coding
! 23Aug00  1.5   RLC  Made compatible with Elf90
! 26Apr02  1.6   RLC  Added NaturalSpline
! 03May02  1.7   RLC  Charged calling sequence of SVD
! 20May02  1.8   RLC  Added BrentZero - mod of ZeroIn
! 28May02  1.9   RLC  Added errCode to Decomp
! 28Jun02  1.91  RLC  Made cond OPTIONAL in Decomp
! 21Aug02  1.95  RLC  Made single and double precision versions 
! 11Oct02  1.96  RLC  Compute eps each time in RKFS
! 20Jul12  0.1   PS   Port BrentZero to Python!


This software is Public Domain. Have fun! And if you feel like porting more of
the Fortran subroutines, share them back and I'll add them to the package!



INSTALLING:

This package is on pypi. Just do:

pip install FMM
