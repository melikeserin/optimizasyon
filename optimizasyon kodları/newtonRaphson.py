# f'(x) = 0 sağlayan x değerini bulmak yani minimum ya da maksimum noktayı
x = 0.5 # başlangıç noktası
# f(x) = (x - 1)^2 * (x - 2) * (x - 3)
f = (x - 1)**2 * (x - 2) * (x - 3)  # f(x)
f1 = 2 * (x - 1) * (x - 2) * (x - 3) + (x - 1)**2 * (2*x - 5)  # f(x)in birinci türevi
f2 = 2 * (x - 2) * (x - 3) + 4 * (x - 1) * (2*x - 5) + 4 * (x - 1)**2  # f(x)in ikinci türevi
dx = -f1 / f2  # newton raphson güncelleme değeri 
iteration = 0 
print(iteration, " x:",round(x,4)," f:",round(f,4)," f1:",round(f1,4)," f2:",round(f2,4)," dx:",round(dx,4),) # ilk durum
while abs(f1) > 1e-10: #neredeyse sıfır olana kadar 10 üzere -10 demek
    iteration += 1
    x = x + dx # x değerinin güncellenmesi
    # yeni değerler
    f = (x - 1)**2 * (x - 2) * (x - 3)         
    f1 = 2 * (x - 1) * (x - 2) * (x - 3) + (x - 1)**2 * (2*x - 5) 
    f2 = 2 * (x - 2) * (x - 3) + 4 * (x - 1) * (2*x - 5) + 4 * (x - 1)**2 
    dx = -f1 / f2
    # sonuçlar
    print(iteration, " x:",round(x,4)," f:",round(f,4)," f1:",round(f1,4)," f2:",round(f2,4)," dx:",round(dx,4),)
print(f"\nminimum veya sabit nokta bulundu x = {x:.4f}")

if f2 > 0:
    print("yerel minimumdur")
elif f2 < 0:
    print("yerel maksimumdur")
else:
    print("saddle point")



