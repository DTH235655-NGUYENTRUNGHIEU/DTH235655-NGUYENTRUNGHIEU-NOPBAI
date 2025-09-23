from math import sqrt
print("chương trinh tam giác11111111111")
a = float(input("nhap a>0:"))
b = float(input("nhap b>0:"))
c = float(input("nhap c>0: "))
if (a<=0 or b <= 0 or c<=0) or( a + b <=c) or (b+c<=a) or (c+a<=b):
    print("không phải tam giác")
else:
    cv = a + b + c
    p = cv/2
    dt = sqrt(p*(p-a)*p*(p-b)*p*(p-c))
    print("chu vi: ",cv)
    print( "dien tích: ",dt)