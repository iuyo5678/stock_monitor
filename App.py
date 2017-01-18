#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2017-01-18 16:57:08 Wednesday by wls81>

from Tkinter import *
from event_engine import *
from api import TushareAPI

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.tuAPI = TushareAPI()
        
    def create_widgets(self):
        self.price_label = Label(self ,width=170,height='40',font='Fixdsys -15', text="")
        self.price_label.pack()

    def update_value(self):
        stock_info = self.tuAPI.get_stock_info('000333')
        if stock_info['price'][0] >= stock_info['open'][0]:
            fg = "red"
        else:
            fg = "green"
        self.price_label.configure(text=stock_info['price'][0], fg=fg)
        self.after(1000, self.update_value)

def main():
    root = Tk()
    # 设置窗口固定再最前面
    root.wm_attributes('-topmost',1)
    app = Application(root)
    # 设置窗口标题:
    app.master.title('simple stock monior')
    app.update_value()
    app.mainloop()

if __name__ == "__main__":
    main()
