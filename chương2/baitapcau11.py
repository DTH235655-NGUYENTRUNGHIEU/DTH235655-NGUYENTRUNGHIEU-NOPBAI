def giaithua(m):
    gt =1
    for i in range(1,m+1):
        gt = gt * i
    return gt
def S(x,n):
    tong = 0
    for j in range (1,n+1):
        tong = x**n/giaithua(n)
    return tong

x = float(input('nhap x: '))
n = int(input('nhap n: '))
print('S','(',x,',',n,')','=',' ',S(x,n))
