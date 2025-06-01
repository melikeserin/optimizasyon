import numpy as np
import math
#------------------------------------------------------------------------------
def f(xk): 
    x1 = xk[0]
    x2 = xk[1]    
    fk = (x1-1)** + (x2-1)** - x1*x2
    return fk

def gradient(xk): # fonksiyonun eğimini gösterir. hangi yöne gidersek fonk azalır bunu belirler. yani optimizasyonda yön tayini için önemli
    x1 = xk[0]
    x2 = xk[1]    
    gk = np.array([2*x1-x2, 2*x2-x1])
    return gk

def hessian(xk): #fonksiyonun ikinci türevlerinden oluşan matris. fonksiyonun eğiminin nasıl değiştiğini gösterir
    x1 = xk[0]
    x2 = xk[1]   
    Hk = np.matrix([[ 2, -1], [ -1, 2 ]])
    return Hk    

#def error(xk): #hata vektörü
    x1 = xk[0]
    x2 = xk[1]    
    ek = np.array([ (10*x2-10*x1**2), (1-x1) ])
    return ek

#def jacobian(xk): #hata türevleri
    x1 = xk[0]
    x2 = xk[1]    
    Jk = np.matrix([[-20*x1, 10], [-1, 0]])
    return Jk 
#------------------------------------------------------------------------------

x0 = np.array([1.2, 1.2])  # Başlangıç noktası

print("f(x0) =", f(x0))
print("gradient(x0) =", gradient(x0))
print("hessian(x0) =\n", hessian(x0))
#print("error(x0) =", error(x0))
#print("jacobian(x0) =\n", jacobian(x0))
