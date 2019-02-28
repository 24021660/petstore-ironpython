import wx
import sys

class MyFrame(wx.Frame):
    session={}
    def __init__(self,title,size):
        super().__init__(parent=None,title=title,size=size,style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)
        self.Center()
        self.contentpanel=wx.Panel(parent=self)
        self.SetSizeHints(size,size)
        self.Bind(wx.EVT_CLOSE,self.OnClose)

    def OnClose(self,event):
        self.Destroy()
        sys.exit(0)