# This file is provided for business operator frames and functions.
import wx
import re
import _lang
import _FrozenDir
import _conn


# This class is responsible for initing the operator frame and providing business functions.
class OperatorFrame(wx.Frame):

    # This method is responsible for initing the operator frame.
    def __init__(self, superior, connAddress, lang):
        self._lang_ = lang
        #self._lang_ = _lang._Language('en_US')
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        print(self._lang_._opf_Initing_operator_frame)
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._opf_Operator_Frame)
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((620, 440))
        self.Center()
        self.SetOwnBackgroundColour("#eeeeee")
        self._connAddress = connAddress[1]
        self._cursor = None
        if(self._connAddress == None):
            dlg = wx.MessageDialog(None, self._lang_._opf_NOT_CONNECTED,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            self._initFailed()
        else:
            self._connInfo = connAddress[0]
            self._mainPanel()
        print(self._lang_._opf_Operator_frame_initiated)
        pass

    # This method is responsible for initing the frame while not connected.
    def _initFailed(self):
        # panel
        self.panelMainPanel = wx.Panel(
            self, -1, pos=(0, 0), size=(600, 400))
        self.panelMainPanel.SetBackgroundColour("#cacaca")
        nonConnected = self._lang_._opf_NOT_CONNECTED
        font = wx.Font(18, wx.FONTFAMILY_DEFAULT,
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.mainPanel = wx.StaticText(parent=self.panelMainPanel, id=-1, label=nonConnected,
                                       pos=(10, 10), size=(580, 380),
                                       style=wx.ALIGN_CENTER)
        self.mainPanel.SetFont(font)
        self.mainPanel.SetBackgroundColour("#eeeeee")
        pass

    # This method is responsible for initing the frame while connected.
    def _mainPanel(self):
        print(self._lang_._opf_Initing_main_panel)
        # panel
        self.panelMainPanel = wx.Panel(
            self, -1, pos=(0, 0), size=(600, 400))
        self.panelMainPanel.SetBackgroundColour("#eeeeee")
        self.txtInputStuNo = wx.StaticText(parent=self.panelMainPanel, id=-1,
                                           label=self._lang_._opf_Student_Number,
                                           pos=(10, 10), size=(100, 20))
        self.inputStuNo = wx.TextCtrl(
            parent=self.panelMainPanel, pos=(10, 30), size=(100, 20))
        self.txtInputCardNo = wx.StaticText(parent=self.panelMainPanel, id=-1,
                                            label=self._lang_._opf_Card_Number,
                                            pos=(120, 10), size=(100, 20))
        self.inputCardNo = wx.TextCtrl(
            parent=self.panelMainPanel, pos=(120, 30), size=(100, 20))
        self.businessSelector = wx.Choice(parent=self.panelMainPanel, id=-1, pos=(10, 55), size=(100, 25),
                                          choices=[self._lang_._opf_Loss,
                                                   self._lang_._opf_Reapply,
                                                   self._lang_._opf_Cancel,
                                                   self._lang_._opf_Recharge,
                                                   self._lang_._opf_Deduct])
        self.Bind(wx.EVT_CHOICE, self._businessSelector_f,
                  self.businessSelector)
        self.businessSelector.SetSelection(0)

        self.txtInputCharge = wx.StaticText(parent=self.panelMainPanel, id=-1,
                                            label=self._lang_._opf_Charge,
                                            pos=(230, 10), size=(100, 20))
        self.inputCharge = wx.TextCtrl(
            parent=self.panelMainPanel, pos=(230, 30), size=(100, 20))
        self.inputCharge.SetValue('0')
        print(self._lang_._opf_Main_panel_initiated)
        pass

    def _checkButton_f(self, event):
        pass

    # This method is responsible for creating a choice selector for business.
    def _businessSelector_f(self, event):
        print(self._lang_._opf_Calling__businessSelector_f)
        if(event.GetString() == self._lang_._opf_Loss):
            self._opf_Loss_f()
            print(self._lang_._opf_Loss)
        elif(event.GetString() == self._lang_._opf_Reapply):
            self._opf_Reapply_f()
            print(self._lang_._opf_Reapply)
        elif(event.GetString() == self._lang_._opf_Cancel):
            self._opf_Cancel_f()
            print(self._lang_._opf_Cancel)
        elif(event.GetString() == self._lang_._opf_Recharge):
            self._opf_Recharge_f()
            print(self._lang_._opf_Recharge)
        elif(event.GetString() == self._lang_._opf_Deduct):
            self._opf_Deduct_f()
            print(self._lang_._opf_Deduct)
        print(self._lang_._opf_Function__businessSelector_f_is_done)
        pass

    def _opf_Loss_f(self):
        pass

    # This method is responsible for reapply the card account.
    def _opf_Reapply_f(self):
        print(self._lang_._opf_Calling__opf_Reapply_f)
        self._cursor = self._connInfo.cursor()
        emptyResult = []
        usableID = None
        sql = str("""
        select * from card
        where sno="""+str(self.inputStuNo.GetValue()))
        self._cursor.execute(sql)
        result = self._cursor.fetchall()
        if(result == emptyResult):
            for it in range(100001, 999999):
                sql = str("""
                        select * from card
                        where card_id="""+str(it))
                self._cursor.execute(sql)
                result = self._cursor.fetchall()
                if(result == emptyResult):
                    usableID = it
                    break
                else:
                    continue
            print(usableID)
            sql = """
            insert into card
            values('"""+str(usableID)+"""','""" +\
                str(self.inputStuNo.GetValue())+"""',""" +\
                str(self.inputCharge.GetValue())+""",'""" +\
                """')"""
            print(sql)
            self._cursor.execute(sql)
            self._connInfo.commit()
            self._cursor.close()
            dlg = wx.MessageDialog(None, self._lang_._opf_Reapply_Successfully,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            print(self._lang_._opf_Function__opf_Reapply_f_is_done)
        else:
            print(self._lang_._opf_Reapply_Failed)
            self._cursor.close()
            dlg = wx.MessageDialog(None, self._lang_._opf_Account_Not_Cancelled,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            print(self._lang_._opf_Function__opf_Reapply_f_is_done)
            return
        pass

    # This method is responsible for cancelling the card account.
    def _opf_Cancel_f(self):
        print(self._lang_._opf_Calling__opf_Cancel_f)
        self._cursor = self._connInfo.cursor()
        sql = str("""
                delete from card
                where card_id=(
                select card_id
                from card,student
                where card.sno=student.sno and
                student.sno='"""+str(self.inputStuNo.GetValue())+"""')""")
        try:
            self._cursor.execute(sql)
            self._connInfo.commit()
            self._cursor.close()
            dlg = wx.MessageDialog(None, self._lang_._opf_Cancelled_Successfully,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            print(self._lang_._opf_Function__opf_Cancel_f_is_done)
            pass
        except Exception as e:
            print(self._lang_._opf_Cancelled_Failed)
            self._cursor.close()
            dlg = wx.MessageDialog(None, self._lang_._opf_Cancelled_Failed,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            print(self._lang_._opf_Function__opf_Cancel_f_is_done)
            pass
        pass

    # This method is responsible for recharging to the card account.
    def _opf_Recharge_f(self):
        print(self._lang_._opf_Calling__opf_Recharge_f)
        self._cursor = self._connInfo.cursor()
        sql = str("""
                update card
                set balance=balance+"""+str(self.inputCharge.GetValue()) +
                  """
                where
                sno='"""+str(self.inputStuNo.GetValue())+"""'""")
        try:
            pattern = re.compile(r'^[0-9]*$')
            if(re.match(pattern, str(self.inputCharge.GetValue()))):
                self._cursor.execute(sql)
                self._connInfo.commit()
                self._cursor.close()
                self.inputCharge.SetValue('0')
                dlg = wx.MessageDialog(None, self._lang_._opf_Recharge_Successfully,
                                       self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
                print(self._lang_._opf_Function__opf_Recharge_f_is_done)
                pass
            else:
                dlg = wx.MessageDialog(None, self._lang_._opf_Charge_Not_Valid,
                                       self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
                print(self._lang_._opf_Function__opf_Recharge_f_is_done)
                pass
        except Exception as e:
            print('Recharge failed\n')
            self._cursor.close()
            dlg = wx.MessageDialog(None, self._lang_._opf_Recharge_Failed,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            print(self._lang_._opf_Function__opf_Recharge_f_is_done)
            pass
        pass

    # This method is responsible for deducting charges from the card account.
    def _opf_Deduct_f(self):
        print(self._lang_._opf_Calling__opf_Deduct_f)
        self._cursor = self._connInfo.cursor()
        sql = str("""
                update card
                set balance=balance-"""+str(self.inputCharge.GetValue()) +
                  """
                where
                sno='"""+str(self.inputStuNo.GetValue())+"""'""")
        try:
            pattern = re.compile(r'^[0-9]*$')
            if(re.match(pattern, str(self.inputCharge.GetValue()))):
                self._cursor.execute(sql)
                self._connInfo.commit()
                self._cursor.close()
                self.inputCharge.SetValue('0')
                dlg = wx.MessageDialog(None, self._lang_._opf_Deduct_Successfully,
                                       self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
                print(self._lang_._opf_Function__opf_Deduct_f_is_done)
                pass
            else:
                dlg = wx.MessageDialog(None, self._lang_._opf_Charge_Not_Valid,
                                       self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    dlg.Destroy()
                print(self._lang_._opf_Function__opf_Deduct_f_is_done)
                pass
        except Exception as e:
            print(self._lang_._opf_Deduct_Failed)
            self._cursor.close()
            dlg = wx.MessageDialog(None, self._lang_._opf_Deduct_Failed,
                                   self._lang_._opf_prompt, wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
            print(self._lang_._opf_Function__opf_Deduct_f_is_done)
            pass
        pass
