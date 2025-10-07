def xulichuoi(s):
    dem_hoa=0
    dem_thuong=0
    dem_so=0
    dem_khoangtrang=0
    dem_dacbiet=0
    dem_nguyenam=0
    dem_phuam=0
    nguyen_am = "aeiouAEIOU"
    
    for ch in s:
        if ch.isupper():
            dem_hoa+=1
        elif ch.islower():
            dem_thuong+=1
        elif ch.isdigit():
            dem_so+=1
        elif ch.ispace():
            dem_khoangtrang+=1
        else:
            dem_dacbiet+=1
        if ch in nguyen_am:
            dem_nguyenam += 1
        elif ch.isalpha():        
            dem_phuam += 1
    print("Số chữ IN HOA:", dem_hoa)
    print("Số chữ in thường:", dem_thuong)
    print("Số chữ là chữ số:", dem_so)
    print("Số ký tự đặc biệt:", dem_dacbiet)
    print("Số ký tự là khoảng trắng:", dem_khoangtrang)
    print("Số chữ Nguyên Âm:", dem_nguyenam)
    print("Số chữ Phụ Âm:", dem_phuam)

s =input("nhập vào 1 ký tự bất kỳ:")
xulichuoi(s)

        