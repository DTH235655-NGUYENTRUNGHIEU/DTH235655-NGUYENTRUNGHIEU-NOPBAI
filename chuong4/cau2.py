from random import randrange
while True: 
    somay = randrange(1,101)
    solandoan =0
    win = False
    while solandoan< 7:
        solandoan+=1
        songuoi = int (input("Máy đoán [1..100], mời bạn đoán:"))
        print("bạn đoán lần thứ: ",solandoan)
        if somay == songuoi:
            print("chúc mừng bạn đã đoán trúng, so máy là = ",somay)
            win = True
            break
        if somay > songuoi:
            print("bạn đoán sai số, số máy > số bạn chọn")
        elif somay < songuoi:
            print("bạn đoán sai số, số máy < số bạn chọn")
    if win == False:
        print("game over!!, số máy = ",somay)
    hoi = input("tiếp không")
    if hoi == "k":
        break 
print("cảm ơn bạn đã tham gia chương trình")


