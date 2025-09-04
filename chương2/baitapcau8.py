n = int(input('nhap so nguyen 1<n<9 để in bảng cửu chương : '))
if 1<n<=9:
    print('bảng cửu chương: ',n)
    for i in range(1,11):
        print(n,' x', i,'=', n*i)
else:
    print('so khong hop le!!!!!')

