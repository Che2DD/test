# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:47:58 2019

@author: 111
"""
import tkinter
from tkinter import *
import threading
import temp2

class jiemianlei(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('试验')
        self.int_n = tkinter.IntVar()
        self.int_n2 = tkinter.IntVar()
        self.thelabel = tkinter.Label(self, textvariable=self.int_n).pack()
        self.thelabel = tkinter.Label(self, textvariable=self.int_n2).pack()
        self.mythread = threading.Thread(target=self.work, name='线程_1')
        self.cond = threading.Condition() # 锁
        self.stop = False
        self.mythread.start()
        self.bind('<Destroy>', self.end)
        
    def work(self):
        n=0
        n2='c'
        while 1:
            with self.cond: # 锁
                n = (n+1)%100
                n2= temp2.shuangjiaoshuju()
                self.int_n.set(n) # 修改变量
                self.int_n2.set(n2)
                self.cond.wait(1) # 可以改为 20秒
                if self.stop: break  # 退出线程循环

    def end(self, event):
        with self.cond: # 锁
            self.stop = True  # 设置结束标志
            self.cond.notify()
            
if __name__ == '__main__':
    jiemian = jiemianlei()
    jiemian.mainloop()

