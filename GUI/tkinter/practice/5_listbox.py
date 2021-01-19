from tkinter import *

root = Tk()
root.title("hyunjin GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "버낸허")
listbox.insert(END, "박수")
listbox.insert(END, "도포")
listbox.pack()
def btncmd():
    listbox.delete(0) # 0번쨰 인덱스 삭제
    #갯수확인
    print("리스트에는", listbox.size(), "개가 있다.")
    #항목확인
    print("1번째 부터 3번째까지의 항목:" , listbox.get(0,2))
    #선택된 항목확인
    print("선택된 항목은" , listbox.curselection())
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
