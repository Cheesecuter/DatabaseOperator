# This file is provided for creating information frame and show informations.
import wx
import _lang
import _FrozenDir


# This class is responsible for providing the information frame with team informations.
class InfoFrame(wx.Frame):
    def __init__(self, superior, lang):
        self._lang_ = lang
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._inff_Infomation)
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((400, 200))
        self.Center()
        # panel
        self.panelInfomationFrame = wx.Panel(
            self, -1, pos=(0, 0), size=(400, 200))
        self.panelInfomationFrame.SetBackgroundColour("#eeeeee")

        self.infomation_line1 = wx.StaticText(parent=self.panelInfomationFrame, label=self._lang_._inff_Database_Operator,
                                              pos=(10, 10), size=(380, 20),
                                              style=wx.ALIGN_CENTER_HORIZONTAL)
        self.infomation_line2 = wx.StaticText(parent=self.panelInfomationFrame, label=self._lang_._inff_Version,
                                              pos=(10, 30), size=(380, 20),
                                              style=wx.ALIGN_CENTER_HORIZONTAL)
        self.infomation_line3 = wx.StaticText(parent=self.panelInfomationFrame, label=self._lang_._inff_OtherInfo1,
                                              pos=(10, 50), size=(380, 20),
                                              style=wx.ALIGN_CENTER_HORIZONTAL)
        self.infomation_line4 = wx.StaticText(parent=self.panelInfomationFrame, label=self._lang_._inff_OtherInfo2,
                                              pos=(10, 70), size=(380, 20),
                                              style=wx.ALIGN_CENTER_HORIZONTAL)
        pass
