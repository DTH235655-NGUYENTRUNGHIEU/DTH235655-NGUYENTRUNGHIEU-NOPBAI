thang = int(input('nhap vao mot thang: '))
if thang in [1,3,5,7,8,10,12]:
    print('thang có 31 ngay')
elif thang in [4,6,9,11]:
    print('thang co 30 ngay')
elif thang ==2:
    nam = int(input('nhap nam: '))
    if nam % 400 ==0 or nam % 4 == 0 and nam % 100 !=0:
        print('thang co 29 ngay')
    else:
        print('thang co 28 ngay') 

