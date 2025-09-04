def chuyendoithap_nhi(n):
    kq = ""
    while n > 0:
        du = n % 2
        kq = str(du) + kq
        n = n // 2
    return kq

n = int(input('nhap so thap phan n: '))
print('dạng nhị phân: ', chuyendoithap_nhi(n))
