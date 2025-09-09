def la_nam_nhuan(nam):
    # Năm nhuận: chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def ngay_trong_thang(thang, nam):
    # Số ngày của từng tháng
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0  # Tháng không hợp lệ

def ngay_ke_tiep(ngay, thang, nam):
    so_ngay = ngay_trong_thang(thang, nam)

    if ngay < so_ngay:
        # Cộng thêm 1 ngày trong cùng tháng
        ngay += 1
    else:
        # Hết tháng → sang tháng mới
        ngay = 1
        if thang == 12:
            thang = 1
            nam += 1
        else:
            thang += 1

    return ngay, thang, nam

# ===== Chương trình chính =====
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

d, m, y = ngay_ke_tiep(ngay, thang, nam)
print("Ngày kế tiếp là: {}/{}/{}".format(d, m, y))