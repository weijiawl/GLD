#!/usr/bin/python
#-*- coding: UTF-8 -*-
import win32com.client
import do
import rk
import configparser
import datetime
import os
import re
import time
import xg
import random
import tk
import threading
xiaoguo = xg.xgdx()
damo = do.bw()
tk_wins = threading.Thread(target=tk.win)
tk_wins.start()
WMI = win32com.client.GetObject('winmgmts:')
class account_value:
    def __init__(self, hao="", mi="", daqu="", zongjuese="", dangqianjuesi="",zhanghaobianhao="",zhanghaozongshu=""):
        self.hao = hao
        self.mi = mi
        self.daqu = daqu
        self.zongjuese = zongjuese
        self.dangqianjuese = dangqianjuesi
        self.zhanghaobianhao = zhanghaobianhao
        self.zhanghaozongshu = zhanghaozongshu
    def get_value(self):
        return self.hao, self.mi, self.daqu, self.zongjuese, self.dangqianjuese
account = account_value()
def remove_option(path,section, option):
    try:
        cf = configparser.ConfigParser()
        cf.read(path)
        cf.remove_option(section,option)
        cf.write(open(path, "w"))
    except:
        print('删除键失败')
def set_ini_n(path,option,strs):
    sr = ""
    with open(path, 'r') as f:
        for i in f.readlines():
            if i.find(option) > -1:
                sr = sr + option + '=' + strs + '\n'
                print(i)
            else:
                sr = sr + i
    with open(path, 'w') as fi:
        fi.write(sr)
def jiluwanchengshijian():
    num = get_ini("config/记录.ini", "刷号记录", "当前账号")
    juese = get_ini("config/记录.ini", "刷号记录", "当前角色")
    qu  = get_ini("config/记录.ini", "刷号记录", "当前大区")
    date = datetime.datetime.now()
    set_ini('config/记录.ini', '完成时间', num + '_' + qu + '_' + juese, date.strftime('%Y-%m-%d %H:%M:%S'))
def jiluwanchengshijian_zhuanqian():
    num = get_ini("config/记录.ini", "刷号记录", "当前账号")
    set_ini('config/记录.ini', '转账', num,'完成')
def get_pc_name():
    return os.environ['COMPUTERNAME']
def prints(strs):
    try:
        tk.text(strs)
        # with open('config/日志.txt', 'a+') as f:
        #     f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '#编号=(' + account.zhanghaobianhao +')=' +account.hao+ '=' + account.mi + '=' + account.daqu + '=' + account.dangqianjuese + '/' + account.zongjuese + '=' +'【' + strs + '】' + '\n')
        #print(datetime.datetime.now().strftime("%H:%M") + '#编号=(' + account.zhanghaobianhao +')=' +account.hao+ '=' + account.mi + '=' + account.daqu + '=' + account.dangqianjuese + '/' + account.zongjuese + '=' +'【' + strs + '】')
    except:
        print("报错######打印信息失败")
def shuaxinliebiao():
    tk.trickit()
def get_ini(name, section, option):
    try:
        cf = configparser.ConfigParser()
        cf.read(name)
        temp = cf.get(section, option)
        return temp
    except:
        return ""
def set_ini(name, section, option, strs):
    try:
        cf = configparser.ConfigParser()
        cf.read(name)
        if cf.has_section(section) == False:
            cf.add_section(section)
        cf.set(section, option, strs)
        cf.write(open(name, "w"))
        return 1
    except:
        return 0
def check_exsit(process_name):
    try:
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
        if len(processCodeCov) > 0:
            return 1
        else:
            return 0
    except:
        return 0
def end_exsit(LeiXing):
    # try:
    #     if LeiXing == 0:
    #         os.system('TASKKILL /F /IM Login.exe"')
    #     elif LeiXing == 1:
    #         os.system('TASKKILL /F /IM DNF.exe"')
    #     elif LeiXing == 2:
    #         os.system('TASKKILL /F /IM DNF.exe"')
    #         os.system('TASKKILL /F /IM tgp_daemon.exe"')
    #         os.system('TASKKILL /F /IM TPHelper.exe"')
    # except:
    #     prints("报错######关闭进程失败")
    try:
        if LeiXing == 0:
            a = damo.EnumProcesspy('Login.exe')
            if a != '':
                arr = a.split(',')
                for i in arr:
                    damo.TerminateProcesspy(i)
        elif LeiXing == 1:
            a = damo.EnumProcesspy('DNF.exe')
            if a != '':
                arr = a.split(',')
                for i in arr:
                    damo.TerminateProcesspy(i)
        elif LeiXing == 2:
            a = damo.EnumProcesspy('DNF.exe')
            if a != '':
                arr = a.split(',')
                for i in arr:
                    damo.TerminateProcesspy(i)
            a = damo.EnumProcesspy('tgp_daemon.exe')
            if a != '':
                arr = a.split(',')
                for i in arr:
                    damo.TerminateProcesspy(i)
            a = damo.EnumProcesspy('TPHelper.exe')
            if a != '':
                arr = a.split(',')
                for i in arr:
                    damo.TerminateProcesspy(i)
    except:
        prints("报错######关闭进程失败")
def riqibijiao(p_now):
    try:
        d1 = datetime.datetime.strptime(p_now, '%Y-%m-%d %H:%M:%S')
        d2 = datetime.datetime.now()
        return d2.__gt__(d1)
    except:
        prints("报错######比较时间失败")
        input()
def gengxin(p_now):
    try:
        d1 = datetime.datetime.strptime(p_now, '%Y-%m-%d %H:%M:%S')
        d2 = datetime.datetime.now()
        days = d2.day - d1.day
        if days > 1:
            return True
        if days == 1:
            if d2.hour >= 6:
                return True
        if days == 0:
            if d1.hour < 6:
                if d2.hour >= 6:
                    return True
        return False
    except:
        prints("报错######更新时间失败")
        input()
def fenghaochaxun(num):
    p_now = get_ini("config/记录.ini", "封号", num)
    if p_now != "":
        temp = riqibijiao(p_now)
        if temp:
            remove_option("config/记录.ini", "封号", num)
            return True
        return False
    else:
        return True
def zhicaichaxun(num):
    p_now = get_ini("config/记录.ini", "制裁", num)
    if p_now != "":
        temp = riqibijiao(p_now)
        if temp:
            remove_option("config/记录.ini", "制裁", num)
            return True
        return False
    else:
        return True
def zhuanzhangchaxun(num):
    p_now = get_ini("config/记录.ini", "转账", num)
    if p_now != "":
        return False
    return True
def wanchengchaxun(num):
    p_now = get_ini("config/记录.ini", "完成", num)
    if p_now != "":
        return False
    return True
