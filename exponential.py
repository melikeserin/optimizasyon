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
