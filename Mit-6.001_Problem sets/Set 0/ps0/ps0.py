# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 01:37:48 2023

@author: creis
"""

#set 0 

import numpy as np

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))


if isinstance(base, int) and isinstance(exponent, int) :
    
    product = (base ** exponent)
    logarithm = (np.log2(base))
    print("\n", base, " to the power of ", exponent, "is: ", product, "\n The logaritm of ", base, "is: ", logarithm)
 
else:
    
    print("Please enter valid numbers")
