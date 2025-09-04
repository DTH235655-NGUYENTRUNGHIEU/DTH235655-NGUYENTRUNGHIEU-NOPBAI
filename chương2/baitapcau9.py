n = int(input('nhap so nguyen duong n: '))
if n > 0:
    s = (n*(n+1))/2
    s1 = n**2
    s2 = n*(n+1)
    s3 = (n*(n+1)*(2*n+1))/6
    print('ket qua: s =',s)
    print('ket qua: s1 =',s1)
    print('ket qua: s2 =',s2)
    print('ket qua: s3 =',s3)
else: 
    print('khong hop le!!!!')