def get_account(path):
    prints("获取账号")
    try:
        pc_name = get_pc_name()
        for ic in range(500):
            num = get_ini(path,pc_name,str(ic + 1))
            if num != "":
                arr = num.split("=")
                hao = arr[0]
                juese = arr[3]
                #检查封号
                if fenghaochaxun(hao) and zhicaichaxun(hao) and wanchengchaxun(hao+'_'+arr[2]):
                    #逐角色判断时间
                    for i in range(int(juese)):
                        returns_now = get_ini('config/记录.ini', '完成时间', hao + '_' + arr[2] + '_' + str(int(i) + 1))
                        if returns_now != "":
                            if gengxin(returns_now) == True:
                                set_ini("config/记录.ini", "刷号记录", "当前账号", arr[0])
                                set_ini("config/记录.ini", "刷号记录", "当前大区", arr[2])
                                set_ini("config/记录.ini", "刷号记录", "当前角色数", arr[3])
                                set_ini("config/记录.ini", "刷号记录", "当前角色", str(int(i) + 1))
                                account.hao, account.mi, account.daqu, account.zongjuese, account.dangqianjuese, \
                                    account.zhanghaobianhao = \
                                    arr[0],arr[1],arr[2],arr[3],str(int(i) + 1),str(ic + 1)
                                return arr[0],arr[1],arr[2],str(int(i) + 1)
                        else:
                            set_ini("config/记录.ini", "刷号记录", "当前账号", arr[0])
                            set_ini("config/记录.ini", "刷号记录", "当前大区", arr[2])
                            set_ini("config/记录.ini", "刷号记录", "当前角色数", arr[3])
                            set_ini("config/记录.ini", "刷号记录", "当前角色", str(int(i) + 1))
                            account.hao, account.mi, account.daqu, account.zongjuese, account.dangqianjuese, \
                                account.zhanghaobianhao= arr[0], arr[1], arr[2], arr[3], \
                                str(int(i) + 1), str(ic + 1)
                            return arr[0], arr[1], arr[2], str(int(i) + 1)
                    #完成
                    set_ini("config/记录.ini", "完成", arr[0]+'_'+arr[2],  '完成')
            else:
                return "", "", "", ""
    except:
        prints("报错######获取账号失败")
        input()
def get_account_zhuanqian(path):
    prints("获取账号")
    try:
        pc_name = get_pc_name()
        for ic in range(500):
            num = get_ini(path,pc_name,str(ic + 1))
            if num != "":
                arr = num.split("=")
                hao = arr[0]
                juese = arr[3]
                #检查封号
                if fenghaochaxun(hao) and zhuanzhangchaxun(hao):
                    set_ini("config/记录.ini", "刷号记录", "当前账号", arr[0])
                    set_ini("config/记录.ini", "刷号记录", "当前大区", arr[2])
                    set_ini("config/记录.ini", "刷号记录", "当前角色数", arr[3])
                    set_ini("config/记录.ini", "刷号记录", "当前角色", str(1))
                    account.hao, account.mi, account.daqu, account.zongjuese, account.dangqianjuese,account.zhanghaobianhao= arr[0], arr[1], arr[2], arr[3],str(1), str(ic + 1)
                    return arr[0], arr[1], arr[2], str(1)
                #完成
            else:
                return "", "", "", ""
    except:
        prints("报错######获取账号失败")
        input()
