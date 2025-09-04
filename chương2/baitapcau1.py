a = float(input('nhap bao so tien a: '))
tienlai = (a * 0.6)/100
s1 = a
for i in range(1,19,1):
    if i % 6 ==0:
        s1 = s1 + tienlai*6
print('so tien lai 18 thang: ',s1)