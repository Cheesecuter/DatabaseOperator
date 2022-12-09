import os
import _FrozenDir


class _Language:
    def __init__(self, _language):
        path = _FrozenDir.app_path()+r'\\src\\langType.txt'
        print(path)
        f = open(path,
                 mode="r", encoding="UTF-8")
        langType = f.readline()
        if(langType == 'en_US'):
            print("lang: "+langType)
            self._en_US()
            f.close()
        if(langType == 'zh_CN'):
            print("语言: "+langType)
            self._zh_CN()
            f.close()
        pass

    def _en_US(self):

        # **********************
        # Main Operator Frame (mopf)
        # **********************
        # End messages
        self._mopf_Initing_main_operator_frame = "Initing main operator frame"
        self._mopf_Initing_menubar = "Initing menubar"
        self._mopf_Menubar_initiated = "Menubar initiated"
        self._mopf_Initing_tree_control = "Initing tree control"
        self._mopf_Tree_control_initiated = "Tree control initiated"
        self._mopf_Initing_input_area = "Initing input area"
        self._mopf_Input_area_initiated = "Input area initiated"
        self._mopf_Initing_result_area = "Initing result area"
        self._mopf_Result_area_initiated = "Result area initiated"
        self._mopf_Initing_operator_frame_button = "Initing operator frame button"
        self._mopf_Operator_frame_button_initiated = "Operator frame button initiated"
        self._mopf_Operator_frame_initiated = "Operator frame initiated"
        self._mopf_Calling__connect_f = "Calling _connect_f"
        self._mopf_Function__connect_f_is_done = "Function _connect_f is done"
        self._mopf_Connected_successfully = "Connected successfully"
        self._mopf_Calling__disconnect_f = "Calling _disconnect_f"
        self._mopf_Function__disconnect_f_is_done = "Function _disconnect_f is done"
        self._mopf_Disconnected_successfully = "Disconnected successfully"
        self._mopf_Calling__disconnecting_f = "Calling _disconnecting_f"
        self._mopf_Function__disconnecting_f_is_done = "Function _disconnecting_f is done"
        self._mopf_Before_connecting = "Before connecting"
        self._mopf_Calling__runningSQL_f = "Calling _runningSQL_f"
        self._mopf_After_connecting = "After connecting"
        self._mopf_Program_exited_successfully = "Program exited successfully"
        self._mopf_Function__runningSQL_f_is_done = "Function _runningSQL_f is done"
        self._mopf_Calling__about_f = "Calling _about_f"
        self._mopf_Function__about_f_is_done = "Function _about_f is done"
        self._mopf_Function__schemesInitial_is_done = "Function _schemesInitial is done"
        # Input area messages
        self._mopf_input_area_1ne_g_1nselect__from_emp = "input area\ne.g:\nselect * from emp"
        # Result area messages
        self._mopf_Connected_successfully_1n_1n = "Connected successfully\n\n"
        self._mopf_Disconnected_successfully_1n_1n = "Disconnected successfully\n\n"
        self._mopf_result_area_1n = "result area\n"
        self._mopf_Language_Changed_Successfully_1n = "Language Changed Successfully\nPlease restart the program\n"
        # Tree control area messages
        self._mopf_Database = "Database"
        self._mopf_WestCampus = "WestCampus"
        self._mopf_SouthCampus = "SouthCampus"
        # Menu titles
        self._mopf_File = "File"
        self._mopf_Connect = "Connect"
        self._mopf_Disconnect = "Disconnect"
        self._mopf_New = "New"
        self._mopf_Open = "Open"
        self._mopf_Save = "Save"
        self._mopf_Exit = "Exit"
        self._mopf_Edit = "Edit"
        self._mopf_Find = "Find"
        self._mopf_View = "View"
        self._mopf_Tools = "Tools"
        self._mopf_Running_SQL = "Running SQL"
        self._mopf_Language = "Language"
        self._mopf_Windows = "Windows"
        self._mopf_Help = "Help"
        self._mopf_About = "About"
        # Frame titles
        self._mopf_Operator_Frame = "Operator Frame"
        self._mopf_Operator = "Operator"

        # **********************
        # Business Operator Frame (opf)
        # **********************
        # End messages
        self._opf_Initing_operator_frame = "Initing business operator frame"
        self._opf_Operator_frame_initiated = "Business operator frame initiated"
        self._opf_Initing_main_panel = "Initing main panel"
        self._opf_Main_panel_initiated = "Main panel initiated"
        self._opf_Calling__businessSelector_f = "Calling _businessSelector_f"
        self._opf_Function__businessSelector_f_is_done = "Function _businessSelector_f is done"
        self._opf_Calling__opf_Reapply_f = "Calling _opf_Reapply_f"
        self._opf_Function__opf_Reapply_f_is_done = "Function _opf_Reapply_f is done"
        self._opf_Calling__opf_Cancel_f = "Calling _opf_Cancel_f"
        self._opf_Function__opf_Cancel_f_is_done = "Function _opf_Cancel_f is done"
        self._opf_Calling__opf_Recharge_f = "Calling _opf_Recharge_f"
        self._opf_Function__opf_Recharge_f_is_done = "Function _opf_Recharge_f is done"
        self._opf_Calling__opf_Deduct_f = "Calling _opf_Deduct_f"
        self._opf_Function__opf_Deduct_f_is_done = "Function _opf_Deduct_f is done"
        # Frame titles
        self._opf_Operator_Frame = "Business Operator Frame"
        self._opf_NOT_CONNECTED = "NOT CONNECTED"
        # Panel titles
        self._opf_Student_Number = "Student Number"
        self._opf_Card_Number = "Card Number"
        self._opf_Charge = "Charge"
        self._opf_Loss = "Loss"
        self._opf_Reapply = "Reapply"
        self._opf_Cancel = "Cancel"
        self._opf_Recharge = "Recharge"
        self._opf_Deduct = "Deduct"
        # Prompt Dialog
        self._opf_prompt = "Prompt"
        self._opf_Reapply_Successfully = "Reapply Successfully"
        self._opf_Reapply_Failed = "Reapply Failed"
        self._opf_Account_Not_Cancelled = "Account Not Cancelled"
        self._opf_Cancelled_Successfully = "Cancelled Successfully"
        self._opf_Cancelled_Failed = "Cancelled Failed"
        self._opf_Recharge_Successfully = "Recharge Successfully"
        self._opf_Charge_Not_Valid = "Charge Not Valid"
        self._opf_Recharge_Failed = "Recharge Failed"
        self._opf_Deduct_Successfully = "Deduct Successfully"
        self._opf_Deduct_Failed = "Deduct Failed"

        # **********************
        # Infomation Frame (inff)
        # **********************
        # Frame titles
        self._inff_Infomation = "Infomation"
        self._inff_Database_Operator = "Database Operator"
        self._inff_Version = "Version 0.0.4"
        self._inff_OtherInfo1 = "2004010525"
        self._inff_OtherInfo2 = "HRBUST"

        # **********************
        # Connect Frame (conf)
        # **********************
        # End messages
        self._conf_Account_infomations = "Account infomations:"
        # Frame titles
        self._conf_Connecting_Frame = "Connecting Frame"
        self._conf_Username = "Username"
        self._conf_Password = "Password"
        self._conf_Service = "Service"
        self._conf_Ip_Adress = "Ip Adress"
        # Button titles
        self._conf_Connect = "Connect"

    def _zh_CN(self):

        # **********************
        # 主操作器窗口 (mopf)
        # **********************
        # 终端消息
        self._mopf_Initing_main_operator_frame = "初始化主操作界面"
        self._mopf_Initing_menubar = "初始化菜单栏"
        self._mopf_Menubar_initiated = "菜单栏初始化完成"
        self._mopf_Initing_tree_control = "初始化树形控件"
        self._mopf_Tree_control_initiated = "树形控件初始化完成"
        self._mopf_Initing_input_area = "初始化输入区"
        self._mopf_Input_area_initiated = "输入区初始化完成"
        self._mopf_Initing_result_area = "初始化结果区"
        self._mopf_Result_area_initiated = "结果区初始化完成"
        self._mopf_Initing_operator_frame_button = "初始化子操作器窗口按钮"
        self._mopf_Operator_frame_button_initiated = "子操作器窗口按钮初始化完成"
        self._mopf_Operator_frame_initiated = "操作器窗口初始化完成"
        self._mopf_Calling__connect_f = "调用 _connect_f"
        self._mopf_Function__connect_f_is_done = "函数 _connect_f 调用完成"
        self._mopf_Connected_successfully = "连接成功"
        self._mopf_Calling__disconnect_f = "调用 _disconnect_f"
        self._mopf_Function__disconnect_f_is_done = "函数 _disconnect_f 调用完成"
        self._mopf_Disconnected_successfully = "断开连接成功"
        self._mopf_Calling__disconnecting_f = "调用 _disconnecting_f"
        self._mopf_Function__disconnecting_f_is_done = "函数 _disconnecting_f 调用完成"
        self._mopf_Before_connecting = "连接前"
        self._mopf_Calling__runningSQL_f = "调用 _runningSQL_f"
        self._mopf_After_connecting = "连接后"
        self._mopf_Program_exited_successfully = "程序退出成功"
        self._mopf_Function__runningSQL_f_is_done = "函数 _runningSQL_f 调用完成"
        self._mopf_Calling__about_f = "调用 _about_f"
        self._mopf_Function__about_f_is_done = "函数 _about_f 调用完成"
        self._mopf_Function__schemesInitial_is_done = "函数 _schemesInitial 调用完成"
        # 输入区信息
        self._mopf_input_area_1ne_g_1nselect__from_emp = "输入区\n示例:\nselect * from emp"
        # 结果区信息
        self._mopf_Connected_successfully_1n_1n = "连接成功\n\n"
        self._mopf_Disconnected_successfully_1n_1n = "断开连接成功\n\n"
        self._mopf_result_area_1n = "结果区\n"
        self._mopf_Language_Changed_Successfully_1n = "语言切换成功\n请重启应用程序\n"
        # 树形控件区信息
        self._mopf_Database = "数据库"
        self._mopf_WestCampus = "西校区"
        self._mopf_SouthCampus = "南校区"
        # 菜单标题
        self._mopf_File = "文件"
        self._mopf_Connect = "连接"
        self._mopf_Disconnect = "断开连接"
        self._mopf_New = "新建"
        self._mopf_Open = "打开"
        self._mopf_Save = "保存"
        self._mopf_Exit = "退出"
        self._mopf_Edit = "编辑"
        self._mopf_Find = "查找"
        self._mopf_View = "视图"
        self._mopf_Tools = "工具"
        self._mopf_Running_SQL = "运行 SQL"
        self._mopf_Language = "语言"
        self._mopf_Windows = "窗口"
        self._mopf_Help = "帮助"
        self._mopf_About = "关于"
        # Frame titles
        self._mopf_Operator_Frame = "数据库操作器"
        self._mopf_Operator = "业务办理"

        # **********************
        # 业务办理操作器窗口 (opf)
        # **********************
        # 终端信息
        self._opf_Initing_operator_frame = "初始化业务办理操作器窗口"
        self._opf_Operator_frame_initiated = "业务办理操作器窗口初始化完成"
        self._opf_Initing_main_panel = "初始化主面板"
        self._opf_Main_panel_initiated = "主面板初始化完成"
        self._opf_Calling__businessSelector_f = "调用 _businessSelector_f"
        self._opf_Function__businessSelector_f_is_done = "函数 _businessSelector_f 调用完成"
        self._opf_Calling__opf_Reapply_f = "调用 _opf_Reapply_f"
        self._opf_Function__opf_Reapply_f_is_done = "函数 _opf_Reapply_f 调用完成"
        self._opf_Calling__opf_Cancel_f = "调用 _opf_Cancel_f"
        self._opf_Function__opf_Cancel_f_is_done = "函数 _opf_Cancel_f 调用完成"
        self._opf_Calling__opf_Recharge_f = "调用 _opf_Recharge_f"
        self._opf_Function__opf_Recharge_f_is_done = "函数 _opf_Recharge_f 调用完成"
        self._opf_Calling__opf_Deduct_f = "调用 _opf_Deduct_f"
        self._opf_Function__opf_Deduct_f_is_done = "函数 _opf_Deduct_f 调用完成"
        # 窗口标题
        self._opf_Operator_Frame = "业务办理"
        self._opf_NOT_CONNECTED = "未连接"
        # 面板标题
        self._opf_Student_Number = "学号"
        self._opf_Card_Number = "卡号"
        self._opf_Charge = "金额"
        self._opf_Loss = "挂失"
        self._opf_Reapply = "补办"
        self._opf_Cancel = "注销"
        self._opf_Recharge = "充值"
        self._opf_Deduct = "扣费"
        # 提示框
        self._opf_prompt = "提示"
        self._opf_Reapply_Successfully = "补办成功"
        self._opf_Reapply_Failed = "补办失败"
        self._opf_Account_Not_Cancelled = "账户未注销"
        self._opf_Cancelled_Successfully = "注销成功"
        self._opf_Cancelled_Failed = "注销失败"
        self._opf_Recharge_Successfully = "充值成功"
        self._opf_Charge_Not_Valid = "金额不规范"
        self._opf_Recharge_Failed = "充值失败"
        self._opf_Deduct_Successfully = "扣费成功"
        self._opf_Deduct_Failed = "扣费失败"

        # **********************
        # 关于信息窗口 (inff)
        # **********************
        # 窗口标题
        self._inff_Infomation = "关于"
        self._inff_Database_Operator = "数据库操作器"
        self._inff_Version = "Version 0.0.4"
        self._inff_OtherInfo1 = "2004010525"
        self._inff_OtherInfo2 = "HRBUST"

        # **********************
        # 连接窗口 (conf)
        # **********************
        # 终端信息
        self._conf_Account_infomations = "账号信息:"
        # 窗口标题
        self._conf_Connecting_Frame = "连接窗口"
        self._conf_Username = "用户名"
        self._conf_Password = "密码"
        self._conf_Service = "服务主机"
        self._conf_Ip_Adress = "Ip 地址"
        # 按钮标题
        self._conf_Connect = "连接"
