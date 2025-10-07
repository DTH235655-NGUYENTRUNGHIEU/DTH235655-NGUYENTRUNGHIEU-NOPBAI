def Laytenfileduoi(path):
    ten_file = path.split("\\")[-1]
    return ten_file

def laytenkhongduoi(path):
    ten_file = Laytenfileduoi(path)      
    tenkhongduoi = ten_file.split(".")[0]  
    return tenkhongduoi


duongdan = input("Nhập đường dẫn bài hát: ")
print("Tên file (có đuôi):", Laytenfileduoi(duongdan))
print("Tên file (không đuôi):", laytenkhongduoi(duongdan))

    