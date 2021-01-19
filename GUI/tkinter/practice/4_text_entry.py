from tkinter import *

root = Tk()
root.title("hyunjin GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자 입력해라")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만입력해라")
def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 1은 1번째라인 0 은 0 번째 컬럼
    print(e.get())
    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
