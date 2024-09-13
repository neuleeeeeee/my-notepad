from tkinter import *
from tkinter.filedialog import *

def new_file():
    test_area.delete(1.0,END)

def save_file() :
    f = asksaveasfile(mode = "w", defaultextension=".txt", filetypes=[('Text files', '.txt')])
    f.write(test_save)
    f.close

def maker():
    help_view = Toplevel(window)
    help_view.geometry("300x50")
    help_view.title("만든이")
    lb = Label(help_view, text = "하늘이 만든 메모장입니다.")
    lb.pack()

window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일")
menu_1.add_command(label="저장")
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이")
menu.add_cascade(label="만든이", menu=menu_2)

test_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
test_area.grid(sticky= N + E + S + W)

window.config(menu=menu)
window.mainloop()
