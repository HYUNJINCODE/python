from tkinter import *
import tkinter.ttk as ttk
import time
root = Tk()
root.title("hyunjin GUI")
root.geometry("640x480")


# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start()
progressbar.pack()
p_var2 = DoubleVar()
progressbar2 =ttk.Progressbar(root, maximum=100, length=150 ,variable=p_var2)
progressbar2.pack()


def btncmd():
    progressbar.stop()
    for i in range(1,101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())
btn = Button(root, text="중지", command=btncmd)
btn.pack()

root.mainloop()
