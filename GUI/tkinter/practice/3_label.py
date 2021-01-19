from tkinter import *

root = Tk()
root.title("hyunjin GUI")
root.geometry("640x480")
label1 = Label(root, text="안녕하세요")
label1.pack()
photo = PhotoImage(file="GUI/tkinter/practice/check.png")
label2 =Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="이현진 짱")
    global photo2
    # 전역선언하지 않을시 garbage collection 대상이된다.
    photo2 = PhotoImage(file="GUI/tkinter/practice/x.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
