def checkdoixung(s):
    flag = True
    for i in range (len(s)):
        if s[i]!= s[len(i)-i-1]:
            flag = False
            break
    return flag
def main():
    print("nhập một chuỗi: ")
    s = input()
    if(checkdoixung):
        print("chuỗi của bạn đối xúng")
    else: 
        print("chuỗi của ban không dối xứng")
while True:
        main()
        print("Tiếp không Thím?(c/k):")
        s=input()
        if s=="k":
            break
print("CÁM ƠN THÍM")