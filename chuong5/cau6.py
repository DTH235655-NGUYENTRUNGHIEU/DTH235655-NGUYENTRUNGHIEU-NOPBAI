def NegativeNumberInStrings(s):
    so_am = []
    i =0
    while i < len(s):
        if s[i] =='-' and i+1< len(s) and s[i+1].isdigit():
            so ='-'
            i+=1
            while i <len(s) and s[i].isdigit():
                so +=s[i]
                i+=1
            so_am.append(int(so))
        else:
            i+=1
    if len(so_am)==0:
         print("Không có số âm nào trong chuỗi.")
    else:
        print("Các số âm trong chuỗi là:", so_am)

chuoi = input("Nhập chuỗi bất kỳ: ")
NegativeNumberInStrings(chuoi)