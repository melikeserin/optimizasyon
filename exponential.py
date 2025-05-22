import numpy as np
import math
from dataset5 import ti,yi

def exponentialIO(t,x):
  yhat = []
  for ti in t:
    toplam = x[0]*math.exp(x[1]*ti)
    yhat.append(toplam)
  return yhat

def error(xk,ti,yi):
  yhat = exponentialIO(ti,xk)
  return np.array(yi) - np.array(yhat)

def findJacobien(traininginput,x):
  numofdata = llen(traininginput)
  J = np.matrix(np.zeros((numofdata,2)))
  for i in range(0, numofdata):
    J[i,0] = -math.exp(x[1]*traininginput[i])
    J[i,1] = -x[0]*traininginput[i]*math.exp(x[1]*traininginput[i])
    return J



