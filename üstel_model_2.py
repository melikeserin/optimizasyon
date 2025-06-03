import numpy as np
import math
import matplotlib.pyplot as plt

# Örnek veri (gerçek x0=2.5, x1=0.8)
t1 = np.linspace(0, 5, 10)
y1 = 2.5 * np.exp(0.8 * t1) + np.random.normal(0, 0.3, len(t1))

# Üstel model
def exponential10(t, x):
    return [x[0] * math.exp(x[1] * t_i) for t_i in t]

# Hata fonksiyonu
def error(xk, t1, y1):
    yhat = exponential10(t1, xk)
    return np.array(y1) - np.array(yhat)

# Jacobian matrisi
def findJacobian(t1, x):
    J = np.zeros((len(t1), 2))
    for i in range(len(t1)):
        J[i, 0] = -math.exp(x[1] * t1[i])
        J[i, 1] = -x[0] * t1[i] * math.exp(x[1] * t1[i])
    return J

# Gauss-Newton algoritması
def gauss_newton(t1, y1, x_init, iterations=10):
    x = np.array(x_init, dtype=float)
    for _ in range(iterations):
        J = findJacobian(t1, x)
        e = error(x, t1, y1).reshape(-1, 1)
        delta = np.linalg.pinv(J.T @ J) @ J.T @ e
        x = x - delta.ravel()
    return x

# Başlangıç tahmini
x_init = [1.0, 0.5]
x_found = gauss_newton(t1, y1, x_init)

# Tahminler
y_pred = exponential10(t1, x_found)

# Grafik
plt.plot(t1, y1, 'ro', label="Gerçek Veri")
plt.plot(t1, y_pred, 'b-', label="Tahmin (Model)")
plt.title(f"Bulunan Katsayılar: x0={x_found[0]:.2f}, x1={x_found[1]:.2f}")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()




