n = int(input('nhap n: '))
#a 
print('ketqua: ',n*(2*n+1))
#b
tongsl = 0
for i in range(1,n):
    if i % 2 !=0:
        tongsl = tongsl + i
print('tong so le nho hon n: ',tongsl)
#c
tongsc = 0
for i in range(1,n):
    if i % 2 ==0:
        tongsc = tongsc + i
print('tong so chan nho hon n: ',tongsc)

