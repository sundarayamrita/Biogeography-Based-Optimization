# -*- coding: utf-8 -*-
"""
Python code of Biogeography-Based Optimization (BBO)
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)
The code template used is similar to code given at link: https://github.com/himanshuRepo/CKGSA-in-Python 
 and matlab version of the BBO at link: http://embeddedlab.csuohio.edu/BBO/software/

Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
@author: Dan Simon (http://embeddedlab.csuohio.edu/BBO/software/)

-- Benchmark Function File: Defining the benchmark function along its range lower bound, upper bound and dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy as np
import math

# define the function blocks
    
def F1(x):
    #Sphere
    return np.sum(np.square(x))

def F2(x):
    #unimodal schwefel
    return np.sum(np.absolute(np.square(x)))
    
def F3(x):
    #Multimodal schwefel
    return np.sum(np.multiply(x, np.sin(x)))

def getFunctionDetails(a):
    
    # [name, lb, ub, dim]
    param = {  0: ["F1",-100,100,30],
               1: ["F2",-100,100,30],
               2: ["F3",-100,100,30],
            }
    # param = {0: ["F1",-100,100,30]}
    return param.get(a, "nothing")



