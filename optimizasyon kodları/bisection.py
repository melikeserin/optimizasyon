#orjinal fonksiyonun türevinin sıfır olduğu noktayı yani orjinal fonksiyonun minimum noktasını bulur
def bisection(f1,a,b,tolerans = 1e-4):
    # f1 fin birinci türevi
    #a,b başlangıç aralığı
    #tolerans durma şartı 0.0001

    if f1(a) * f1(b) >= 0:
        print("bu aralikta kok yok ya da çift katli kok olabilir")
        return
    while True:
        k = (a+b) / 2.0

        if f1(k) == 0 or abs (b - a) < tolerans:
            return k # kok ya da koke cok yakın bir degeri dondurur
        if f1(k) * f1(a) > 0:
            a = k
        else:
            b = k
        
# f = x^2 - 4x + 6
# f1 = 2x - 4
def f1(x):
    return 2 * x - 4
kok = bisection(f1,0,5) # 0-5 aralık
print("turevin sifir oldugu nokta yaklasik = ",round(kok,6))