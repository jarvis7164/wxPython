'''
-*- coding: utf-8 -*-
@Author  : Jarvis
@Time    : 2021/5/28 11:31
@Software: PyCharm
@File    : wxPython.py
'''

import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title='第一个GUI程序！', size=(300, 180))
        self.Center()    # 设置窗口居中
        panel = wx.Panel(parent=self)  # 创建面板对象，父容器未Frame窗口对象
        self.statictext = wx.StaticText(parent=panel, pos=(110,15))  # 创建静态文本对象
        b1 = wx.Button(parent=panel, id=10, label='button1', pos=(100,45))
        b2 = wx.Button(parent=panel, id=11, label='button2', pos=(100,85))
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)  # 绑定事件，self是当前窗口对象，第一个参数是事件类型，第二个参数是事件处理者，第三个参数是事件源
        self.Bind(wx.EVT_BUTTON, self.on_click, id=11)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('应用程序推出')
        return 0

if __name__ == '__main__':
    app = App()
    app.MainLoop()   # 进入主事件循环