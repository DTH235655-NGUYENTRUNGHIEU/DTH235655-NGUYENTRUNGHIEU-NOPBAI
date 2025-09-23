def BMI(height, weight):
    return weight/(height*height)
def Phanloai(bmi):
    if bmi < 18.5:
        return "gầy"
    elif bmi <= 24.9:
        return "bình thường" 
    elif bmi <= 29.9:
        return "hơi béo"
    elif bmi <=34.9:
        return "béo phì cấp độ 1"
    elif bmi <=39.9: 
        return "béo phì cấp độ 2"
    else:
        return "béo phì cấp độ 3"
def Nguycobenh(bmi):
    if bmi < 18.5:
        return "thấp"
    elif bmi <= 24.9:
        return "trung bình"
    elif bmi <= 29.9:
        return "cao"
    elif bmi <=34.9:
        return "hơi cao"
    elif bmi <=39.9: 
        return "siêu cao"
    else:
        return "siêu siêu cao nguy hiểm"  
#height = float(input("nhập chiều cao: "))
#weight = float(input("nhập cân nặng: "))
print("Nhập vào chiều cao:")
height=float(input())
print("Nhập vào cân nặng:")
weight=float(input())

bmi = BMI(height,weight)
print("mức độ béo phì: ",Phanloai(bmi))
print("mức độ nguy hiểm: ",Nguycobenh(bmi))