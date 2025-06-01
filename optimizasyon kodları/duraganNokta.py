import numpy as np

# Amaç fonksiyonu
def f(x):
    return x[0]**2 - 2 * x[0] - 3* x[1]*x[0] + 12 *x[1]

# Amaç fonksiyonunun gradyanı (türevler)
def gradf(x): 
    return [2 * x[0] -2 - 3* x[1], -3 * x[0] + 12]
# Amaç fonksiyonunun Hessian matrisi (ikinci türevler)
def hessianf(x):
    return np.array([[2, -3], [-3, 0]])

# Durağan noktaları ve tiplerini bulma fonksiyonu
def find_stationary_points():
    # Gradf(x) = 0 olduğu noktaları çözmek için
    from sympy import symbols, Eq, solve

    # x1 ve x2'yi sembolik olarak tanımla
    x1, x2 = symbols('x1 x2')
    
    # Gradyanı yazalım
    grad_f1 = 2*(x1 - 1) - x2
    grad_f2 = 2*(x2 - 1) - x1
    
    # Gradyanın sıfır olduğu denklemleri çöz
    eq1 = Eq(grad_f1, 0)
    eq2 = Eq(grad_f2, 0)
    
    # Denklemleri çöz
    stationary_points = solve((eq1, eq2), (x1, x2))
    
    return stationary_points

# Durağan noktaların tiplerini belirleme
def classify_stationary_points():
    stationary_points = find_stationary_points()
    
    for point in stationary_points:
        H = hessianf(point)
        eigvals, _ = np.linalg.eig(H)  # Özdeğerleri hesapla
        
        print(f"Point: {point}")
        print(f"Hessian matrix at point:\n{H}")
        print(f"Eigenvalues: {eigvals}")
        
        if np.all(eigvals > 0):
            print("This point is a minimum.")
        elif np.all(eigvals < 0):
            print("This point is a maximum.")
        else:
            print("This point is a saddle point.")

# Durağan noktaları bul ve tiplerini belirle
classify_stationary_points()
