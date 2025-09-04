n = int(input('nhap n: '))
s =0
for i in range(1,n):
    if n % i == 0:
        s = s + i
if s==n:
    print(n, 'la so hoan hao ')
else:
    print(n,'khong la so hoan hao')