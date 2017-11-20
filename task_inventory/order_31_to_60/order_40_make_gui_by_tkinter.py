import tkinter as tk
from tkinter.filedialog import askdirectory

paper = tk.Tk()
# Code to add widgets will go here...

li = ['C','python','php','html','SQL','java']

# listbox = tk.Listbox(paper)
# for item in li:
#     listbox.insert(0, item)

path = tk.StringVar()

def select_path():
    dir = askdirectory()
    path.set(dir)

# 创建entry
# e = tk.StringVar()
# entry = tk.Entry(paper, textvariable=e)
# e.set('input value')
# entry.pack()
#
# text = tk.Text(paper, height=5)
# text.pack()
#
#
# # 定义Button的回调函数
# def hello_button():
#     print(entry.get())
#     print(text.get('1.0', tk.END))
#
#
# tk.Button(paper, text='Hello Button', command=hello_button).pack()

tk.Entry(paper, textvariable=path).grid(row=0, column=0)
tk.Button(paper, text='选择路径', command=select_path).grid(row=0, column=1)

# listbox.pack()
paper.mainloop()
