a = int(input('nhap so nguyen a: '))
b = int(input('nhap so nguyen b: '))
ch = input('nhap vao cac ky tu (+,-,*,/): ')
if ch == '+':
    print('a + b =: ',a+b)
elif ch =='-':
    print('a - b=: ', a-b)
elif ch == '*':
    print('a * b =',a*b )
elif ch == '/':
    if b!=0:
        print('a / b = ',a/b)
    else:
        print('khong chia duoc')
else:
    print('ky tu ch khong phai mot toan tu!!')