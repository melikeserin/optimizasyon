import math

def golden_section_search(f, x_alt, x_ust, delta_x_son):
    tau = 0.38197
    epsilon = delta_x_son / (x_ust - x_alt)
    N = math.ceil(-2.078 * math.log(epsilon))
    k = 0

    # Başlık
    print(f"{'k':<3} {'x₁':<10} {'x₂':<10} {'f(x₁)':<10} {'f(x₂)':<10}")
    print("-" * 50)

    # İlk iki nokta
    x1 = x_alt + tau * (x_ust - x_alt)
    x2 = x_ust - tau * (x_ust - x_alt)
    f1 = f(x1)
    f2 = f(x2)

    # İterasyonlar
    while k < N:
        k += 1
        print(f"{k:<3} {x1:<10.4f} {x2:<10.4f} {f1:<10.4f} {f2:<10.4f}")

        if f1 > f2:
            x_alt = x1
            x1 = x2
            f1 = f2
            x2 = x_ust - tau * (x_ust - x_alt)
            f2 = f(x2)
        else:
            x_ust = x2
            x2 = x1
            f2 = f1
            x1 = x_alt + tau * (x_ust - x_alt)
            f1 = f(x1)

    x_min = (x_alt + x_ust) / 2
    return x_min, f(x_min)

# fonksiyon
def f(x):
    return (x-1)**2*(x-2)*(x-3) 

# Kullanım
x_minimum, f_minimum = golden_section_search(f, 0, 4, 0.0001)

print(f"\nMinimum noktası yaklaşık olarak: x = {x_minimum:.5f}, f(x) = {f_minimum:.5f}")
