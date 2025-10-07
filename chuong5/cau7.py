def toiuuchuoi(s):
    s =s.strip()
    words = s.split()
    words_chuan = [word.capitalize() for word in words]
    ket_qua = ' '.join(words_chuan)
    return ket_qua
chuoi = input("Nhập chuỗi danh tu: ")
print("Chuỗi sau khi tối ưu:", toiuuchuoi(chuoi))