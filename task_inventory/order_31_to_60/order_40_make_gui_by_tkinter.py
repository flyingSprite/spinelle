import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory, askopenfilename


class TkTool(object):

    def __init__(self):
        self.paper = tk.Tk()
        self.paper.title('Spinelle Tool')
        # width x hight + offset width x offset hight
        self.paper.geometry('600x400+500+200')
        # set icon
        # self.paper.iconbitmap('spider_128px_1169260_easyicon.net.ico')

        self.selected_path = tk.StringVar()

    def load_image(self, image_path):
        im = Image.open(image_path)
        tkimg = ImageTk.PhotoImage(im)
        lb = tk.Label(self.paper, text="hello", image=tkimg)
        lb.bm = tkimg
        lb.pack(padx=5, pady=5)
        # img = tk.PhotoImage(file=image_path)
        # label = tk.Label(self.paper, text="hello", image=img)
        # label.pack()

    def play_gif(self, gif_path):
        def run_animation():
            while True:
                try:
                    global photo
                    global frame
                    global label
                    photo = tk.PhotoImage(
                        file=gif_path,
                        format="gif - {}".format(frame)
                    )

                    label.configure(image=nextframe)

                    frame = frame + 1

                except Exception:
                    frame = 1
                    break

        photo = tk.PhotoImage(
            file=gif_path,
        )
        label = tk.Label(
            image=photo
        )
        animate = tk.Button(
            self.paper,
            text="animate",
            command=run_animation
        )

        label.pack()
        animate.pack()


    def start(self):
        # Add selector
        # def select_path():
        #     self.selected_path.set(askopenfilename())
        # tk.Entry(self.paper, textvariable=self.selected_path).grid(row=0, column=0)
        # tk.Button(self.paper, text='Select', command=select_path).grid(row=0, column=1)
        #
        # # Add read folder
        # def read_directory():
        #     print(self.selected_path.get())
        # tk.Button(self.paper, text='xxxx', command=read_directory).grid(row=0, column=2)
        self.load_image(u'/Users/Fernando/Desktop/video_gif/DO54Jg5V4AIgycB.gif')
        self.paper.mainloop()


# paper = tk.Tk()
# # Code to add widgets will go here...
#
# li = ['C','python','php','html','SQL','java']
#
# # listbox = tk.Listbox(paper)
# # for item in li:
# #     listbox.insert(0, item)
#
# path = tk.StringVar()
#
# def select_path():
#     dir = askdirectory()
#     path.set(dir)
#
# # 创建entry
# # e = tk.StringVar()
# # entry = tk.Entry(paper, textvariable=e)
# # e.set('input value')
# # entry.pack()
# #
# # text = tk.Text(paper, height=5)
# # text.pack()
# #
# #
# # # 定义Button的回调函数
# # def hello_button():
# #     print(entry.get())
# #     print(text.get('1.0', tk.END))
# #
# #
# # tk.Button(paper, text='Hello Button', command=hello_button).pack()
#
# tk.Entry(paper, textvariable=path).grid(row=0, column=0)
# tk.Button(paper, text='选择路径', command=select_path).grid(row=0, column=1)
#
# # listbox.pack()
# paper.mainloop()

to = TkTool()
to.start()
