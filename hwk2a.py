import numpy as np
import math
import pandas as pd

A=58.0
Z=28.0
a1=15.8
a2=18.3
a3=0.714
a4=23.2
if A % 2 == 1:
    a5=0
elif Z % 2 == 0:
    a5=12.0
else:
    a5=-12.0

def SemiEmpirical_mass_formula(A, Z):
    B = a1*A - a2*(A**(2/3)) -a3*((Z**2)/(A**(1/3))) -a4*((A-(2*Z))**2/A) -(a5/(A**1/2))
    return B

answer=SemiEmpirical_mass_formula(A,Z)
print(answer)
