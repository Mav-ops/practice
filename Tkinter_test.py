import tkinter as tk
from PIL import Image,ImageTk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("登录界面")
        self.geometry("300x200")

        self.init_widgets()

    def init_widgets(self):
        photo=ImageTk.PhotoImage(Image.open('bg.jpg'))
        self.lbl_img=tk.Label(self,image=photo,width=300,height=50)
        self.lbl_img.image=photo
        self.lbl_img.pack()

        self.frame=tk.Frame(self)

        self.lbl_username=tk.Label(self.frame,text="用户名",anchor=tk.W)
        self.lbl_username.pack(fill=tk.X)

        self.txt_username=tk.Entry(self.frame)
        self.txt_username.pack(fill=tk.X)

        self.lbl_password = tk.Label(self.frame, text="密码", anchor=tk.W)
        self.lbl_password.pack(fill=tk.X)

        self.txt_password = tk.Entry(self.frame,show='*')
        self.txt_password.pack(fill=tk.X)

        self.btn_login=tk.Button(self.frame,text='登录',width=16)
        self.btn_login.pack(side=tk.LEFT,pady=10)
        self.btn_cancle = tk.Button(self.frame, text='取消', width=16,command=lambda:self.destroy())
        self.btn_cancle.pack(side=tk.RIGHT, pady=10)

        self.frame.pack(padx=20,pady=5,fill=tk.X)


if __name__=='__main__':
    app=Application()
    app.mainloop()