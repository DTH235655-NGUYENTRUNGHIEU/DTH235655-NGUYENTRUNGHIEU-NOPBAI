from tkinter import*
from tkinter import messagebox
root = Tk()

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

def cong():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a+b)

def tru():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a-b)

def nhan():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a*b)

def chia():
    a = float(stringA.get())
    b = float(stringB.get())
    if b==0:
        messagebox.showerror("nhập sai","b không được bằng 0")
    else:
        stringKQ.set(a/b)

root.minsize(height=150,width=250)
root.title("cộng trừ nhân chia")

Label(root,text="cộng trừ nhân chia",fg="blue",font=("tahoma",18)).grid(row=0,columnspan=3)

Label(root,text= "số a: ").grid(row=1,column=1)
Entry(root,width=18,textvariable=stringA).grid(row=1,column=2)

Label(root,text="số b: ").grid(row=2,column=1)
Entry(root,width=18,textvariable=stringB).grid(row=2,column=2)

Label(root,text="kết quả: ").grid(row=3,column=1)
Entry(root,width=18,textvariable=stringKQ).grid(row=3,column=2)


frameButton = Frame(root) #khung chứa các button,entry,label

Button(frameButton,text="Cộng",command=cong).pack(side=TOP,fill=X)
Button(frameButton,text="Trừ",command=tru).pack(side=TOP,fill=X)
Button(frameButton,text="Nhân",command=nhan).pack(side=TOP,fill=X)
Button(frameButton,text="Chia",command=chia).pack(side=TOP,fill=X)

frameButton.grid(row=1,column=0,rowspan=4)

Button(frameButton,text="Thoát",command=root.quit).pack(side= TOP,fill=X)

root.mainloop()



