n = int(input('nhap vao so nguyen n (0<=n<=99): '))
chu_so =['','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
#th nhỏ hơn 10
if n < 10:
    print('cách đọc: ', chu_so[n])
else:
    chuc = n // 10
    donvi = n % 10
    #xuli hang chuc
    if chuc == 1: 
        doc = "mười"
    else: 
        doc = chu_so[chuc] + " mươi"
    #Xu li hang dơn vi
    if donvi ==0:
        doc = doc
    elif donvi == 1: 
        doc = doc + " mốt"
    elif donvi == 5:
        doc = doc + " lăm"
    else:
        doc = doc + chu_so[donvi]
print('cách đọc: ',doc)