def juesechuli(leixing):
    prints("角色界面处理")
    #每次换角色都要按赛丽亚房间的键
    #set_ini('config/功能键设置.ini', '飞机功能键', '赛丽亚房间按键开关', "True")
    try:
        # t_gangtie = 192
        # t_gelandi = 104
        # dengji_gld = get_ini('config/cfg.ini', '游戏配置', "等级上限")
        # dengji_gt = get_ini('config/cfg.ini', '游戏配置', "等级上限_钢铁")
        zongjuese = get_ini('config/记录.ini', '刷号记录', "当前角色数")
        juese = get_ini('config/记录.ini', '刷号记录', "当前角色")
        qu = get_ini("config/记录.ini", "刷号记录", "当前大区")
        hao = get_ini("config/记录.ini", "刷号记录", "当前账号")
        p_x =[70,192,314,436,70,192,314,436]
        p_y =[256,256,256,256,464,464,464,464]
        juese_time = datetime.datetime.now()
        while True:
            FinStr = damo.FindStrEpy(507, 531, 593, 564, "结束游戏", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                break
            else:
                damo.KeyPresspy(27)
                damo.Delaypy(3000)
                FinStr = damo.FindStrEpy(360, 459, 413, 477, "选择角色", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    damo.MoveTopy(intx + 10, inty - 10)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(5000)
            damo.Delaypy(1000)
            juese_time_now = datetime.datetime.now()
            time_temp = juese_time_now.minute - juese_time.minute
            if time_temp > 3:
                qingkongyouxichuangkou()
                return 3
        damo.MoveTopy(1, 1)
        damo.Delaypy(1000)
        #1 = 上角色,2 = 换角色
        if leixing == 2:
            juese = str(int(juese) + 1)
            if int(juese) > int(zongjuese):
                return 0
        #判断当前角色前面的角色是否更新疲劳
        for i in range(int(juese)):
            returns_now = get_ini('config/记录.ini', '完成时间', hao + '_' + qu + '_' + str(int(i) + 1))
            if returns_now != "":
                if gengxin(returns_now) == True:
                    juese = str(i + 1)
                    break
            else:
                juese = str(i+1)
        while True:
            FinStr = damo.FindStrEpy(507, 531, 593, 564, "结束游戏", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if int(juese) <= 8:
                    juese_index = 1
                    #上拉
                    for i in range(3):
                        damo.MoveTopy(579, 92)
                        damo.Delaypy(200)
                        damo.LeftDoubleClickpy()
                        damo.Delaypy(500)
                elif int(juese) <= 12:
                    juese_index = 5
                    # 上拉
                    for i in range(5):
                        damo.MoveTopy(579, 92)
                        damo.Delaypy(200)
                        damo.LeftDoubleClickpy()
                        damo.Delaypy(500)
                    # 下拉一下
                    damo.MoveTopy(579, 495)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(1000)
                elif int(juese) <= 16:
                    juese_index = 9
                    # 上拉
                    for i in range(5):
                        damo.MoveTopy(579, 92)
                        damo.Delaypy(200)
                        damo.LeftDoubleClickpy()
                        damo.Delaypy(500)
                    damo.MoveTopy(579, 495)
                    damo.Delaypy(1000)
                    # 下拉二下
                    damo.LeftClickpy()
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                #等级检查关闭，不到84自动练级
                #检查等级
                # lv = damo.Ocrpy(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index], p_x[int(juese) - juese_index] + 60,p_y[int(juese) - juese_index] + 18, "d1b994-000000", 1)
                # if lv != "":
                #     lv = re.sub("\D", "", lv)
                #     # 地图分配
                #     if int(lv) >= int(dengji_gt):
                #         set_ini('config/记录.ini', '地图', "地图ID", str(t_gangtie))
                #         damo.MoveTopy(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index])
                #     elif int(lv) >= int(dengji_gld):
                #         set_ini('config/记录.ini', '地图', "地图ID", str(t_gelandi))
                #         damo.MoveTopy(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index])
                #     else:
                #         set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                #         account.dangqianjuese = juese
                #         prints("等级不够卡图，换下个角色")
                #         juese = str(int(juese) + 1)
                #         if int(juese) > int(zongjuese):
                #             set_ini("config/记录.ini", "完成", hao + '_' + qu, '完成')
                #             return 0
                #         continue
                #点击角色
                damo.MoveTopy(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index])
                damo.Delaypy(500)
                damo.LeftDoubleClickpy()
                damo.Delaypy(500)
                #点击开始
                damo.MoveTopy(402, 548)
                damo.Delaypy(200)
                damo.LeftDoubleClickpy()
                damo.Delaypy(5000)
            FinStr = damo.FindStrEpy(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = damo.FindPicEpy(365, 356, 418, 384, "签到.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = damo.FindStrEpy(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = damo.FindPicEpy(768, 1, 800, 31, "图外.bmp|图外1.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            # FinStr = damo.FindPicEpy(768, 1, 800, 31, "图内.bmp", "000000", "0.9", 0)
            # pos = FinStr.split('|')
            # if int(pos[1]) > 0:
            #     account.dangqianjuese = juese
            #     set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
            #     return 1
            FinStr = damo.FindStrEpy(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 2
            FinStr = damo.FindPicEpy(242, 430, 316, 490, "金麦克.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty - 10)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                damo.KeyPresspy(27)
                damo.Delaypy(2000)
                damo.MoveTopy(372, 319)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(3000)
            damo.Delaypy(1000)
            juese_time_now = datetime.datetime.now()
            time_temp = juese_time_now.minute - juese_time.minute
            if time_temp > 3:
                return 3
    except:
        prints("报错######选择角色失败")
        input()
def zhongduan_cha():
    FinStr = damo.FindStrEpy(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        prints("网络连接中断")
        intx = int(pos[1])
        inty = int(pos[2])
        damo.MoveTopy(intx + 37, inty - 29)
        damo.Delaypy(1000)
        damo.LeftDownpy()
        damo.Delaypy(1000)
        damo.MoveTopy(406, 48)
        damo.Delaypy(1000)
        damo.LeftUppy()
        damo.Delaypy(1000)
        FinStr = damo.FindStrEpy(234, 243, 562, 400, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = damo.FindStrEpy(234, 243, 562, 335, "第三方模块", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints("第三方模块，重启")
                end_exsit(2)
                damo.Delaypy(2000)
                return 1
            FinStr = damo.FindStrEpy(234, 243, 562, 335, "制裁1小时", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(seconds=3600)
                n_days = d1 + delta
                num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                prints("制裁一个小时，换号")
                end_exsit(2)
                damo.Delaypy(2000)
                return 1
            FinStr = damo.FindStrEpy(234, 243, 562, 335, "制裁一天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(days=1)
                n_days = d1 + delta
                num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                prints("制裁一天，检查飞机稳定性")
                prints("制裁一天，检查飞机稳定性")
                prints("制裁一天，检查飞机稳定性")
                prints("制裁一天，检查飞机稳定性")
                prints("制裁一天，检查飞机稳定性")
                prints("制裁一天，检查飞机稳定性")
                prints("制裁一天，检查飞机稳定性")
                end_exsit(2)
                damo.Delaypy(5000*10)
                return 1
            prints('中断制裁未识别，请把【中断截图】文件夹中的截图发给作者')
            damo.Capturepy(234, 243, 562, 335, str(time.time()) + '.bmp')
        else:
            prints("只是中断没有制裁，重上")
            end_exsit(2)
            damo.Delaypy(2000)
        return 1
    return 0
def jianceanquanmoshi(p_xgis,p_xguer,p_xgpwd):
    try:
        prints("检查安全模式")
        qingkongyouxichuangkou()
        while True:
            FinStr = damo.FindStrEpy(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 23, inty + 76)
                damo.Delaypy(2000)
                damo.LeftDoubleClickpy()
                damo.Delaypy(2000)
                damo.MoveTopy(intx + 23 + 60, inty + 76 + 55)
                damo.Delaypy(2000)
                damo.LeftDoubleClickpy()
                damo.Delaypy(2000)
            FinStr = damo.FindStrEpy(210, 511, 276, 539, "出售", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intxa = int(pos[1])
                intya = int(pos[2])
                #点击出售
                damo.MoveTopy(intxa + 10, intya + 3)
                damo.Delaypy(2000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                #点击材料
                damo.MoveTopy(590, 246)
                damo.Delaypy(2000)
                damo.LeftDoubleClickpy()
                damo.Delaypy(2000)
                #鼠标移开
                while True:
                    if zhongduan_cha() == 1:
                        break
                    # 点击出售
                    damo.MoveTopy(intxa + 10, intya + 3)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(1000)
                    damo.MoveTopy(608, 176)
                    damo.Delaypy(1000)
                    FinStr = damo.FindPicEpy(473, 258, 715, 409, "黑曜石.bmp|血滴石.bmp|金刚石.bmp|紫玛瑙.bmp|迪卡斯印章.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        damo.MoveTopy(intx + 5, inty + 5)
                        damo.Delaypy(2000)
                        damo.LeftClickpy()
                        damo.Delaypy(800)
                        damo.LeftClickpy()
                        damo.Delaypy(800)
                        damo.LeftClickpy()
                        damo.Delaypy(2000)
                    else:
                        break
                    FinStr = damo.FindStrEpy(310, 307, 427, 361, "安全模式", "ddc593-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints(account.hao + '|' + account.mi + "出现安全模式，等待解除")
                        if p_xgis == '真':
                            prints('小果解除安全模式')
                            p_qq = get_ini("config/记录.ini", "刷号记录", "当前账号")
                            xaoguo_return = xiaoguo.jiandanjieanquan(p_qq,p_xguer,p_xgpwd)
                            if xaoguo_return == True:
                                prints('小果解除安全模式 成功')
                            else:
                                prints('小果解除安全模式 失败')
                        while True:
                            # 等待解除安全模式
                            FinStr = damo.FindStrEpy(287, 250, 496, 319, "退出安全模式", "ffffff-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                intx = int(pos[1])
                                inty = int(pos[2])
                                qingkongyouxichuangkou()
                                break
                            damo.Delaypy(2000)
                            if zhongduan_cha() > 0:
                                break
                        break
                break
    except:
        prints("报错######检查安全模式失败")
def qingkongyouxichuangkou():
    try:
        while True:
            FinStr = damo.FindPicEpy(585, 117, 628, 140, "关闭系统菜单.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx+10, inty+5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                FinStr = damo.FindStrEpy(307, 242, 362, 274, "邮件箱", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    damo.MoveTopy(intx + 10, inty + 5)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(1000)
                    break
                else:
                    break
            else:
                damo.MoveTopy(1, 1)
                damo.Delaypy(500)
                damo.LeftClickpy()
                damo.Delaypy(500)
                damo.KeyPresspy(27)
                damo.Delaypy(2000)
    except:
        prints("报错######清空游戏窗口失败")
def fayoujian(CRuser, CRpwd):
    prints("发送邮件")
    kuaqu = ""
    money = get_ini('config/cfg.ini','游戏配置', '邮寄金币上限')
    qu = get_ini("config/记录.ini", "刷号记录", "当前大区")
    name = get_ini('config/仓库设置.ini',qu, "仓库名称")
    fyj_time = datetime.datetime.now()
    if name == "":
        prints("没有仓库号")
        qingkongyouxichuangkou()
        return
    try:
        prints('仓库号信息 = ' + name)
        #随机仓库
        index = name.find("|")
        if index > 0:
            namearr = name.split('|')
            intrnd = random.randint(0,len(namearr)-1)
            name = namearr[intrnd]
        #跨区仓库
        index = name.find("/")
        if index > 0:
            temp = name.split("/")
            name = temp[0]
            kuaqu = temp[1]
        while True:
            FinStr = damo.FindStrEpy(307, 242, 362, 274, "邮件箱", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty - 10)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(3000)
            else:
                damo.KeyPresspy(27)
                damo.Delaypy(3000)
            FinStr = damo.FindStrEpy(338, 138, 419, 169, "邮件保管箱", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
            damo.Delaypy(500)
        #检查金币
        number = damo.Ocrpy(610, 529, 700, 549,"e6c89b-000000",1)
        if int(number) < int(money):
            prints("游戏币不够设置的金额")
            qingkongyouxichuangkou()
            return
        while True:
            FinStr = damo.FindStrEpy(278, 139, 341, 171, "发送邮件", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx+10, inty+3)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(500)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
            FinStr = damo.FindStrEpy(202, 169, 246, 191, "收件人", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 104, inty + 5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(3000)
                hwnd = damo.FindWindowpy("地下城与勇士", "地下城与勇士")
                if hwnd > 0:
                    damo.SendStringpy(hwnd, name)
                damo.Delaypy(3000)
                damo.MoveTopy(intx + 203, inty + 5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
            damo.Delaypy(500)
        while True:
            FinStr = damo.FindStrEpy(315, 261, 451, 294, "选择接收区", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                if kuaqu == "":
                    damo.MoveTopy(intx + 72, inty + 60)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(2000)
                    #大区确认
                    damo.MoveTopy(400, 340)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(2000)
                    break
                else:
                    #点击下拉列表
                    damo.MoveTopy(462, 299)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(3000)
                    while True:
                        FinStr = damo.FindStrEpy(323, 307, 369, 475, kuaqu, "ddc593-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            intx = int(pos[1])
                            inty = int(pos[2])
                            #选择跨区
                            damo.MoveTopy(intx + 5, inty + 3)
                            damo.Delaypy(1000)
                            damo.LeftClickpy()
                            damo.Delaypy(3000)
                            #确认
                            damo.MoveTopy(397, 326)
                            damo.Delaypy(1000)
                            damo.LeftClickpy()
                            damo.Delaypy(3000)
                            # 大区确认
                            damo.MoveTopy(400, 340)
                            damo.Delaypy(1000)
                            damo.LeftClickpy()
                            damo.Delaypy(5000)
                            break
                        else:
                            damo.MoveTopy(467, 460)
                            damo.Delaypy(1000)
                            damo.LeftClickpy()
                            damo.Delaypy(2000)
                        fyj_time_now = datetime.datetime.now()
                        time_temp = fyj_time_now.minute - fyj_time.minute
                        if time_temp > 3:
                            prints("发邮件超时，取消")
                            qingkongyouxichuangkou()
                            return
                        damo.Delaypy(500)
                    break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
            damo.Delaypy(500)
                    #添加发送物品
        #添加附件
        damo.MoveTopy(317, 378)
        damo.Delaypy(1000)
        damo.LeftClickpy()
        damo.Delaypy(3000)
        #选择材料
        damo.MoveTopy(590, 246)
        damo.Delaypy(1000)
        damo.LeftDoubleClickpy()
        damo.Delaypy(3000)
        tianjiashuliang = 0
        while True:
            FinStr = damo.FindPicEpy(472, 256, 767, 436, "无色小晶体.bmp|魔刹石.bmp|挑战书.bmp|无尽的永恒.bmp|数据芯片.bmp|迷幻晶石.bmp|强烈之痕迹.bmp|矛盾的结晶体.bmp|浓缩的异界精髓.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 3, inty + 5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                if int(pos[0]) == 0:
                    damo.KeyPresspy(13)
                    damo.Delaypy(1000)
                else:
                    damo.LeftClickpy()
                    damo.Delaypy(1000)
                tianjiashuliang = tianjiashuliang + 1
            else:
                break
            if tianjiashuliang >= 10:
                break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
        #选择副职业
        damo.MoveTopy(638, 246)
        damo.Delaypy(1000)
        damo.LeftClickpy()
        damo.Delaypy(3000)
        while True:
            FinStr = damo.FindPicEpy(472, 260, 716, 413, "紫色卡片.bmp|粉色卡片.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty + 10)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(3000)
                tianjiashuliang = tianjiashuliang + 1
            else:
                break
            if tianjiashuliang >= 10:
                break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
        #输入金币
        damo.MoveTopy(333, 412)
        damo.Delaypy(1000)
        damo.LeftClickpy()
        damo.Delaypy(3000)
        damo.KeyPressStrpy(str(int(number)-300000),200)
        damo.Delaypy(1000)
        #发送
        damo.MoveTopy(261, 461)
        damo.Delaypy(1000)
        damo.LeftClickpy()
        damo.Delaypy(1000)
        damo.MoveTopy(261 - 60, 461)
        damo.LeftClickpy()
        damo.Delaypy(3000)
        while True:
            FinStr = damo.FindPicEpy(232, 69, 693, 499, "发邮件验证码.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                damo.Delaypy(1000)
                intx = int(pos[1])
                inty = int(pos[2])
                #打码
                damo.CaptureJpgpy(intx - 207, inty - 22, intx - 78, inty + 30, os.getcwd() + "/ver.jpg", 20)
                damo.Delaypy(500)
                dc = rk.RClient(CRuser, CRpwd, "92131", "4e1ce1108f244c6381d5bcfdbe368ae4")
                im = open(os.getcwd() + '/ver.jpg', 'rb').read()
                yzm = dc.rk_create(im, "3040")
                xy = yzm["Result"]
                damo.MoveTopy(intx + 35, inty + 5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                for n in range(6):
                    damo.KeyPresspy(8)
                    damo.Delaypy(500)
                damo.Delaypy(1000)
                damo.KeyPressStrpy(xy, 500)
                damo.Delaypy(1000)
                damo.MoveTopy(intx -123, inty + 131)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(5000)
                FinStr = damo.FindStrEpy(346, 278, 449, 309, "已成功发送邮件", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    qingkongyouxichuangkou()
                    break
                else:
                    damo.MoveTopy(410, 176)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(2000)
                    damo.MoveTopy(400, 339)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(2000)
                    damo.MoveTopy(262, 462)
                    damo.Delaypy(1000)
                    damo.LeftClickpy()
                    damo.Delaypy(4000)
            damo.Delaypy(1000)
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
        return 1
    except:
        prints("报错######发送邮件失败")
def login(CRuser,CRpwd,path,WeGame,money_is):
    prints("登录账号")
    account_path = path
    shubiaodianji = False
    x = damo.GetScreenWidthpy()
    y = damo.GetScreenHeightpy()
    login_time = datetime.datetime.now()
    while True:
        if money_is == '真':
            hao, mi, qu, jue = get_account_zhuanqian(account_path)
        else:
            hao, mi, qu, jue = get_account(account_path)
        if hao == "":
            prints('没有没有可刷账号，等待6点更新')
            damo.Delaypy(10000)
            return 101
        else:
            break
        login_time_now = datetime.datetime.now()
        time_temp = login_time_now.minute - login_time.minute
        if time_temp > 6:
            return 3
    damo.RunApppy(WeGame,0)
    # 恢复打印机窗口
    try:
        while True:
            FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_登录.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                #刷新列表
                shuaxinliebiao()
                damo.MoveTopy(intx + 70, inty - 136)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(500)
                for i in range(13):
                    damo.KeyPresspy(8)
                    damo.Delaypy(200)
                damo.Delaypy(500)
                #输入账号
                damo.KeyPressStrpy(hao,100)
                damo.Delaypy(500)
                damo.MoveTopy(intx + 70, inty - 106)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(500)
                #输入密码
                damo.KeyPressStrpy(mi, 100)
                damo.Delaypy(500)
                #点击登录
                damo.MoveTopy(intx, inty)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(2000)
            FinStr = damo.FindStrEpy(0, 0, x, y, "拖动滑块", "000000-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.Delaypy(2000)
                damo.CaptureJpgpy(intx + 1,inty + 22, intx + 280, inty + 179,os.getcwd() + "/ver.jpg", 20)
                damo.Delaypy(500)
                dc = rk.RClient(CRuser, CRpwd, "92131", "4e1ce1108f244c6381d5bcfdbe368ae4")
                im = open(os.getcwd() + '/ver.jpg', 'rb').read()
                yzm = dc.rk_create(im, "6137")
                xy = yzm["Result"]
                px = intx + 43
                py = inty + 199
                damo.MoveTopy(px, py)
                damo.Delaypy(500)
                damo.LeftDownpy()
                damo.Delaypy(500)
                for i in range(int(xy.split(',')[0]) - 38):
                    damo.MoveTopy(px + i, py - i)
                    damo.Delaypy(5)
                damo.LeftUppy()
                damo.Delaypy(5000)
                #确认后延迟大点
            FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_跳过.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            FinStr = damo.FindStrEpy(0, 0, x, y, "今日推荐", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 403, inty + 8)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_主页.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty + 10)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_开始游戏.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intxa = int(pos[1])
                intya = int(pos[2])
                FinStr = damo.FindStrEpy(intxa - 321 , intya - 16, intxa - 199, intya + 30, qu, "3c3c3c-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    damo.MoveTopy(intxa + 20, intya + 10)
                    damo.Delaypy(200)
                    damo.LeftClickpy()
                    damo.Delaypy(2000)
                    shubiaodianji = True
                else:
                    damo.MoveTopy(intxa - 116, intya + 10)
                    damo.Delaypy(200)
                    damo.LeftClickpy()
                    damo.Delaypy(2000)
                    FinStr = damo.FindStrEpy(intxa - 326, intya - 186, intxa - 251, intya - 21, qu, "3c3c3c-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        damo.MoveTopy(intx +10, inty + 3)
                        damo.Delaypy(200)
                        damo.LeftClickpy()
                        damo.Delaypy(2000)
            else:
                FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_列表_dnf.bmp|tgp_列表_dnf1.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    damo.MoveTopy(intx, inty)
                    damo.Delaypy(200)
                    damo.LeftClickpy()
                    damo.Delaypy(1000)
            FinStr = damo.FindStrEpy(0, 0, x, y, "跳过检测", "2098ff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty + 3)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            FinStr = damo.FindStrEpy(0, 0, x, y, "优化跳过", "3c3c3c-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx, inty)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_登录失败.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 0
            FinStr = damo.FindStrEpy(0, 0, x, y, "连接频道失败", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 0
            FinStr = damo.FindStrEpy(1, 1, x, y, "结束游戏", "ddc593-000000|ffffb8-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                set_ini('config/功能键设置.ini', '飞机功能键', '赛丽亚房间按键开关', "True")
                set_ini('config/功能键设置.ini', '飞机功能键', '图内按键开关', "True")
                return 1
            if shubiaodianji:
                damo.MoveTopy(1, 1)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            login_time_now = datetime.datetime.now()
            time_temp = login_time_now.minute - login_time.minute
            if time_temp > 6:
                return 3
    except:
        prints("报错######登录账号失败")
        input()
def fenghaojianhcha():
    FinStr = damo.FindStrEpy(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        prints("网络连接中断")
        intx = int(pos[1])
        inty = int(pos[2])
        damo.MoveTopy(intx + 37, inty - 29)
        damo.Delaypy(1000)
        damo.LeftDownpy()
        damo.Delaypy(1000)
        damo.MoveTopy(406, 48)
        damo.Delaypy(1000)
        damo.LeftUppy()
        damo.Delaypy(2000)
        FinStr = damo.FindStrEpy(234, 243, 562, 400, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = damo.FindStrEpy(238, 243, 562, 335, "停封5天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                number = damo.Ocrpy(414, 291, 526, 307, "ffffff-000000", 1)
                if number != "":
                    number = number.replace('/','-',2)
                    number = number.replace('/',' ',1)
                    prints(number)
                    try:
                        d1 = datetime.datetime.strptime(number,'%Y-%m-%d %H:%M')
                        #获取的时间上+100秒只是为了获取到一个完整格式
                        #也可以用days加天数
                        delta = datetime.timedelta(seconds=100)
                        n_days = d1 + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                    except:
                        n_days = datetime.datetime.now()
                        delta = datetime.timedelta(days=1)
                        n_days = n_days + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                return 'F5'
            FinStr = damo.FindStrEpy(238, 243, 562, 335, "停封7天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                number = damo.Ocrpy(414, 291, 526, 307, "ffffff-000000", 1)
                if number != "":
                    number = number.replace('/','-',2)
                    number = number.replace('/',' ',1)
                    prints(number)
                    try:
                        d1 = datetime.datetime.strptime(number,'%Y-%m-%d %H:%M')
                        #获取的时间上+100秒只是为了获取到一个完整格式
                        #也可以用days加天数
                        delta = datetime.timedelta(seconds=100)
                        n_days = d1 + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                    except:
                        n_days = datetime.datetime.now()
                        delta = datetime.timedelta(days=1)
                        n_days = n_days + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                return 'F7'
            FinStr = damo.FindStrEpy(234, 243, 562, 335, "永久封号", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(days=365)
                n_days = d1 + delta
                num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                return 'F100'
            prints('封号类型未识别，请把【中断截图】文件夹中的截图发给作者')
            damo.Capturepy(234, 243, 562, 335, str(time.time()) + '.bmp')
        else:
            return 'F0'
    FinStr = damo.FindStrEpy(234, 243, 562, 335, "此ID已在游戏", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 'F101'
    return ''
def yongbingchuzhan():
    prints('佣兵出战')
    while True:
        FinStr = damo.FindStrEpy(390, 85, 440, 120, "佣兵", "ffffb8-000000|ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            damo.MoveTopy(intx + 10, inty + 5)
            damo.Delaypy(1000)
            damo.LeftClickpy()
            damo.Delaypy(1000)
            FinStr = damo.FindPicEpy(510, 325, 604, 363, "佣兵_领取奖励.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty + 5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                #选择领取奖励的佣兵
                damo.MoveTopy(365, 197)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                #确认
                damo.MoveTopy(363, 319)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                qingkongyouxichuangkou()
            FinStr = damo.FindPicEpy(513, 323, 599, 363, "佣兵_佣兵出战.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty + 5)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                #确认
                damo.MoveTopy(361, 326)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(2000)
                qingkongyouxichuangkou()
                break
            FinStr = damo.FindPicEpy(503, 323, 614, 369, "佣兵_取消出战.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                qingkongyouxichuangkou()
                break
            FinStr = damo.FindPicEpy(513, 323, 599, 363, "佣兵_佣兵出战_灰.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                qingkongyouxichuangkou()
                break
        else:
            damo.MoveTopy(781,521)
            damo.Delaypy(1000)
            damo.LeftClickpy()
            damo.Delaypy(2000)
        if zhongduan_cha() == 1:
            break
        damo.Delaypy(1000)
def qingchushuatujilu():
    config = configparser.ConfigParser()
    config.read("config/记录.ini")
    ret = config.options('完成时间')
    for i in ret:
        print(i)
        config.remove_option("完成时间", i)
    ret = config.options('完成')
    for i in ret:
        print(i)
        config.remove_option("完成", i)
    config.write(open("config/记录.ini", "w"))
def liudiangengxin():
    try:
        temp = get_ini("config/记录.ini", "更新", '六点更新')
        d2 = datetime.datetime.now()
        if temp != "":
            d1 = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S')
            days = d2.day-d1.day
            if days > 1:
                qingchushuatujilu()
                shuaxinliebiao()
                prints('六点更新成功')
                set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
            elif days == 1:
                    if d2.hour >= 6:
                        qingchushuatujilu()
                        shuaxinliebiao()
                        prints('六点更新成功')
                        set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
            elif days == 0:
                if d1.hour < 6:
                    if d2.hour >= 6:
                        qingchushuatujilu()
                        shuaxinliebiao()
                        prints('六点更新成功')
                        set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            d1 = datetime.datetime.now()
            set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
    except:
        prints('六点更新失败')
def saotubiao():
    damo.MoveTopy(689, 945)
    damo.MoveTopy(1266, 945)
def chushoudianquan():
    prints('兑换点券')
    int_quan = 0
    while True:
        FinStr = damo.FindStrEpy(601, 414, 775, 540, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            number = damo.Ocrpy(intx - 178, inty + 45, intx - 124, inty + 69, "e6c89b-000000", 1)
            number = re.sub("\D", "", number)
            prints('点券 = ' + number)
            if int(number) >= 200:
                if int(number) >= 4500:
                    int_quan = 1
                break
            else:
                return 0
        else:
            damo.KeyPresspy(73)
            damo.Delaypy(2000)
    qingkongyouxichuangkou()
    if int_quan == 0:
        wenzi = '一百万'
    elif int_quan == 1:
        wenzi = '一千万'
    else:
        wenzi = '一百万'
    while True:
        if wenzi == '':
            return 1
        FinStr = damo.FindStrEpy(41, 534,114, 566, "寄售金币", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = damo.FindPicEpy(160, 545, 191, 573, "商城.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                damo.MoveTopy(761, 24)
                damo.Delaypy(500)
                damo.LeftClickpy()
                damo.Delaypy(2000)
            FinStr = damo.FindStrEpy(34, 148, 89, 418, wenzi, "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty + 3)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                #搜索
                damo.MoveTopy(516, 89)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                for i in range(10):
                    FinStr = damo.FindStrEpy(484, 122, 540, 309, '购买', "ffb400-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        #购买
                        damo.MoveTopy(570, 290)
                        damo.Delaypy(500)
                        damo.LeftClickpy()
                        damo.Delaypy(500)
                        damo.MoveTopy(570+55, 290+12)
                        damo.Delaypy(500)
                        damo.LeftClickpy()
                        damo.Delaypy(500)
                        damo.MoveTopy(570+55+57, 290+12+23)
                        damo.Delaypy(500)
                        damo.LeftClickpy()
                        damo.Delaypy(6000)
                        FinStr = damo.FindStrEpy(293, 235, 503, 356, '拍卖行不存在', "ffffff-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            damo.MoveTopy(400, 319)
                            damo.Delaypy(500)
                            damo.LeftClickpy()
                            damo.Delaypy(500)
                            while True:
                                FinStr = damo.FindPicEpy(160, 545, 191, 573, "商城.bmp", "000000", "0.9", 0)
                                pos = FinStr.split('|')
                                if int(pos[1]) > 0:
                                    damo.MoveTopy(400, 557)
                                    damo.Delaypy(500)
                                    damo.LeftClickpy()
                                    damo.Delaypy(500)
                                    damo.LeftClickpy()
                                    damo.Delaypy(2000)
                                    damo.MoveTopy(761, 24)
                                    damo.Delaypy(500)
                                    damo.LeftClickpy()
                                    damo.Delaypy(2000)
                                    break
                                else:
                                    damo.MoveTopy(483, 580)
                                    damo.Delaypy(500)
                                    damo.LeftClickpy()
                                    damo.Delaypy(3000)
                            break
                        FinStr = damo.FindStrEpy(293, 235, 503, 356, '完成竞拍', "ffffff-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            damo.MoveTopy(400, 319)
                            damo.Delaypy(500)
                            damo.LeftClickpy()
                            damo.Delaypy(500)
                            break
                    #红色购买
                    FinStr = damo.FindStrEpy(484, 122, 540, 309, '购买', "ff3232-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        if wenzi == '一千万':
                            wenzi = '一百万'
                        elif wenzi == '一百万':
                            wenzi = ""
                        break
                    damo.Delaypy(500)
            else:
                damo.MoveTopy(37, 136)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
        else:
            damo.MoveTopy(386, 576)
            damo.Delaypy(1000)
            damo.LeftClickpy()
            damo.Delaypy(1000)
            damo.MoveTopy(367, 538)
            damo.Delaypy(1000)
            damo.LeftClickpy()
            damo.Delaypy(1000)
def jieshouyoujian():
        FinStr = damo.FindPicEpy(263, 462, 533, 551, "邮件.bmp|邮件1.bmp", "202020", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            damo.MoveTopy(intx + 5, inty + 3)
            damo.Delaypy(1000)
            damo.LeftClickpy()
            damo.Delaypy(3000)
            FinStr = damo.FindStrEpy(338, 138, 419, 169, "邮件保管箱", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                damo.Delaypy(1000)
                damo.MoveTopy(298, 465)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(3000)
                for i in range(10):
                    FinStr = damo.FindStrEpy(338, 138, 419, 169, "邮件领取完毕", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        break
                    damo.Delaypy(1000)
def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            return fp
def yanjiuweipeizhi(fubenID):
    name = search('C:\\Users\Administrator\Desktop','.ini')
    set_ini_n(name,'出售分解','1')
    set_ini_n(name, '是否全图', '1')
    set_ini_n(name, '副本ID', fubenID)
def shengoupeizhi(fubenID,jinengID):
    set_ini_n('C:\神狗.ini','技能代码',jinengID)
    set_ini_n('C:\神狗.ini', '指定地图', fubenID)
def ZiHgpeizhi(fubenID):
    set_ini_n('C:\\Users\Administrator\Desktop\ZiHg.ini', '地图ID', fubenID)
    set_ini_n('C:\\Users\Administrator\Desktop\ZiHg.ini', '角色数量', '1')
    set_ini_n('C:\\Users\Administrator\Desktop\ZiHg.ini', '预留PL', '0')
def jinqizhicai():
    FinStr = damo.FindStrEpy(812, 26, 1114, 114, "近期出现异常|制裁", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        num = get_ini("config/记录.ini", "刷号记录", "当前账号")
        a = damo.Ocrpy(812, 26, 1114, 114, "e6c89b-000000", 1)
        if a.find('小时') > -1:
            arr = a.split('小时')
            temp_h = re.sub("\D", "", arr[0])
            d1 = datetime.datetime.now()
            # 制裁的小时+1
            # 转换成秒加到当前时间
            prints('制裁' + str(int(temp_h) + 1) + '小时')
            z_time = (int(temp_h) + 1) * 60 * 60
            delta = datetime.timedelta(seconds=z_time)
            n_days = d1 + delta
            set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
            prints("出现制裁,已记录制裁时间，换号")
            end_exsit(2)
            damo.Delaypy(2000)
        else:
            d1 = datetime.datetime.now()
            # 也可以用days加天数,seconds加秒
            # 制裁时间无法识别，先加一小时
            delta = datetime.timedelta(seconds=3600)
            n_days = d1 + delta
            set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
            prints("出现制裁等待一小时，换号")
            prints('近期制裁，请把文件夹中的截图发给作者')
            damo.Capturepy(812, 26, 1114, 114, os.getcwd() + '/' + str(time.time()) + '.bmp')
            end_exsit(2)
            damo.Delaypy(2000)
        return 1
    return 0
def while_():
    # 读取配置文档
    WeGame = get_ini('config/cfg.ini','主配置', 'WeGame')
    number = get_ini('config/cfg.ini','主配置', '账号路径')
    CRuser = get_ini('config/cfg.ini','主配置', '若快账号')
    CRpwd = get_ini('config/cfg.ini','主配置', '若快密码')
    zhuanqian =get_ini('config/cfg.ini','主配置', '只转钱')
    xgis = get_ini('config/cfg.ini','小果配置', '小果解安全')
    xguer = get_ini('config/cfg.ini','小果配置', '小果账号')
    xgpwd = get_ini('config/cfg.ini','小果配置', '小果密码')
    x = damo.GetScreenWidthpy()
    y = damo.GetScreenHeightpy()
    time_60 = False
    while True:
        liudiangengxin()
        saotubiao()
        shuaxinliebiao()
        # 游戏内执行一次
        if check_exsit("DNF.exe") == 0:
            #结束全部进程
            end_exsit(2)
            #登录成功返回窗口句柄
            login_ret = login(CRuser,CRpwd,number,WeGame,zhuanqian)
            if login_ret == 0:
                prints("连接频道失败，重上")
                end_exsit(2)
                damo.Delaypy(2000)
                continue
            elif login_ret == 3:
                prints("登录超时，重上")
                end_exsit(2)
                damo.Delaypy(2000)
                continue
            elif login_ret == 101:
                continue
            time_60 = True
            damo.Delaypy(3000)
        hwnd = damo.FindWindowpy("地下城与勇士", "地下城与勇士")
        if hwnd > 0:
            damo.MoveWindowpy(hwnd, 0, 0)
            damo.Delaypy(5000)
            hwnda = damo.FindWindowpy("", "疯子打印机")
            if hwnda > 0:
                damo.SetWindowStatepy(hwnda, 12)
            FinStr = damo.FindStrEpy(0, 0, x, y, "结束游戏", "ddc593-050505|ffffb8-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                damo.Delaypy(5000)
                fenghao_return = fenghaojianhcha()
                if fenghao_return == 'F5':
                    prints("账号停封5天，换号")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                elif fenghao_return == 'F7':
                    prints("账号停封7天，换号")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                elif fenghao_return == 'F0':
                    prints('只是中断没有封号，重上')
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                elif fenghao_return == 'F100':
                    prints("永久封号，换号")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                elif fenghao_return == 'F101':
                    prints("此ID已在游戏中，重上")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                juesechuli_ret = juesechuli(1)
                if juesechuli_ret == 0:
                    prints("角色刷完，换号")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                elif juesechuli_ret == 1:
                    prints("角色更换完成")
                elif juesechuli_ret == 2:
                    prints("网络连接中断，重上")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                elif juesechuli_ret == 3:
                    prints("角色处理超时，重上")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    continue
                damo.Delaypy(5000)
                #刷新列表
                shuaxinliebiao()
            FinStr = damo.FindStrEpy(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if jinqizhicai() == 1:
                    continue
                damo.Delaypy(3000)
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 5, inty + 3)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                qingkongyouxichuangkou()
            FinStr = damo.FindPicEpy(365, 356, 418, 384, "签到.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if jinqizhicai() == 1:
                    continue
                damo.Delaypy(1000)
                qingkongyouxichuangkou()
            FinStr = damo.FindPicEpy(768, 1, 800, 31, "图外.bmp|图外1.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if jinqizhicai() == 1:
                    continue
                damo.Delaypy(1000)
                damo.MoveTopy(1, 1)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                qingkongyouxichuangkou()
            time_is = False
            #游戏内循环执行
            while True:
                if zhongduan_cha() == 1:
                    break
                FinStr = damo.FindStrEpy(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    FinStr = damo.FindStrEpy(812, 26, 1114, 114, "近期出现异常|制裁", "e6c89b-000000|ff3232-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        d1 = datetime.datetime.now()
                        # 也可以用days加天数,seconds加秒
                        # 制裁时间无法识别，先加一天
                        delta = datetime.timedelta(days=1)
                        n_days = d1 + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号")
                        set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                        prints("出现制裁等待一天，换号")
                        prints('近期制裁，请把【中断截图】文件夹中的截图发给作者')
                        damo.Capturepy(812, 26, 1114, 114, str(time.time()) + '.bmp')
                        end_exsit(2)
                        damo.Delaypy(2000)
                        break
                    temp = get_ini('config/功能键设置.ini', '飞机功能键', '赛丽亚房间按键开关')
                    if temp == "True":
                        if time_60 == True:
                            prints("等待60秒...")
                            damo.Delaypy(4000*10)
                            # 检测安全模式
                            qingkongyouxichuangkou()
                            jianceanquanmoshi(xgis,xguer,xgpwd)
                            qingkongyouxichuangkou()
                            csdq_ret = chushoudianquan()
                            qingkongyouxichuangkou()
                            if csdq_ret > 0:
                                jieshouyoujian()
                                qingkongyouxichuangkou()
                            #只兑换点券
                            if zhuanqian == '真':
                                fyj_return = fayoujian(CRuser, CRpwd)
                                if fyj_return == 1:
                                    #正常返回
                                    pass
                                elif fyj_return == 2:
                                    prints('网络连接中断,重上')
                                    end_exsit(2)
                                    damo.Delaypy(2000)
                                    break
                                elif fyj_return == 3:
                                    prints('发送邮件超时,重上')
                                    end_exsit(2)
                                    damo.Delaypy(2000)
                                    break
                                prints("转账完成，换号")
                                jiluwanchengshijian_zhuanqian()
                                end_exsit(2)
                                damo.Delaypy(2000)
                                break
                            yongbingchuzhan()
                            qingkongyouxichuangkou()
                        time_60 = False
                        # #设置飞机配置
                        # dt_temp = get_ini('config/记录.ini', '地图', "地图ID")
                        # if dt_temp != '':
                        #     ZiHgpeizhi(dt_temp)
                        # else:
                        #     ZiHgpeizhi('104')
                        #飞机功能键
                        # 疲劳刷完了
                        color = damo.GetColorpy(339, 553)
                        if color == "0b0b0b" or color == "333333":
                            prints('PL刷完，不启动飞机')
                        else:
                            # key_str = get_ini('config/功能键设置.ini', '飞机功能键', '赛丽亚房间按键')
                            # if key_str != "":
                            #     if key_str.find('|') > -1:
                            #         key_str_arr = key_str.split('|')
                            #         for key in key_str_arr:
                            #             damo.KeyDownCharpy(key)
                            #             damo.Delaypy(200)
                            #             damo.KeyUpCharpy(key)
                            #             damo.Delaypy(1000)
                            #     else:
                            #         damo.KeyDownCharpy(key_str)
                            #         damo.Delaypy(200)
                            #         damo.KeyUpCharpy(key_str)
                            #         damo.Delaypy(1000)
                            #启动飞机
                            damo.KeyDownpy(16)
                            damo.Delaypy(200)
                            damo.KeyPresspy(112)
                            damo.Delaypy(200)
                            damo.KeyUppy(16)
                            set_ini('config/功能键设置.ini', '飞机功能键', '赛丽亚房间按键开关', "False")
                            time_is = True
                            while_time = datetime.datetime.now()
                temp = get_ini('config/功能键设置.ini', '飞机功能键', '图内按键开关')
                if temp == "True":
                    #还没有进入图内 判断高延迟可能出现的 关闭 和 签到
                    FinStr = damo.FindPicEpy(365, 356, 418, 384, "签到.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        if jinqizhicai() == 1:
                            break
                        damo.Delaypy(1000)
                        qingkongyouxichuangkou()
                    FinStr = damo.FindPicEpy(242, 430, 316, 490, "金麦克.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        damo.MoveTopy(intx + 10, inty - 10)
                        damo.Delaypy(1000)
                        damo.LeftClickpy()
                        damo.Delaypy(2000)
                        damo.KeyPresspy(27)
                        damo.Delaypy(500)
                        damo.KeyPresspy(27)
                        damo.Delaypy(500)
                        damo.KeyPresspy(27)
                        damo.Delaypy(500)
                        damo.MoveTopy(372, 319)
                        damo.Delaypy(200)
                        damo.LeftClickpy()
                        damo.Delaypy(3000)
                    FinStr = damo.FindPicEpy(768, 1, 800, 31, "图内.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints("刷图中......")
                        damo.Delaypy(3000)
                        key_str = get_ini('config/功能键设置.ini', '飞机功能键', '图内按键')
                        if key_str != "":
                            damo.Delaypy(1000)
                            if key_str.find('|') > -1:
                                key_str_arr = key_str.split('|')
                                for key in key_str_arr:
                                    damo.KeyDownCharpy(key)
                                    damo.Delaypy(200)
                                    damo.KeyUpCharpy(key)
                                    damo.Delaypy(1000)
                            else:
                                damo.KeyDownCharpy(key_str)
                                damo.Delaypy(200)
                                damo.KeyUpCharpy(key_str)
                                damo.Delaypy(1000)
                            set_ini('config/功能键设置.ini', '飞机功能键', '图内按键开关', "False")
                            damo.Delaypy(5000)
                        else:
                            set_ini('config/功能键设置.ini', '飞机功能键', '图内按键开关', "False")
                #疲劳刷完了
                color = damo.GetColorpy(339,553)
                if color == "0b0b0b" or color == "333333":
                    FinStr = damo.FindPicEpy(768, 1, 800, 31, "图外.bmp|图外1.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        damo.MoveTopy(1, 1)
                        damo.Delaypy(1000)
                        damo.LeftClickpy()
                        damo.Delaypy(1000)
                        damo.KeyPresspy(27)
                        damo.Delaypy(3000)

                    FinStr = damo.FindStrEpy(360, 459, 413, 477, "选择角色", "e6c89b-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints("PL刷完，换角色")
                        #发送邮件
                        fyj_return = fayoujian(CRuser, CRpwd)
                        if fyj_return == 1:
                            # 正常返回
                            pass
                        elif fyj_return == 2:
                            prints('网络连接中断,重上')
                            end_exsit(2)
                            damo.Delaypy(2000)
                            break
                        elif fyj_return == 3:
                            prints('发送邮件超时,重上')
                            end_exsit(2)
                            damo.Delaypy(2000)
                            break
                        jieshouyoujian()
                        # 记录完成时间
                        jiluwanchengshijian()
                        #换角色
                        juesechuli_ret = juesechuli(2)
                        if juesechuli_ret == 0:
                            prints("角色刷完，换号")
                            end_exsit(2)
                            damo.Delaypy(2000)
                            break
                        if juesechuli_ret == 1:
                            #正常返回
                            pass
                        elif juesechuli_ret == 2:
                            prints("网络连接中断，重上")
                            end_exsit(2)
                            damo.Delaypy(2000)
                            break
                        elif juesechuli_ret == 3:
                            prints("角色处理超时，重上")
                            end_exsit(2)
                            damo.Delaypy(2000)
                            break
                        tk.trickit()
                        damo.Delaypy(5000)
                        prints("准备刷图")
                        qingkongyouxichuangkou()
                        while_time = datetime.datetime.now()
                        set_ini('config/功能键设置.ini', '飞机功能键', '赛丽亚房间按键开关','True')

                #借用计时开关
                if time_is == True:
                    #到角色界面关闭飞机
                    #二嫂飞机功能
                    FinStr = damo.FindStrEpy(0, 0, x, y, "结束游戏", "ddc593-050505|ffffb8-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        damo.Delaypy(5000)
                        FinStr = damo.FindStrEpy(0, 0, x, y, "结束游戏", "ddc593-050505|ffffb8-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            prints('再次上角色，发邮件')
                            damo.KeyDownpy(16)
                            damo.Delaypy(200)
                            damo.KeyPresspy(112)
                            damo.Delaypy(200)
                            damo.KeyUppy(16)
                            juesechuli(1)
                            qingkongyouxichuangkou()
                            time_is = False


                FinStr = damo.FindPicEpy(0, 0, x, y, "tgp_列表_dnf.bmp|tgp_列表_dnf1.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    prints("游戏窗口消失")
                    end_exsit(2)
                    damo.Delaypy(2000)
                    break
                FinStr = damo.FindStrEpy(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    FinStr = damo.FindStrEpy(812, 26, 1114, 114, "近期出现异常|制裁", "e6c89b-000000|ff3232-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        if jinqizhicai() == 1:
                            break
                        break
                    damo.Delaypy(1000)
                    qingkongyouxichuangkou()
                FinStr = damo.FindStrEpy(333, 571, 473, 597, "只能城镇交易", "ffff00-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    time_is = True
                    while_time = datetime.datetime.now()

                if time_is == True:
                    while_time_now = datetime.datetime.now()
                    time_temp =  while_time_now.minute - while_time.minute
                    if time_temp > 3:
                        prints("图内超时，重上")
                        end_exsit(2)
                        damo.Delaypy(2000)
                        break
                FinStr = damo.FindStrEpy(310, 307, 427, 361, "安全模式", "ddc593-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    prints(account.hao + '|' + account.mi + "出现安全模式，等待解除")
                    if xgis == '真':
                        prints('小果解除安全模式')
                        p_qq = get_ini("config/记录.ini", "刷号记录", "当前账号")
                        xaoguo_return = xiaoguo.jiandanjieanquan(p_qq, xguer, xgpwd)
                        if xaoguo_return == True:
                            prints('小果解除安全模式 成功')
                        else:
                            prints('小果解除安全模式 失败')
                    else:
                        prints(account.hao + '|' + account.mi + "出现安全模式，等待解除")
                        damo.Delaypy(5000)
                damo.Delaypy(1000)
        damo.Delaypy(1000)

while_()
