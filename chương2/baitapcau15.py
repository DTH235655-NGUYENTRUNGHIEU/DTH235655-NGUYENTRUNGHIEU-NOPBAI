a ,b ,c = map(float,input("nhap 3 so a b c cách nhau bởi dấu chấm phẩy: ").split(";"))
print('a = ',a, 'b = ', b, 'c = ', c)
if a + b > c and b + c > a and c + a >b:
    print('co the tao thanh mot tam giac')
else:
    print('không thể tạo thành mot tam giac')