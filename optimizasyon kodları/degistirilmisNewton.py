import numpy as np

# Fonksiyon
def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2  # Çarpma işlemi düzeltildi

# Gradyan (gradient)
def gradf(x):
    return np.array([ -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0]), 
                      200 * (x[1] - x[0]**2)])

# Hessian matrisi (sabit çünkü kuadratik)
def hessianf(x):
    return np.array([[1200 * x[0]**2 - 400 * x[1] + 2, -400 * x[0]],
                     [-400 * x[0], 200]])

# Pozitif tanımlılık kontrolü
def is_positive_definite(H):
    return np.all(np.linalg.eigvals(H) > 0)

# Line search: sabit adım da kullanabiliriz, örneği basit tutmak için
def line_search(x, p):
    s = 1  # sabit adım
    return s

# Değiştirilmiş Newton Algoritması
def modified_newton(x0, N_max=100, epsilon1=1e-6, epsilon2=1e-6, epsilon3=1e-6):
    x = np.array(x0, dtype=float)
    k = 0

    print(f"Başlangıç noktası x₀ = {x}, f(x₀) = {f(x)}")

    while k < N_max:
        grad = gradf(x)
        H = hessianf(x)

        # Adım 2: Pozitif tanımlı değilse düzelt
        if is_positive_definite(H):
            p = -np.linalg.inv(H) @ grad
        else:
            mu = 0.01
            I = np.eye(len(x))
            H_mod = H + mu * I
            p = -np.linalg.inv(H_mod) @ grad

        # Line search (burada sabit adım alıyoruz)
        s = line_search(x, p)

        # Yeni nokta
        x_new = x + s * p

        # Kontroller
        delta_f = abs(f(x_new) - f(x))
        delta_x = np.linalg.norm(x_new - x)
        norm_grad = np.linalg.norm(gradf(x_new))

        print(f"\nIterasyon {k+1}:")
        print(f"x = {x_new}, f(x) = {f(x_new)}")
        print(f"|Δf| = {delta_f:.2e}, |Δx| = {delta_x:.2e}, ||gradf|| = {norm_grad:.2e}")

        # Sonlandırma kriterleri
        if delta_f < epsilon1:
            print("C2 sağlandı: Fonksiyon değeri değişmiyor.")
            break
        if delta_x < epsilon2:
            print("C3 sağlandı: Değişkenler değişmiyor.")
            break
        if norm_grad < epsilon3:
            print("C4 sağlandı: Yerel minimuma yaklaşıldı.")
            break

        x = x_new
        k += 1

    if k >= N_max:
        print("C1 sağlandı: Maksimum iterasyon sayısına ulaşıldı.")
        
    print(f"\nYaklaşık minimum nokta: x* = {x}, f(x*) = {f(x)}")

# Başlangıç noktası [0, 0]
x0 = [0, 0]
modified_newton(x0)
