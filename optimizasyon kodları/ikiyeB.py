def f1(x):
    f1 = 2*(x-1)*(x-2)*(x-3) + (x-1)**2*(2*x-5)
    return f1

xa = -2
xb = 5

if f1(xa)*f1(xb)<0:
    print("noktalar doğru seçildi")

    while abs(xa-xb)>1e-10:
        ortanokta = (xa + xb)/2
        if f1(ortanokta) * f1(xa)>0:
            xa = ortanokta
        else:
            xb = ortanokta
        print(xa,xb,ortanokta,abs(xa-xb))
else:
    print("dogru noktalar seç")