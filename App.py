#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2017-01-06 18:23:55 Friday by wls81>

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
        value = self.tuAPI.get_stock_price('000333')[0]
        self.price_label.configure(text=value)
        self.after(1000, self.update_value)

def main():
    app = Application()
    # 设置窗口标题:
    app.master.title('simple stock monior')
    app.update_value()
    app.mainloop()

if __name__ == "__main__":
    main()
