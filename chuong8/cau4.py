from tkinter import *

# Tạo cửa sổ chính
root = Tk()
root.title("Máy tính bỏ túi")
root.minsize(width=250, height=300)

# Biến chuỗi hiển thị trên ô kết quả
stringKQ = StringVar()

# ===== Frame cho ô hiển thị =====
frameDisplay = Frame(root)
frameDisplay.pack(side=TOP, fill=X, padx=5, pady=5)

# Ô hiển thị kết quả
txtDisplay = Entry(frameDisplay, textvariable=stringKQ, font=("Arial", 16), justify='right')
txtDisplay.pack(fill=X)

# ===== Frame cho các nút bấm =====
frameButton = Frame(root)
frameButton.pack(side=TOP, fill=BOTH, expand=True)

# Biến lưu biểu thức
expression = ""

# Hàm xử lý khi bấm phím số hoặc phép toán
def press(num):
    global expression
    expression += str(num)
    stringKQ.set(expression)

# Hàm tính kết quả
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        stringKQ.set(total)
        expression = total
    except:
        stringKQ.set("Lỗi")
        expression = ""

# Hàm xóa toàn bộ
def clear():
    global expression
    expression = ""
    stringKQ.set("")

# ===== Tạo các nút số và phép toán =====
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('-', 4, 0), ('0', 4, 1), ('.', 4, 2),
    ('+', 5, 0), ('*', 5, 1), ('/', 5, 2),
]

for (text, row, col) in buttons:
    Button(frameButton, text=text, width=5, height=2,
           command=lambda t=text: press(t)).grid(row=row, column=col, padx=2, pady=2)

# Nút "="
Button(frameButton, text='=', width=16, height=2, bg='lightblue',
       command=equalpress).grid(row=6, column=0, columnspan=3, pady=3)

# Nút "Clr"
Button(frameButton, text='Clr', width=16, height=2, bg='lightcoral',
       command=clear).grid(row=7, column=0, columnspan=3, pady=3)

root.mainloop()
