def kiemtra_ngay_thang_nam(day,month,year):
    ngaytrongthang = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if (year % 400 ==0) or (year % 4 == 0 and year % 100 != 0):
        ngaytrongthang[2] = 29
    if year < 1:
        return False
    if month < 1 or month >12:
        return False 
    if day < 1 or day > ngaytrongthang[month]:
        return False
    return True
day = int(input('nhap day: '))
month = int(input('nhap month: '))
year = int(input('nhap year'))
if (kiemtra_ngay_thang_nam(day,month,year)):
    print("hop le")
else:
    print('khong hop le')
    