from random import randrange
print("chương trình xử lý list!")
n= int(input("nhập số phần tử"))
lst = [0]*n #phần tử bắt đầu bằng 0
for i in range(n):
    lst[i]=randrange(-100,100)
print("danh sách list ngẫu nhiên là: ")
print(lst)
print(" Mời đạo hữu thêm số mới: ")
daohuu = int(input())
lst.append(daohuu)
print(lst)
print("bạn muốn thêm số nào!!!!!")
k = int(input())
dem= lst.count(k)
print(k,"lan xuat hien trong lst",dem)
def kiemtrasnt(n):
    if n <2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True
demsnt =0
tongsnt =0
for y in lst:
    if kiemtrasnt(y):
        demsnt+=1
        tongsnt = tongsnt + y
print("tong sont trong lst: ",tongsnt )
print("so nguyen to trong lst: ",demsnt)

for i in range(len(lst)):
    for j in range(0,len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print("danh sahc sap xep tang dan")
print(lst)

del lst 
print("lst đã bị xóa khỏi bộ nhớ, không thể in ra được")