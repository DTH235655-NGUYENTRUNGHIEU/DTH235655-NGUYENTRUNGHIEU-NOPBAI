import math
x = float(input("nhập x: "))
a = float(input("nhap a: "))
if (a <=0 and a ==1) or x <=0:
    print("nhập lại!!!!!!!!")
    x = float(input("nhập x: "))
    a = float(input("nhap a: "))
logx = math.log(x)/math.log(a)
print("logx= ",logx)
    
