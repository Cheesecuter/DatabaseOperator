# This file is provided for creating connecting frame and connecting functions.
import wx
import _lang
import _conn
import _FrozenDir


# This class is responsible for creating a frame for connection with databases.
class ConnectFrame(wx.Frame):
    def __init__(self, superior, lang):
        self._lang_ = lang
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._conf_Connecting_Frame)
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((400, 300))
        self.Center()
        # panel
        self.panelConnectFrame = wx.Panel(
            self, -1, pos=(0, 0), size=(400, 300))
        self.panelConnectFrame.SetBackgroundColour("#eeeeee")

        self.username = wx.StaticText(
            parent=self.panelConnectFrame, label=self._lang_._conf_Username, pos=(10, 10))
        self.inputUserName = wx.TextCtrl(parent=self.panelConnectFrame,
                                         pos=(10, 30), size=(360, 30))
        self.password = wx.StaticText(
            parent=self.panelConnectFrame, label=self._lang_._conf_Password, pos=(10, 60))
        self.inputPassword = wx.TextCtrl(parent=self.panelConnectFrame, style=wx.TE_PASSWORD,
                                         pos=(10, 80), size=(360, 30))
        self.service = wx.StaticText(
            parent=self.panelConnectFrame, label=self._lang_._conf_Service, pos=(10, 110))
        self.inputService = wx.TextCtrl(parent=self.panelConnectFrame,
                                        pos=(10, 130), size=(360, 30))
        self.ipadress = wx.StaticText(
            parent=self.panelConnectFrame, label=self._lang_._conf_Ip_Adress, pos=(10, 160))
        self.inputIpAdress = wx.TextCtrl(parent=self.panelConnectFrame,
                                         pos=(10, 180), size=(360, 30))
        # init connecting informations

        self.inputUserName.SetValue('')
        self.inputPassword.SetValue('')
        self.inputService.SetValue('')
        self.inputIpAdress.SetValue('')

        self.buttonConnect = wx.Button(
            parent=self.panelConnectFrame, label=self._lang_._conf_Connect, pos=(150, 220))
        self.Bind(wx.EVT_BUTTON, self._buttonConnect_f, self.buttonConnect)
        pass

    # This method is responsible for the basic function with the "Connect" button in the connecting frame.
    def _buttonConnect_f(self, event):
        self._get_conn()
        print(self._lang_._conf_Account_infomations)
        print(self._connInfo)
        self.Hide()
        pass

    # This method is responsible for collection the basic connecting informations from the _conn.Collect class.
    def _get_conn(self):
        # connection
        self._connection = _conn.Connect(str(self.inputUserName.GetValue()), str(self.inputPassword.GetValue()),
                                         self.inputIpAdress.GetValue(), '1521', str(self.inputService.GetValue()))
        self._connInfo = self._connection.gl_conn
        self._connAddress = self._connection
        connArr = [self._connInfo, self._connAddress]
        return connArr

    def _clear_conn(self):
        self.inputUserName.SetValue('')
        self.inputPassword.SetValue('')
        self.inputService.SetValue('')
        self.inputIpAdress.SetValue('')
        pass
