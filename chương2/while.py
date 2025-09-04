a = int(input('nhap so nguyen a: '))
b = int(input('nhap so nguyen b: '))
while a!=b:
    if a >b:
        a =a -b
    else:
        b = b - a
print('uoc so chung lon nhat cua a va b la: ',a)
