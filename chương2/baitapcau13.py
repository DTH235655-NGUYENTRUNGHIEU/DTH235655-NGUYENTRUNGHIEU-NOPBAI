import math
a = float(input('nhap a (a#0): '))
while a ==0:
    print('không hop le nhập lại!!!')
    a = float(input('nhap a (a#0): '))
b = float(input('nhap b: '))
c = float(input('nhap c: '))

denta = b**2 - 4*a*c
if denta < 0:
        print('phương trình vô nghiệm')
elif denta == 0:
        x = -b/(2*a)
        print('phương trình có nghiệm kép x = ', x)
else:
    x1 = (-b + math.sqrt(denta))
    x2 = (-b - math.sqrt(denta))
    print('phương trình có hai nghiệm phân biệt: x1, x2')
    print('x1 = ', x1)
    print('x2 = ', x2)