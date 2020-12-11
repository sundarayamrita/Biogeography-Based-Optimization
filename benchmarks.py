import numpy as np
import math

# define the function blocks
    
def F1(x):
    #Sphere
    return np.sum(np.square(x))

def F2(x):
    #Unimodal schwefel
    summation = np.sum(np.absolute(x))
    product = np.prod(np.absolute(x))
    return summation + product
    
def F3(x):
    #Multimodal schwefel
    n = np.asarray(x).ndim
    A = 418.9829
    return (A * n) - np.sum(np.multiply(x, np.sin(np.sqrt(np.absolute(x)))))

def F4(x):
    #Multimodal Rastrigin
    A = 10
    n = np.asarray(x).ndim
    return (A * n) + np.sum(np.square(x) - (A * np.cos(2 * np.pi * x)))

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
    param = {  0: ["F1",-5.12,5.12,3],
               1: ["F2",-100,100,3],
               2: ["F3",-500,500,3],
               3: ["F4",-5.12,5.12,3],
               4: ["F5",-32,32,3],
            }
    # param = {0: ["F1",-100,100,30]}
    return param.get(a, "nothing")



