import numpy as np
import math as mt

def MF(i):
    opt = np.zeros(i+2)
    opt[0] = 0
    opt[1] = 1
    opt[2] = 1
    for j in range(2,i):
        opt[j] = mt.pow(opt[j-1],0.5) + mt.pow(opt[j-2],1.1)
    return opt[i-1]

print(MF(100))