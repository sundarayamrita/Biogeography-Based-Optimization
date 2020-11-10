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

def F4(x):
    #Multimodal Rastrigin
    A = 10
    n = np.asarray(x).ndim
    return (A * n) + np.sum(np.square(x) - (A * np.cos(2* np.pi * x)))

def F5(x):
    #Multimodal Ackley
    a = 20
    b = 0.2
    c = 2 * np.pi
    n = np.asarray(x).ndim
    sum1 = np.sum(np.square(x))
    sum2 = np.sum(np.cos(c * x))
    exp_sum1 = b * np.sqrt((1 / n) * (sum1))
    exp_sum2 = (1 / n) * sum2

    return a + np.exp(1) - (a * np.exp(-exp_sum1)) - np.exp(exp_sum2)


def getFunctionDetails(a):
    
    # [name, lb, ub, dim]
    param = {  0: ["F1",-100,100,30],
               1: ["F2",-100,100,30],
               2: ["F3",-100,100,30],
               3: ["F4",-100,100,30],
               4: ["F5",-100,100,30],
            }
    # param = {0: ["F1",-100,100,30]}
    return param.get(a, "nothing")



