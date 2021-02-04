import numpy as np  #Declarations
import math
import pandas as pd

nuclearData = pd.read_csv('nuclear_data.txt', sep=" ", header=None)
nuclearData.columns = ["A", "Z", "Name", "Binding Energy","x","y"] 

Z=0
n=0
a1=15.8
a2=18.3     #constants
a3=0.714
a4=23.2

def a5_assignment(A,Z):
    if A % 2 == 1:
        a5=0
    elif Z % 2 == 0:
        a5=12.0         #solving for a5 given A & Z
    else:
        a5=-12.0
 
def SemiEmpirical_mass_formula(A, Z): #function for semi-empirical mass formula
    B = a1*A - a2*(A**(2/3)) -a3*((Z**2)/(A**(1/3))) -a4*((A-(2*Z))**2/A) -(a5/(A**1/2))
    # b.) just add "B = B/A" to find binding energy per nucleon
    return B

while Z != "~~~":                   # "~~~" was inserted into the txt file to
    Z = nuclearData["Z"].iloc[n]    # stop the while loop from reading the data
    n = n + 1                       # out of the Z column

    A = Z
    lst=[]
    while A != 4*Z:
        a5_assignment(A,Z)
        ans=SemiEmpirical_mass_formula(A,Z)
        lst.extend([ans])
        A = A + Z
    maximum = max(lst,key=lambda x:float(x))
    print(maximum)
