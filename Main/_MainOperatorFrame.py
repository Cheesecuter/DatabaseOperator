# This file is provided for GUI moudular with basic frame and tree etc.
import wx
import threading
import time
import re
import os
import _conn
import _ConnectFrame
import _InfoFrame
import _OperatorFrame
import _lang
import _FrozenDir


# This class is responsible for the main frame, including the menu and result area.
class MainOperatorFrame(wx.Frame):

    # This method is responsible for initing the main frame.
    def __init__(self, superior):
        self._langType = 'en_US'
        self._lang_ = _lang._Language(self._langType)
        self.srcPath = _FrozenDir.app_path()+r'\\src'
        self._initing(superior)
        pass

    def _initing(self, superior):
        print(self._lang_._mopf_Initing_main_operator_frame)
        wx.Frame.__init__(self, parent=superior,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.SetTitle(self._lang_._mopf_Operator_Frame)
        iconPath = self.srcPath+r'\\icon.png'
        self.SetIcon(wx.Icon(iconPath))
        self.SetSize((900, 700))
        self.Center()
        self.SetOwnBackgroundColour("#b3b3b3")

        self._conn = None

        # init menuBar area
        print(self._lang_._mopf_Initing_menubar)
        self._menuBar()
        print(self._lang_._mopf_Menubar_initiated)

        # init treeCtrl area
        print(self._lang_._mopf_Initing_tree_control)
        self._initTreeCtrl()
        print(self._lang_._mopf_Tree_control_initiated)

        # init Input area
        print(self._lang_._mopf_Initing_input_area)
        self._initInputArea()
        print(self._lang_._mopf_Input_area_initiated)

        # init Result area
        print(self._lang_._mopf_Initing_result_area)
        self._initResultArea()
        print(self._lang_._mopf_Result_area_initiated)

        # init OperatorFrame area
        print(self._lang_._mopf_Initing_operator_frame_button)
        self._initOperatorFrame()
        print(self._lang_._mopf_Operator_frame_button_initiated)

        print(self._lang_._mopf_Operator_frame_initiated)
        pass

    # ******************************************************************
    #   MenuBar
    # ******************************************************************

    # This method is responsible for initing the menubar.
    def _menuBar(self):
        menuBar = wx.MenuBar()

        # file menu
        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, self._lang_._mopf_File)
        _connectM = fileMenu.Append(-1, self._lang_._mopf_Connect)
        self.Bind(wx.EVT_MENU, self._connect_f, _connectM)
        _disconnectM = fileMenu.Append(-1, self._lang_._mopf_Disconnect)
        self.Bind(wx.EVT_MENU, self._disconnect_f, _disconnectM)
        # separate **********************
        fileMenu.AppendSeparator()
        # Placeholder
        """
        _newM = fileMenu.Append(-1, self._lang_._mopf_New)
        self.Bind(wx.EVT_MENU, self._new_f, _newM)
        _openM = fileMenu.Append(-1, self._lang_._mopf_Open)
        self.Bind(wx.EVT_MENU, self._empty, _openM)
        _saveM = fileMenu.Append(-1, self._lang_._mopf_Save)
        self.Bind(wx.EVT_MENU, self._empty, _saveM)
        # separate **********************
        fileMenu.AppendSeparator()
        """
        _exitM = fileMenu.Append(-1, self._lang_._mopf_Exit)
        self.Bind(wx.EVT_MENU, self._exit_f, _exitM)

        # Placeholder
        """
        # edit menu
        editMenu = wx.Menu()
        menuBar.Append(editMenu, self._lang_._mopf_Edit)
        _findM = editMenu.Append(-1, self._lang_._mopf_Find)
        self.Bind(wx.EVT_MENU, self._empty, _findM)

        # view menu
        viewMenu = wx.Menu()
        menuBar.Append(viewMenu, self._lang_._mopf_View)
        """
        # tools menu
        toolsMenu = wx.Menu()
        menuBar.Append(toolsMenu, self._lang_._mopf_Tools)
        _runningSQLM = toolsMenu.Append(-1, self._lang_._mopf_Running_SQL)
        self.Bind(wx.EVT_MENU, self._runningSQL_f, _runningSQLM)
        _language = toolsMenu.Append(-1, self._lang_._mopf_Language)
        self.Bind(wx.EVT_MENU, self._language_f, _language)

        # Placeholder
        """
        # windows menu
        windowsMenu = wx.Menu()
        menuBar.Append(windowsMenu, self._lang_._mopf_Windows)
        """
        # help menu
        helpMenu = wx.Menu()
        menuBar.Append(helpMenu, self._lang_._mopf_Help)
        _aboutM = helpMenu.Append(-1, self._lang_._mopf_About)
        self.Bind(wx.EVT_MENU, self._about_f, _aboutM)

        # set menubar
        self.SetMenuBar(menuBar)

        # Placeholder
        """
        # popup menu
        self.popupMenu = wx.Menu()
        popupMenu1M = self.popupMenu.Append(-1, "Menu 1")
        popupMenu2M = self.popupMenu.Append(-1, "Menu 2")
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnRClick)
        """
        # basic attributes
        self._connInfo = None
        self._connAddress = None
        self._connFlag = False
        pass

    # This method is responsible for create a right click menu.
    def OnRClick(self, event):
        pos = event.GetPosition()
        pos = self.panelResultArea.ScreenToClient(pos)
        self.panelResultArea.PopupMenu(self.popupMenu, pos)
        pass

    # This method is a placeholder.
    def _empty(self, event):
        pass

    # **********************
    # Files menu submenu
    # **********************

    # This method is responsible for connecting to the database.
    def _connect_f(self, event):
        print(self._lang_._mopf_Calling__connect_f)
        if(self._connFlag == True):
            self._disconnecting_f()
        self._connInfo = None
        self._connAddress = None
        self._connectframe = _ConnectFrame.ConnectFrame(None, self._lang_)
        self._connFlag = False
        # call the ConnectFrame class and create a frame for connecting.
        self._connectframe.Show(True)
        self._connecting_f()

        print(self._lang_._mopf_Function__connect_f_is_done)
        print(self._lang_._mopf_Connected_successfully)
        self.resultArea.AppendText(
            self._lang_._mopf_Connected_successfully_1n_1n)
        pass

    # This method is responsible for collecting connecting infomations from the ConnectFrame class.
    def _connecting_f(self):
        self._connArr = self._connectframe._get_conn()
        # Pointer to the connectframe object.
        self._connAddress = self._connArr[1]
        # Basic connecting informations from the ConnectFrame class.
        self._connInfo = self._connArr[0]
        pass

    # This method is responsible for disconnecting from the database.
    def _disconnect_f(self, event):
        print(self._lang_._mopf_Calling__disconnect_f)
        self._disconnecting_f()
        print(self._lang_._mopf_Function__disconnect_f_is_done)
        pass

    # This method is responsible for disconnecting from the database.
    def _disconnecting_f(self):
        print(self._lang_._mopf_Calling__disconnecting_f)
        self._connAddress._disConnect_f()
        self._connectframe._clear_conn()
        self._connAddress = None
        self._connInfo = None
        self._connFlag = False

        self.resultArea.AppendText(
            self._lang_._mopf_Disconnected_successfully_1n_1n)
        print(self._lang_._mopf_Function__disconnecting_f_is_done)
        print(self._lang_._mopf_Disconnected_successfully)
        pass

    # This method is responsible for updating the _connFlag and connecting variables.
    def _connInit_f(self):
        print(self._lang_._mopf_Before_connecting)
        print(self._connInfo)
        print(self._connAddress)
        print(self._lang_._mopf_Calling__runningSQL_f)
        self._connecting_f()
        print(self._lang_._mopf_After_connecting)
        self._connFlag = True
        print(self._connInfo)
        print(self._connAddress)
        pass

    # This method is creating a new file.
    def _new_f(self, event):
        self._schemesInitial()
        pass

    # This method is responsible for exiting from the program.
    def _exit_f(self, event):
        print(self._lang_._mopf_Program_exited_successfully)
        self.Close(True)
        wx.Exit()

    # **********************
    # Tools menu submenu
    # **********************

    # This method is responsible for running sql sentences.

    def _runningSQL_f(self, event):
        if(self._connFlag == False):
            self._connInit_f()
        sql = str(self.inputArea.GetValue())
        print('\n', sql, '\n')
        result = self._connAddress._sql_f(sql)
        for i in result:
            self.resultArea.AppendText(str(i)+'\n')
        self.resultArea.AppendText('\n')
        print(self._lang_._mopf_Function__runningSQL_f_is_done)
        pass

    # This method is responsible for changing the language of the program.
    def _language_f(self, event):
        path = self.srcPath+r'\\langType.txt'
        f = open(path,
                 mode="r", encoding="UTF-8")
        langType = f.readline()
        if(langType == 'en_US'):
            f = open(path,
                     mode="w", encoding="UTF-8")
            f.write('zh_CN')
            print(langType+" => zh_CN")
            self.resultArea.AppendText(
                self._lang_._mopf_Language_Changed_Successfully_1n)
            print(self._lang_._mopf_Language_Changed_Successfully_1n)
            f.close()
        if(langType == 'zh_CN'):
            f = open(path,
                     mode="w", encoding="UTF-8")
            f.write('en_US')
            print(langType+" => en_US")
            self.resultArea.AppendText(
                self._lang_._mopf_Language_Changed_Successfully_1n)
            print(self._lang_._mopf_Language_Changed_Successfully_1n)
            f.close()
        return True

    # **********************
    # Help menu submenu
    # **********************

    # This method is responsible for showing off the basic information of the team.
    def _about_f(self, event):
        print(self._lang_._mopf_Calling__about_f)
        infoframe = _InfoFrame.InfoFrame(None, self._lang_)
        infoframe.Show(True)
        print(self._lang_._mopf_Function__about_f_is_done)
        pass

    # ******************************************************************
    #   InputArea
    # ******************************************************************

    # This method is responsible for initing the input area.
    def _initInputArea(self):
        # panel
        self.panelInputArea = wx.Panel(
            self, -1, pos=(210, 0), size=(700, 225))
        self.panelInputArea.SetBackgroundColour("#cacaca")
        self.inputArea = wx.TextCtrl(parent=self.panelInputArea, style=wx.TE_MULTILINE,
                                     pos=(10, 10), size=(650, 205))
        self.inputArea.SetBackgroundColour("#eeeeee")
        self.inputArea.AppendText(
            self._lang_._mopf_input_area_1ne_g_1nselect__from_emp)
        pass

    # ******************************************************************
    #   ResultArea
    # ******************************************************************

    # This method is responsible for initing the result area.
    def _initResultArea(self):
        # panel
        self.panelResultArea = wx.Panel(
            self, -1, pos=(210, 235), size=(700, 465))
        self.panelResultArea.SetBackgroundColour("#cacaca")
        self.resultArea = wx.TextCtrl(parent=self.panelResultArea, style=wx.TE_MULTILINE | wx.TE_READONLY,
                                      pos=(10, 10), size=(650, 385))
        self.resultArea.SetBackgroundColour("#eeeeee")
        self.resultArea.AppendText(self._lang_._mopf_result_area_1n)
        pass

    # This method is responsible for updating the result area.
    def _updateResultArea(self, result):
        print('result_1\n')
        self.resultArea.AppendText(result)
        print(result)
        print('result_2\n')
        pass

    # ******************************************************************
    #   TreeCtrl
    # ******************************************************************

    # This method is responsible for initing the tree control.
    def _initTreeCtrl(self):
        # panel
        self.panelTreeCtrl = wx.Panel(self, -1, pos=(0, 0), size=(200, 580))
        # self.panelTreeCtrl.SetBackgroundColour("#2fd0c0")
        self.panelTreeCtrl.SetBackgroundColour("#cacaca")
        self.tree = wx.TreeCtrl(parent=self.panelTreeCtrl,
                                pos=(10, 10), size=(180, 570))
        self.tree.SetBackgroundColour("#eeeeee")

        # Init Database Tree Ctrl
        databaseRoot = self.tree.AddRoot(self._lang_._mopf_Database)
        westCampus = self.tree.AppendItem(
            databaseRoot, self._lang_._mopf_WestCampus)
        southCampus = self.tree.AppendItem(
            databaseRoot, self._lang_._mopf_SouthCampus)
        # westCampusInition
        self.InitDatabase(westCampus)
        # southCampusInition
        self.InitDatabase(southCampus)
        pass

    def _OpenOperatorFrame(self, event):
        self._connecting_f()
        self._connAddress = self._connArr[1]
        print(self._connArr[0])
        print(self._connArr[1])
        self._operatorFrame = _OperatorFrame.OperatorFrame(
            None, self._connArr, self._lang_)
        self._operatorFrame.Show(True)
        pass

    # This method is responsible for initing the database tree.
    def InitDatabase(self, root):
        self.Table = self.tree.AppendItem(root, "Table")
        self._tableSpace = self.tree.AppendItem(root, "TableSpace")
        self._view = self.tree.AppendItem(root, "View")
        self._synonym = self.tree.AppendItem(root, "Synonym")
        self._basicTable = self.tree.AppendItem(self.Table, "BasicTable")
        self._indexTable = self.tree.AppendItem(self.Table, "IndexTable")
        self._cluster = self.tree.AppendItem(self.Table, "Cluster")
        self._partition = self.tree.AppendItem(self.Table, "Partition")
        self._externalTable = self.tree.AppendItem(self.Table, "ExternalTable")
        self._objectTable = self.tree.AppendItem(self.Table, "ObjectTable")
        pass

    # ******************************************************************
    #   OperatorFrame
    # ******************************************************************

    # This method is responsible for initing the operator frame button area.
    def _initOperatorFrame(self):
        # panel
        self.panelOperatorPanel = wx.Panel(
            self, -1, pos=(0, 580), size=(200, 120))
        self.openOperatorFrame = wx.Button(parent=self.panelOperatorPanel,
                                           pos=(10, 10), size=(180, 40),
                                           label=self._lang_._mopf_Operator)
        self.Bind(wx.EVT_BUTTON, self._OpenOperatorFrame,
                  self.openOperatorFrame)
        self.panelOperatorPanel.SetBackgroundColour("#cacaca")
        self.openOperatorFrame.SetBackgroundColour("#eeeeee")
        pass

    # ******************************************************************
    # ******************************************************************
    # Methods below are responsible for logic functional operations.
    # ******************************************************************
    # ******************************************************************

    # This method is responsible for selecting all tables from the users connecting to the database.
    def _schemesInitial(self):
        if(self._connFlag == False):
            self._connInit_f()
        sql = """
        select table_name from tabs
        """
        print('\n', sql, '\n')
        tables = str(self._connAddress._sql_f(sql))
        match = re.compile(
            r".*?('(?P<table>.*?)',)", re.S
        )
        result = match.finditer(tables)
        for i in result:
            print(str(i.group("table")))
            self.tree.AppendItem(self._basicTable, str(i.group("table")))
            self.resultArea.AppendText(str(i.group("table"))+'\n')

        self.resultArea.AppendText('\n')
        print(self._lang_._mopf_Function__schemesInitial_is_done)
        pass
