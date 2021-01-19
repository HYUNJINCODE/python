from tkinter import *
import tkinter.ttk as ttk
import time
root = Tk()
root.title("hyunjin GUI")
root.geometry("640x480")


menu = Menu(root)

def create_new_file():
    print("새파일 만듦")

# file menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window", command=create_new_file)
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_command(label="Save All", state="disable")
menu_file.add_command(label="EXIT", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#edit menu
menu.add_cascade(label="Edit")

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="JAVA")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="LANGUAGE", menu = menu_lang)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(labe="View", menu= menu_view)



root.config(menu=menu)

def btncmd():
    pass
btn = Button(root, text="중지", command=btncmd)
btn.pack()

root.mainloop()
