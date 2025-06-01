import numpy as np

# Hedef fonksiyon
def f(x):
    return (3+(x[0] -1.5 * x[1])**2 + (x[1]-2)**2)

# Gradyan (gradient) fonksiyonu
def gradf(x):
    return np.array([2*(x[0]-1.5*x[1]), -3*(x[0]-1.5*x[1])+2*(x[1]-2)])

# Başlangıç değerleri
x0 = np.array([-4.5, 3-3.5])
x = x0.copy()
max_iter = 1000
epsilon1 = 1e-8  # |f(x_{k+1}) - f(x_k)|
epsilon2 = 1e-8  # |x_{k+1} - x_k|
epsilon3 = 1e-8  # ||∇f(x)||
k = 0

# İlk gradyan ve yön
gk = gradf(x)
pk = -gk
print(f"i: {k}, f(x): {f(x)}, ||gradf||: {np.linalg.norm(gk)}")

while k < max_iter:
    # Sabit adım uzunluğu (isteğe göre line search yapılabilir)
    s_k = 0.01

    # x güncelle
    x_new = x + s_k * pk

    # Yeni gradyan
    gk_new = gradf(x_new)

    # Konverjans kriterleri
    delta_f = abs(f(x_new) - f(x))
    delta_x = np.linalg.norm(x_new - x)
    norm_grad = np.linalg.norm(gk_new)

    print(f"i: {k+1}, f(x): {f(x_new):.8f}, ||gradf||: {norm_grad:.8f}")

    if delta_f < epsilon1 or delta_x < epsilon2 or norm_grad < epsilon3:
        break

    # Beta hesapla (Fletcher-Reeves)
    beta = np.dot(gk_new, gk_new) / np.dot(gk, gk)

    # Yeni yönü hesapla
    pk = -gk_new + beta * pk

    # Değişkenleri güncelle
    x = x_new
    gk = gk_new
    k += 1

# Sonuç
print("\nOptimal nokta (x*):", x)
print("f(x*):", f(x))
print("İterasyon sayısı:", k)
