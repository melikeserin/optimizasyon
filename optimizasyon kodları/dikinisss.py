import numpy as np

def f(x):
    return (x[0] - 2 * x [1] + x[2] + 1)**2 + (x[0] + x[1]- x[2] + 3) ** 2 + (-2 * x[0] + x[1] - x[2]) ** 2

def gradf(x):
    return np.array ([12 * x[0] - 6 * x[1] + 4 *x[2] + 8 , - 6* x[0] + 12* x[1] - 8* x[2] +2, -8 * x[0] - 4 * x[1] + 2 * x[2] + 8 ])

# Line search (backtracking)
def line_search(xk, pk, alpha=1.0, rho=0.5, c=1e-4):
    while f(xk + alpha * pk) > f(xk) + c * alpha * np.dot(gradf(xk), pk):
        alpha *= rho
    return alpha

# Dik İniş Algoritması
def steepest_descent(x0, N_max=1000, eps1=1e-6, eps2=1e-6, eps3=1e-8):
    xk = np.array(x0, dtype=float)
    k = 0
    print(f"i: {k}, f(x): {f(xk)}")

    while True:
        grad = gradf(xk)
        pk = -grad
        sk = line_search(xk, pk)
        x_new = xk + sk * pk

        k += 1
        print(f"i: {k}, f(x): {f(x_new)}, ||grad||: {np.linalg.norm(grad)}")

        # Durma kriterleri
        if k >= N_max:
            print("C1: Maksimum iterasyona ulaşıldı.")
            break
        if abs(f(x_new) - f(xk)) < eps1:
            print("C2: Fonksiyon değişimi küçük.")
            break
        if np.linalg.norm(x_new - xk) < eps2:
            print("C3: Değişkenlerde değişim yok.")
            break
        if np.linalg.norm(gradf(x_new)) < eps3:
            print("C4: Yerel minimuma yaklaşıldı.")
            break

        xk = x_new

    print("x* =", xk)
    return xk

# Kullanım
x0 = [0,0,0]
steepest_descent(x0)
