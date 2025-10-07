def ROI(dt,cp):
    return (dt - cp)/cp
def GoiYDauTu(roi):
    if roi>=0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
    
print("chương trình tính roi!!")
dt = int(input("nhập doanh thu: "))
cp = int(input("nhập chi phí: "))
roi = ROI(dt,cp)
print("tỉ lệ roi",roi)
print("==>",GoiYDauTu(roi)) 

