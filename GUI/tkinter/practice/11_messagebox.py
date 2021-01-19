from tkinter import *
import tkinter.messagebox as msgbox
import time
root = Tk()
root.title("hyunjin GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예메됨")
def warn():
    msgbox.showwarning("경고", "매진되었다.")
def error():
    msgbox.showerror("에러", "결제 오류 발생")
def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당좌석은 유아동반석입니다. 예매하시겠습니까?")
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack() 



def btncmd():
    pass
btn = Button(root, text="중지", command=btncmd)
btn.pack()

root.mainloop()
