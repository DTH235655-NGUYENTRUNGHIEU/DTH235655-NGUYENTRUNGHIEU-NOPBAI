import math
#a
def demuocnt(n):
    uocnguyento = set()
    for i in range(2,int(math.sqrt(n)+1)):
        while n % i ==0:
            uocnguyento.add(i)
            n = n // i
    if n > 1:
        uocnguyento.add(n)
    return len(uocnguyento)
#b
def uocsots(n):
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong = tong + i
    return tong
n = int(input('nhap n: '))
print('số lượng ước nguyên tố: ',demuocnt(n))
print('tong uoc so: ',uocsots(n))

    
