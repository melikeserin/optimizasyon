import numpy as np

def f(x):
    return (x[0] - 2 * x [1] + x[2] + 1)**2 + (x[0] + x[1]- x[2] + 3) ** 2 + (-2 * x[0] + x[1] - x[2]) ** 2
    

def gradf(x): 
    return np.array ([12 * x[0] - 6 * x[1] + 4 *x[2] + 8 , - 6* x[0] + 12* x[1] - 8* x[2] +2, -8 * x[0] - 4 * x[1] + 2 * x[2] + 8 ])


def hessianf(x):
    H = np.array([[12,--6,4], [-6,12,-8], [-8, -4- 2]])
    return H

x = [0,0, 0]
i = 0
print("i:",i,"f(x):",f(x))

loop = True
while loop:
    i += 1
    x = x - 0.01*np.array(gradf(x))
    normGradf = np.linalg.norm(gradf(x))
    print("i:", i,"f(x)", f(x), "//gradf(x)//:", normGradf)
    if normGradf<1e-8:
        loop = False
    
print("x*=", x)

H = hessianf(x)
ozdeger,ozvektor = np.linalg.eig(H)

if min(ozdeger)>0:
    print("x* noktası minimum")
elif max(ozdeger)<0:
    print("x* noktası maksimum")
else:
    print("x* noktası semer")
