__author__ = 'lenovo'
from math import atan2,sqrt,cos
import numpy as np

def var(angleArray, n):
    averageDir = sum(angleArray)/float(n)
    print(averageDir)
    sumValue = sum([pow((angle - averageDir), 2) for angle in angleArray])
    return sqrt(float(sumValue)/n)


arr = [1,2,3,4,5,6,7,8,9,10,10]
arr = [1,1,1,1,1,1,4,5,4,5,1,2]
arr = [80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,22,22,22,22,22,22,22,22]
print(var(arr,len(arr)))