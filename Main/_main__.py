import wx
import threading
import _MainOperatorFrame
import _SchemeObjects
import _conn


class MainClass:
    def __init__(self):
        pass

    def _main(self):
        self._mainThread()

    def _mainThread(self):
        self.app = wx.App()
        self.frame = _MainOperatorFrame.MainOperatorFrame(None)
        self.frame.Show(True)
        self.app.MainLoop()
