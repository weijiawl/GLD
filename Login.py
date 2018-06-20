#!/usr/bin/python
#-*- coding: UTF-8 -*-
import win32com.client
from win32con import HKEY_CURRENT_USER,KEY_SET_VALUE,REG_SZ
from win32api import RegSetValueEx,RegOpenKeyEx,RegCloseKey
import rk
import configparser
import datetime
import re
import time
import xg
import random
import test
from socket import *
import multiprocessing
#import tk
#import threading
from subprocess import *
import os
import ctypes
from PIL import ImageGrab

#界面
# tk_wins = threading.Thread(target=tk.win)
# tk_wins.start()
dll = ctypes.windll.LoadLibrary(os.getcwd() + '/testgame.dll')
dll.NFfyuHGvNTS(os.getcwd() + '/wiwl.dll',1)
dw = win32com.client.Dispatch('tv.cc')
dw.KBKDIaFTjE(os.getcwd() + "/Image")
dw.ZcmXmGrwol(0, os.getcwd() + "/soft.txt")
dw_ret = dw.VbXjmz("weijiawl95794bdf61a133a0415974c0c2c93e76", "python")
print(dw.LbaZsEtnLBcKSai())
dw.lrClHaBwmzW(0)
print(dw.aVZsYLBIa(1,"f1"))
time.sleep(1)
#print(dw.aVZsYLBIa(1,"b2"))
xiaoguo = xg.xgdx()
x = dw.yTKUBaTqevaYZRU()
y = dw.vgtwHdrCtErzwk()
xamo = test.HZ(x, y)
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
# 定义参数
jn_key = {'弗利特': 81, '桑德尔': 87, '牛头王': 69, '路易斯': 82, '伊伽贝拉': 84, '召唤兽狂化': 89, '鞭子': 65, '赫德尔': 83,'冰': 68, '火': 70, '光': 71, '暗': 72}
jn_time = {'伊伽贝拉': 200, '冰': 200, '火': 200, '光': 200, '暗': 200}
jn_now_time = {'弗利特': '2018-03-30 21:44:09', '桑德尔': '2018-03-30 21:44:09', '牛头王': '2018-03-30 21:44:09','路易斯': '2018-03-30 21:44:09', '伊伽贝拉': '2018-03-30 21:44:09', '召唤兽狂化': '2018-03-30 21:44:09','鞭子': '2018-03-30 21:44:09', '赫德尔': '2018-03-30 21:44:09', '冰': '2018-03-30 21:44:09','火': '2018-03-30 21:44:09', '光': '2018-03-30 21:44:09', '暗': '2018-03-30 21:44:09'}
jn_sf_time = {'弗利特': 0.8, '桑德尔': 0.9, '牛头王': 1.3, '路易斯': 1.1, '伊伽贝拉': 1.1, '召唤兽狂化': 0.8, '鞭子': 0.3,'赫德尔': 0.8, '冰': 0.8, '火': 0.8, '光': 0.8, '暗': 0.8}
def addfile2autorun(path):
    prints('写入开机自启')
    #"注册到启动项"
    runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
    hKey = RegOpenKeyEx(HKEY_CURRENT_USER, runpath, 0, KEY_SET_VALUE)
    (filepath, filename) = os.path.split(path)
    RegSetValueEx(hKey, "WindowsInit", 0, REG_SZ, path)
    RegCloseKey(hKey)
def 向左():
    if xamo.CJdsfDH(38) == 1:
        xamo.LJDFnmeFSD(38)
    if xamo.CJdsfDH(39) == 1:
        xamo.LJDFnmeFSD(39)
    if xamo.CJdsfDH(40) == 1:
        xamo.LJDFnmeFSD(40)
    if xamo.CJdsfDH(37) == 0:
        xamo.KJDfekiHDh(37,1)
        time.sleep(0.05)
        xamo.LKDFemrrh(37)
def 向右():
    if xamo.CJdsfDH(38) == 1:
        xamo.LJDFnmeFSD(38)
    if xamo.CJdsfDH(37) == 1:
        xamo.LJDFnmeFSD(37)
    if xamo.CJdsfDH(40) == 1:
        xamo.LJDFnmeFSD(40)
    if xamo.CJdsfDH(39) == 0:
        xamo.KJDfekiHDh(39,1)
        time.sleep(0.05)
        xamo.LKDFemrrh(39)
def 向上():
    if xamo.CJdsfDH(40) == 1:
        xamo.LJDFnmeFSD(40)
    if xamo.CJdsfDH(37) == 1:
        xamo.LJDFnmeFSD(37)
    if xamo.CJdsfDH(39) == 1:
        xamo.LJDFnmeFSD(39)
    if xamo.CJdsfDH(38) == 0:
        xamo.LKDFemrrh(38)
def 向下():
    if xamo.CJdsfDH(38) == 1:
        xamo.LJDFnmeFSD(38)
    if xamo.CJdsfDH(37) == 1:
        xamo.LJDFnmeFSD(37)
    if xamo.CJdsfDH(39) == 1:
        xamo.LJDFnmeFSD(39)
    if xamo.CJdsfDH(40) == 0:
        xamo.LKDFemrrh(40)
def 左上():
    if xamo.CJdsfDH(39) == 1:
        xamo.LJDFnmeFSD(39)
    if xamo.CJdsfDH(40) == 1:
        xamo.LJDFnmeFSD(40)
    if xamo.CJdsfDH(37) == 0:
        xamo.KJDfekiHDh(37,1)
        time.sleep(0.05)
        xamo.LKDFemrrh(37)
        time.sleep(0.1)
    if xamo.CJdsfDH(38) == 0:
        xamo.LKDFemrrh(38)
def 左下():
    if xamo.CJdsfDH(38) == 1:
        xamo.LJDFnmeFSD(38)
    if xamo.CJdsfDH(39) == 1:
        xamo.LJDFnmeFSD(39)

    if xamo.CJdsfDH(37) == 0:
        xamo.KJDfekiHDh(37,1)
        time.sleep(0.05)
        xamo.LKDFemrrh(37)
        time.sleep(0.1)
    if xamo.CJdsfDH(40) == 0:
        xamo.LKDFemrrh(40)
def 右上():
    if xamo.CJdsfDH(37) == 1:
        xamo.LJDFnmeFSD(37)
    if xamo.CJdsfDH(40) == 1:
        xamo.LJDFnmeFSD(40)

    if xamo.CJdsfDH(39) == 0:
        xamo.KJDfekiHDh(39,1)
        time.sleep(0.05)
        xamo.LKDFemrrh(39)
        time.sleep(0.1)
    if xamo.CJdsfDH(38) == 0:
        xamo.LKDFemrrh(38)
def 右下():
    if xamo.CJdsfDH(37) == 1:
        xamo.LJDFnmeFSD(37)
    if xamo.CJdsfDH(38) == 1:
        xamo.LJDFnmeFSD(38)

    if xamo.CJdsfDH(39) == 0:
        xamo.KJDfekiHDh(39,1)
        time.sleep(0.05)
        xamo.LKDFemrrh(39)
        time.sleep(0.1)
    if xamo.CJdsfDH(40) == 0:
        xamo.LKDFemrrh(40)
def 弹起():
    xamo.LJDFnmeFSD(37)
    xamo.LJDFnmeFSD(38)
    xamo.LJDFnmeFSD(39)
    xamo.LJDFnmeFSD(40)
def 截图(x,y,x1,y1,name):
    bbox = (x,y,x1,y1)
    im = ImageGrab.grab(bbox)
    im.save(name)
def get_ini(name, section, option,moren):
    try:
        cf = configparser.ConfigParser()
        cf.read(name)
        temp = cf.get(section, option)
        return temp
    except:
        return moren
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
def loop():
    HOST = '47.92.87.126'
    PORT = 8680
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    b = os.getcwd()
    print(b)
    try:
        f = open('ver', 'r')
        f.close()
    except IOError:
        b = os.getcwd()
        print(b)
        if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs(b)
        xxoo = b + '/ver'  # 在当前py文件所在路径下的new文件中创建txt
        file = open(xxoo, 'w')
        file.write('1')  # 写入内容信息
        file.close()
    with open('ver', 'r') as f:
        ver = f.read()
    while True:
        print('检查版本')
        #检查版本
        try:
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
            tcpCliSock.send('bb'.encode())
            data = tcpCliSock.recv(BUFSIZ)
            if data:
                strs= data.decode('utf-8')
                if isinstance(strs,str):
                    print(strs + '=' + ver)
                    if ver != strs:
                        with open('ver', 'w') as f:
                            f.write(strs)
                        弹起()
                        dw.AQkYZXxNfqMz('update.exe', 0)
        except:
            print('检查版本失败')
        time.sleep(10)
def log(leixing,zhanghao,strs):
    # 格式=jl|类型|账号|文本|时间
    HOST = '47.92.87.126'
    PORT = 8680
    ADDR = (HOST, PORT)
    user = 'weijiawl'
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        date = datetime.datetime.now()
        tcpCliSock.send(('jl|'+ user + '|' + leixing + '|' + zhanghao + '|' + strs + '|' + date.strftime('%Y-%m-%d %H:%M:%S')).encode())
    except:
        print('发送日志失败')
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
    num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
    juese = get_ini("config/记录.ini", "刷号记录", "当前角色","")
    qu  = get_ini("config/记录.ini", "刷号记录", "当前大区","")
    date = datetime.datetime.now()
    set_ini('config/记录.ini', '完成时间', num + '_' + qu + '_' + juese, date.strftime('%Y-%m-%d %H:%M:%S'))
def jiluwanchengshijian_zhuanqian():
    num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
    set_ini('config/记录.ini', '转账', num,'完成')
def get_pc_name():
    return os.environ['COMPUTERNAME']
def prints(strs):
    try:
        print(strs)
        #tk.text(strs)
        #pass
        # with open('config/日志.txt', 'a+') as f:
        #     f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '#编号=(' + account.zhanghaobianhao +')=' +account.hao+ '=' + account.mi + '=' + account.daqu + '=' + account.dangqianjuese + '/' + account.zongjuese + '=' +'【' + strs + '】' + '\n')
        #print(datetime.datetime.now().strftime("%H:%M") + '#编号=(' + account.zhanghaobianhao +')=' +account.hao+ '=' + account.mi + '=' + account.daqu + '=' + account.dangqianjuese + '/' + account.zongjuese + '=' +'【' + strs + '】')
    except:
        print("报错######打印信息失败")
def shuaxinliebiao():
    pass
    #tk.trickit()
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
    dw.AQkYZXxNfqMz('清理.bat',0)
    time.sleep(5)
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
    p_now = get_ini("config/记录.ini", "封号", num,"")
    if p_now != "":
        temp = riqibijiao(p_now)
        if temp:
            remove_option("config/记录.ini", "封号", num)
            return True
        return False
    else:
        return True
def zhicaichaxun(num):
    p_now = get_ini("config/记录.ini", "制裁", num,"")
    if p_now != "":
        temp = riqibijiao(p_now)
        if temp:
            remove_option("config/记录.ini", "制裁", num)
            return True
        return False
    else:
        return True
def zhuanzhangchaxun(num):
    p_now = get_ini("config/记录.ini", "转账", num,"")
    if p_now != "":
        return False
    return True
def wanchengchaxun(num):
    p_now = get_ini("config/记录.ini", "完成", num,"")
    if p_now != "":
        return False
    return True
def get_account(path):
    prints("获取账号")
    try:
        pc_name = get_pc_name()
        for ic in range(500):
            num = get_ini(path,pc_name,str(ic + 1),"")
            if num != "":
                arr = num.split("=")
                hao = arr[0]
                juese = arr[3]
                #检查封号
                if fenghaochaxun(hao) and zhicaichaxun(hao) and wanchengchaxun(hao+'_'+arr[2]):
                    #逐角色判断时间
                    for i in range(int(juese)):
                        returns_now = get_ini('config/记录.ini', '完成时间', hao + '_' + arr[2] + '_' + str(int(i) + 1),"")
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
            num = get_ini(path,pc_name,str(ic + 1),"")
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
        # dengji_gld = get_ini('config/cfg.ini', '游戏配置', "等级上限","")
        # dengji_gt = get_ini('config/cfg.ini', '游戏配置', "等级上限_钢铁","")
        zongjuese = get_ini('config/记录.ini', '刷号记录', "当前角色数","")
        juese = get_ini('config/记录.ini', '刷号记录', "当前角色","")
        qu = get_ini("config/记录.ini", "刷号记录", "当前大区","")
        hao = get_ini("config/记录.ini", "刷号记录", "当前账号","")
        try:
            if zongjuese == "" and juese == "" and qu == "" and hao == "":
                os.remove("config/记录.ini")
                return 3
        except:
            os.remove("config/记录.ini")
            return 3
        p_x =[70,192,314,436,70,192,314,436]
        p_y =[256,256,256,256,464,464,464,464]
        juese_time = datetime.datetime.now()
        while True:
            time.sleep(0.5)
            FinStr = dw.RsJCdWDvHA(507, 531, 593, 564, "结束游戏", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                break
            else:
                xamo.KJDfekiHDh(27,1)
                time.sleep(3)
                FinStr = dw.RsJCdWDvHA(360, 459, 413, 477, "选择角色", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx + 10, inty - 10)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(5)
            time.sleep(1)
            juese_time_now = datetime.datetime.now()
            time_temp = juese_time_now.minute - juese_time.minute
            if time_temp > 3:
                qingkongyouxichuangkou()
                return 3
        xamo.UIKBudj(1, 1)
        time.sleep(1)
        #1 = 上角色,2 = 换角色
        if leixing == 2:
            juese = str(int(juese) + 1)
            if int(juese) > int(zongjuese):
                return 0
        #判断当前角色前面的角色是否更新疲劳
        for i in range(int(juese)):
            returns_now = get_ini('config/记录.ini', '完成时间', hao + '_' + qu + '_' + str(int(i) + 1),"")
            if returns_now != "":
                if gengxin(returns_now) == True:
                    juese = str(i + 1)
                    break
            else:
                juese = str(i+1)
        while True:
            time.sleep(0.5)
            FinStr = dw.RsJCdWDvHA(507, 531, 593, 564, "结束游戏", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if int(juese) <= 8:
                    juese_index = 1
                    #上拉
                    for i in range(3):
                        xamo.UIKBudj(579, 92)
                        time.sleep(0.2)
                        xamo.KFNVCnehsdg(1)
                        time.sleep(0.5)
                elif int(juese) <= 12:
                    juese_index = 5
                    # 上拉
                    for i in range(5):
                        xamo.UIKBudj(579, 92)
                        time.sleep(0.2)
                        xamo.KFNVCnehsdg(1)
                        time.sleep(0.5)
                    # 下拉一下
                    xamo.UIKBudj(579, 495)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                elif int(juese) <= 16:
                    juese_index = 9
                    # 上拉
                    for i in range(5):
                        xamo.UIKBudj(579, 92)
                        time.sleep(0.2)
                        xamo.KFNVCnehsdg(1)
                        time.sleep(0.5)
                    xamo.UIKBudj(579, 495)
                    time.sleep(1)
                    # 下拉二下
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                #等级检查关闭，不到84自动练级
                #检查等级
                lv = dw.ghKWigkPfdBCtSd(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index], p_x[int(juese) - juese_index] + 60,p_y[int(juese) - juese_index] + 18, "d1b994-000000", 1)
                if lv != "":
                    lv = re.sub("\D", "", lv)
                    if int(lv) < 85:
                        set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                        account.dangqianjuese = juese
                        prints("等级不够卡图，换下个角色")
                        juese = str(int(juese) + 1)
                        if int(juese) > int(zongjuese):
                            set_ini("config/记录.ini", "完成", hao + '_' + qu, '完成')
                            return 0
                        continue
                #     # 地图分配
                #     if int(lv) >= int(dengji_gt):
                #         set_ini('config/记录.ini', '地图', "地图ID", str(t_gangtie))
                #         dw.UIKBudj(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index])
                #     elif int(lv) >= int(dengji_gld):
                #         set_ini('config/记录.ini', '地图', "地图ID", str(t_gelandi))
                #         dw.UIKBudj(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index])
                print('角色数 = ' + juese)
                #点击角色
                xamo.UIKBudj(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index])
                time.sleep(0.5)
                xamo.KFNVCnehsdg(1)
                time.sleep(0.5)
                #点击开始
                xamo.UIKBudj(402, 548)
                time.sleep(0.2)
                xamo.KFNVCnehsdg(1)
                time.sleep(5)
            FinStr = dw.RsJCdWDvHA(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.uEKuRfCL(365, 356, 418, 384, "签到.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.RsJCdWDvHA(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.uEKuRfCL(768, 1, 800, 31, "图外.bmp|图外1.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            # FinStr = dw.uEKuRfCL(768, 1, 800, 31, "图内.bmp", "000000", "0.9", 0)
            # pos = FinStr.split('|')
            # if int(pos[1]) > 0:
            #     account.dangqianjuese = juese
            #     set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
            #     return 1
            FinStr = dw.RsJCdWDvHA(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 2
            FinStr = dw.uEKuRfCL(242, 430, 316, 490, "金麦克.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty - 10)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                xamo.KJDfekiHDh(27,1)
                time.sleep(2)
                xamo.UIKBudj(372, 319)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(3)
            time.sleep(1)
            juese_time_now = datetime.datetime.now()
            time_temp = juese_time_now.minute - juese_time.minute
            if time_temp > 3:
                return 3
    except:
        prints("报错######选择角色失败")
        input()
def zhongduan_cha():
    FinStr = dw.RsJCdWDvHA(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        prints("网络连接中断")
        intx = int(pos[1])
        inty = int(pos[2])
        xamo.UIKBudj(intx + 37, inty - 29)
        time.sleep(1)
        xamo.cndjGdsbSdg()
        time.sleep(1)
        xamo.UIKBudj(406, 48)
        time.sleep(1)
        xamo.mboHdjGsV()
        time.sleep(1)
        FinStr = dw.RsJCdWDvHA(234, 243, 562, 400, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "第三方模块", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints("第三方模块，重启")
                log('三方', account.hao, '三方模块')
                end_exsit(2)
                time.sleep(2)
                #重启电脑
                run('shutdown -r', shell=True)
                time.sleep(20)
                return 1
            FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "制裁1小时", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(seconds=7200)
                n_days = d1 + delta
                num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                prints("制裁一个小时，换号")
                log('制裁', account.hao, '一小时')
                end_exsit(2)
                time.sleep(2)
                return 1
            FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "制裁一天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(days=1)
                n_days = d1 + delta
                num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                prints("制裁一天，换号")
                log('制裁', account.hao, '一天')
                end_exsit(2)
                time.sleep(60)
                return 1
            FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "制裁15天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(days=15)
                n_days = d1 + delta
                num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                prints("制裁15天，换号")
                log('制裁', account.hao, '15天')
                end_exsit(2)
                time.sleep(60)
                return 1
            prints('中断制裁未识别，请把【中断截图】文件夹中的截图发给作者')
            dw.BRjQifPapFtzcvC(234, 243, 562, 335, str(time.time()) + '.bmp')
        else:
            prints("只是中断没有制裁，重上")
            end_exsit(2)
            time.sleep(2)
        return 1
    return 0
def jianceanquanmoshi(p_xgis,p_xguer,p_xgpwd):
    try:
        prints("检查安全模式")
        qingkongyouxichuangkou()
        while True:
            FinStr = dw.RsJCdWDvHA(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 23, inty + 76)
                time.sleep(2)
                xamo.KFNVCnehsdg(1)
                time.sleep(2)
                xamo.UIKBudj(intx + 23 + 60, inty + 76 + 55)
                time.sleep(2)
                xamo.KFNVCnehsdg(1)
                time.sleep(2)
            FinStr = dw.RsJCdWDvHA(210, 511, 276, 539, "出售", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intxa = int(pos[1])
                intya = int(pos[2])
                #点击出售
                xamo.UIKBudj(intxa + 10, intya + 3)
                time.sleep(2)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                #点击材料
                xamo.UIKBudj(590, 246)
                time.sleep(2)
                xamo.KFNVCnehsdg(1)
                time.sleep(2)
                #鼠标移开
                while True:
                    if zhongduan_cha() == 1:
                        break
                    # 点击出售
                    xamo.UIKBudj(intxa + 10, intya + 3)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    xamo.UIKBudj(608, 176)
                    time.sleep(1)
                    FinStr = dw.uEKuRfCL(473, 258, 715, 409, "黑曜石.bmp|血滴石.bmp|金刚石.bmp|紫玛瑙.bmp|迪卡斯印章.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 5, inty + 5)
                        time.sleep(2)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.8)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.8)
                        xamo.PPWEbxbar(1)
                        time.sleep(2)
                    else:
                        break
                    FinStr = dw.RsJCdWDvHA(310, 307, 427, 361, "安全模式", "ddc593-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints(account.hao + '|' + account.mi + "出现安全模式，等待解除")
                        if p_xgis == '真':
                            prints('小果解除安全模式')
                            p_qq = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                            xaoguo_return = xiaoguo.jiandanjieanquan(p_qq,p_xguer,p_xgpwd)
                            if xaoguo_return == True:
                                prints('小果解除安全模式 成功')
                            else:
                                prints('小果解除安全模式 失败')
                        while True:
                            # 等待解除安全模式
                            FinStr = dw.RsJCdWDvHA(287, 250, 496, 319, "退出安全模式", "ffffff-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                intx = int(pos[1])
                                inty = int(pos[2])
                                qingkongyouxichuangkou()
                                break
                            time.sleep(2)
                            if zhongduan_cha() > 0:
                                break
                        break
                break
    except:
        prints("报错######检查安全模式失败")
def qingkongyouxichuangkou():
    try:
        while True:
            FinStr = dw.uEKuRfCL(585, 117, 628, 140, "关闭系统菜单.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 5)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                FinStr = dw.RsJCdWDvHA(307, 242, 362, 274, "邮件箱", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    xamo.UIKBudj(intx + 10, inty + 5)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(0.5)
                    break
                else:
                    break
            else:
                xamo.UIKBudj(1, 1)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.KJDfekiHDh(27,1)
                time.sleep(1)
    except:
        prints("报错######清空游戏窗口失败")
def fayoujian(CRuser, CRpwd):
    prints("发送邮件")
    kuaqu = ""
    money = get_ini('config/cfg.ini','游戏配置', '邮寄金币上限',"1000000")
    qu = get_ini("config/记录.ini", "刷号记录", "当前大区","")
    name = get_ini('config/仓库设置.ini',qu, "仓库名称","")
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
            FinStr = dw.RsJCdWDvHA(307, 242, 362, 274, "邮件箱", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty - 10)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(3)
            else:
                xamo.KJDfekiHDh(27,1)
                time.sleep(3)
            FinStr = dw.RsJCdWDvHA(338, 138, 419, 169, "邮件保管箱", "ddc593-000000", 1)
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
            time.sleep(0.5)
        #检查金币
        number = dw.ghKWigkPfdBCtSd(610, 529, 700, 549,"e6c89b-000000",1)
        if int(number) < int(money):
            prints("游戏币不够设置的金额")
            qingkongyouxichuangkou()
            return
        while True:
            FinStr = dw.RsJCdWDvHA(278, 139, 341, 171, "发送邮件", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx+10, inty+3)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
            FinStr = dw.RsJCdWDvHA(202, 169, 246, 191, "收件人", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 104, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(3)
                hwnd = dw.bcGT("地下城与勇士", "地下城与勇士")
                if hwnd > 0:
                    dw.gshNarIzNfhm(hwnd, name)
                time.sleep(3)
                xamo.UIKBudj(intx + 203, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
            time.sleep(0.5)
        while True:
            FinStr = dw.RsJCdWDvHA(315, 261, 451, 294, "选择接收区", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                if kuaqu == "":
                    xamo.UIKBudj(intx + 72, inty + 60)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    #大区确认
                    xamo.UIKBudj(400, 340)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    break
                else:
                    #点击下拉列表
                    xamo.UIKBudj(462, 299)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(3)
                    while True:
                        FinStr = dw.RsJCdWDvHA(323, 307, 369, 475, kuaqu, "ddc593-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            intx = int(pos[1])
                            inty = int(pos[2])
                            #选择跨区
                            xamo.UIKBudj(intx + 5, inty + 3)
                            time.sleep(1)
                            xamo.PPWEbxbar(1)
                            time.sleep(3)
                            #确认
                            xamo.UIKBudj(397, 326)
                            time.sleep(1)
                            xamo.PPWEbxbar(1)
                            time.sleep(3)
                            # 大区确认
                            xamo.UIKBudj(400, 340)
                            time.sleep(1)
                            xamo.PPWEbxbar(1)
                            time.sleep(5)
                            break
                        else:
                            xamo.UIKBudj(467, 460)
                            time.sleep(1)
                            xamo.PPWEbxbar(1)
                            time.sleep(2)
                        fyj_time_now = datetime.datetime.now()
                        time_temp = fyj_time_now.minute - fyj_time.minute
                        if time_temp > 3:
                            prints("发邮件超时，取消")
                            qingkongyouxichuangkou()
                            return
                        time.sleep(0.5)
                    break
            if zhongduan_cha() >0:
                return 2
            fyj_time_now = datetime.datetime.now()
            time_temp = fyj_time_now.minute - fyj_time.minute
            if time_temp > 3:
                prints("发邮件超时，取消")
                qingkongyouxichuangkou()
                return 3
            time.sleep(0.5)
                    #添加发送物品
        #添加附件
        xamo.UIKBudj(317, 378)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        #选择材料
        xamo.UIKBudj(590, 246)
        time.sleep(1)
        xamo.KFNVCnehsdg(1)
        time.sleep(3)
        tianjiashuliang = 0
        wuse_is = True
        while True:
            FinStr = dw.uEKuRfCL(472, 256, 767, 436, "魔刹石.bmp|挑战书.bmp|无尽的永恒.bmp|数据芯片.bmp|迷幻晶石.bmp|强烈之痕迹.bmp|矛盾的结晶体.bmp|浓缩的异界精髓.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 3, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                tianjiashuliang = tianjiashuliang + 1
            else:
                break
            if wuse_is:
                FinStr = dw.uEKuRfCL(472, 256, 767, 436, "无色小晶体.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx + 3, inty + 5)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    if int(pos[0]) == 0:
                        ws_sl = dw.ghKWigkPfdBCtSd(627, 313, 742, 396, "ffe3ab-000000", 1)
                        ws_sl = re.sub("\D", "", ws_sl)
                        xamo.LbferJhd(str(int(ws_sl) - 200))
                        time.sleep(0.5)
                        xamo.KJDfekiHDh(13,1)
                        time.sleep(1)
                        xamo.UIKBudj(0, 0)
                    else:
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                    tianjiashuliang = tianjiashuliang + 1
                    wuse_is = False
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
        xamo.UIKBudj(638, 246)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        while True:
            FinStr = dw.uEKuRfCL(472, 260, 716, 413, "紫色卡片.bmp|粉色卡片.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 10)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(3)
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
        xamo.UIKBudj(333, 412)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        prints("税前 = " + number)
        bl = int(int(number) / 100 * 7)
        number = str(int(number) - bl)
        prints("税后 = " + number)
        log('支出',account.hao,str(number))
        xamo.LbferJhd(number)
        time.sleep(1)
        #发送
        xamo.UIKBudj(261, 461)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(1)
        xamo.UIKBudj(261 - 60, 461)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        while True:
            FinStr = dw.uEKuRfCL(232, 69, 693, 499, "发邮件验证码.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                time.sleep(1)
                intx = int(pos[1])
                inty = int(pos[2])
                #打码
                dw.BRjQifPapFtzcvC(intx - 207, inty - 22, intx - 78, inty + 30, os.getcwd() + "/ver.jpg")
                time.sleep(0.5)
                dc = rk.RClient(CRuser, CRpwd, "92131", "4e1ce1108f244c6381d5bcfdbe368ae4")
                im = open(os.getcwd() + '/ver.jpg', 'rb').read()
                yzm = dc.rk_create(im, "3040")
                xy = yzm["Result"]
                xamo.UIKBudj(intx + 35, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                for n in range(6):
                    xamo.KJDfekiHDh(8,1)
                    time.sleep(0.5)
                time.sleep(1)
                xamo.LbferJhd(xy)
                time.sleep(1)
                xamo.UIKBudj(intx -123, inty + 131)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(5)
                FinStr = dw.RsJCdWDvHA(346, 278, 449, 309, "已成功发送邮件", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    qingkongyouxichuangkou()
                    break
                else:
                    xamo.UIKBudj(410, 176)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    xamo.UIKBudj(400, 339)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    xamo.UIKBudj(262, 462)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(4)
            time.sleep(1)
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
    x = dw.yTKUBaTqevaYZRU()
    y = dw.vgtwHdrCtErzwk()
    login_time = datetime.datetime.now()
    while True:
        liudiangengxin()
        if money_is == '真':
            hao, mi, qu, jue = get_account_zhuanqian(account_path)
        else:
            hao, mi, qu, jue = get_account(account_path)
        if hao == "":
            prints('没有没有可刷账号，等待6点更新')
            time.sleep(30)
            #return 101
        else:
            break
    dw.AQkYZXxNfqMz(WeGame,0)
    # 恢复打印机窗口
    try:
        jc_DNF = True
        while True:
            time.sleep(0.5)
            # if jc_DNF:
                # if check_exsit("DNF.exe") == 1:
                #     time.sleep(10)
                #     run('taskkill /F /IM tgp_daemon.exe', shell=True)
                #     jc_DNF = False
            FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp挤掉.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if check_exsit("DNF.exe") == 0:
                    dw.AQkYZXxNfqMz('清理.bat', 0)
                    time.sleep(30)
                    login_time = datetime.datetime.now()
                    dw.AQkYZXxNfqMz(WeGame, 0)
            FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp_登录.bmp|tgp_登录1.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                #刷新列表
                shuaxinliebiao()
                xamo.UIKBudj(intx + 70, inty - 136)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                for i in range(13):
                    xamo.KJDfekiHDh(8,1)
                    time.sleep(0.2)
                time.sleep(0.5)
                #输入账号
                xamo.LbferJhd(hao)
                time.sleep(0.5)
                xamo.UIKBudj(intx + 70, inty - 106)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                #输入密码
                xamo.LbferJhd(mi)
                time.sleep(0.5)
                #点击登录
                xamo.UIKBudj(intx, inty)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                xamo.UIKBudj(intx + 30, inty + 30)
            FinStr = dw.RsJCdWDvHA(0, 0, x, y, "拖动滑块", "000000-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                print('验证码')
                intx = int(pos[1])
                inty = int(pos[2])
                time.sleep(2)
                截图(intx + 1,inty + 22, intx + 280, inty + 179, os.getcwd() + "/ver.jpg")
                time.sleep(0.5)
                dc = rk.RClient(CRuser, CRpwd, "92131", "4e1ce1108f244c6381d5bcfdbe368ae4")
                im = open(os.getcwd() + '/ver.jpg', 'rb').read()
                yzm = dc.rk_create(im, "6137")
                xy = yzm["Result"]
                px = intx + 43
                py = inty + 199
                xamo.UIKBudj(px, py)
                time.sleep(1)
                xamo.cndjGdsbSdg()
                time.sleep(1)
                xamo.UIKBudj(px + int(xy.split(',')[0]) - 38, py)
                time.sleep(1)
                xamo.mboHdjGsV()
                time.sleep(5)
                #确认后延迟大点
            FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp_跳过.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty+3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.RsJCdWDvHA(0, 0, x, y, "今日推荐", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 403, inty + 8)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp_主页.bmp|tgp_主页1.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 10)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.uEKuRfCL(0, 0, x, y, "更新游戏.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 20, inty + 10)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp_开始游戏.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intxa = int(pos[1])
                intya = int(pos[2])
                FinStr = dw.RsJCdWDvHA(intxa - 321 , intya - 16, intxa - 199, intya + 30, qu, "3c3c3c-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    xamo.UIKBudj(intxa + 20, intya + 10)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    shubiaodianji = True
                else:
                    xamo.UIKBudj(intxa - 116, intya + 10)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    FinStr = dw.RsJCdWDvHA(intxa - 326, intya - 186, intxa - 251, intya - 21, qu, "3c3c3c-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx +10, inty + 3)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(2)
            else:
                FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp_列表_dnf.bmp|tgp_列表_dnf1.bmp", "000000", "1", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
            FinStr = dw.RsJCdWDvHA(0, 0, x, y, "优化跳过", "3c3c3c-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx -384, inty + 8)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.UIKBudj(intx, inty)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(2)
            FinStr = dw.RsJCdWDvHA(0, 0, x, y, "跳过检测", "2098ff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.uEKuRfCL(0, 0, x, y, "tgp_登录失败.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 0
            FinStr = dw.RsJCdWDvHA(0, 0, x, y, "连接频道失败", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 0
            FinStr = dw.RsJCdWDvHA(0, 0, x, y, "结束游戏", "ddc593-000000|ffffb8-000000", 0.9)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                print('角色界面')
                hwnda = dw.bcGT("", "打印机")
                if hwnda > 0:
                    dw.cqMQFoSnghY(hwnda, 12)
                return 1
            if shubiaodianji:
                xamo.UIKBudj(1, 1)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            login_time_now = datetime.datetime.now()
            time_temp = login_time_now.minute - login_time.minute
            if time_temp > 6:
                return 3
    except:
        prints("报错######登录账号失败")
        input()
def fenghaojianhcha():
    FinStr = dw.RsJCdWDvHA(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        prints("网络连接中断")
        intx = int(pos[1])
        inty = int(pos[2])
        xamo.UIKBudj(intx + 37, inty - 29)
        time.sleep(1)
        xamo.cndjGdsbSdg()
        time.sleep(1)
        xamo.UIKBudj(406, 48)
        time.sleep(1)
        xamo.mboHdjGsV()
        time.sleep(2)
        FinStr = dw.RsJCdWDvHA(234, 243, 562, 400, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.RsJCdWDvHA(238, 243, 562, 335, "停封5天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                number = dw.ghKWigkPfdBCtSd(414, 291, 526, 307, "ffffff-000000", 1)
                if number != "":
                    number = number.replace('/','-',2)
                    number = number.replace('/',' ',1)
                    prints(number)
                    log('停封', account.hao, "停封5天")
                    try:
                        d1 = datetime.datetime.strptime(number,'%Y-%m-%d %H:%M')
                        #获取的时间上+100秒只是为了获取到一个完整格式
                        #也可以用days加天数
                        delta = datetime.timedelta(seconds=100)
                        n_days = d1 + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                    except:
                        n_days = datetime.datetime.now()
                        delta = datetime.timedelta(days=1)
                        n_days = n_days + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                return 'F5'
            FinStr = dw.RsJCdWDvHA(238, 243, 562, 335, "停封7天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                number = dw.ghKWigkPfdBCtSd(414, 291, 526, 307, "ffffff-000000", 1)
                if number != "":
                    number = number.replace('/','-',2)
                    number = number.replace('/',' ',1)
                    prints(number)
                    log('停封', account.hao, "停封7天")
                    try:
                        d1 = datetime.datetime.strptime(number,'%Y-%m-%d %H:%M')
                        #获取的时间上+100秒只是为了获取到一个完整格式
                        #也可以用days加天数
                        delta = datetime.timedelta(seconds=100)
                        n_days = d1 + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                    except:
                        n_days = datetime.datetime.now()
                        delta = datetime.timedelta(days=1)
                        n_days = n_days + delta
                        num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                        set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                return 'F7'
            FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "永久封号", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                d1 = datetime.datetime.now()
                # 也可以用days加天数,seconds加秒
                delta = datetime.timedelta(days=365)
                n_days = d1 + delta
                log('停封', account.hao, "永久封号")
                num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
                set_ini("config/记录.ini", "封号", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
                return 'F100'
            FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "第三方模块", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints("第三方模块，重启")
                log('三方', account.hao, "三方模块")
                end_exsit(2)
                time.sleep(2)
                return 'F0'
            prints('封号类型未识别，请把【中断截图】文件夹中的截图发给作者')
            dw.BRjQifPapFtzcvC(234, 243, 562, 335, str(time.time()) + '.bmp')
        else:
            return 'F0'
    FinStr = dw.RsJCdWDvHA(234, 243, 562, 335, "此ID已在游戏", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 'F101'
    return ''
def yongbingchuzhan():
    prints('佣兵出战')
    while True:
        FinStr = dw.RsJCdWDvHA(390, 85, 440, 120, "佣兵", "ffffb8-000000|ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 10, inty + 5)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            FinStr = dw.uEKuRfCL(510, 325, 604, 363, "佣兵_领取奖励.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                #选择领取奖励的佣兵
                xamo.UIKBudj(365, 197)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                #确认
                xamo.UIKBudj(363, 319)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                qingkongyouxichuangkou()
            FinStr = dw.uEKuRfCL(513, 323, 599, 363, "佣兵_佣兵出战.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                #确认
                xamo.UIKBudj(361, 326)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                qingkongyouxichuangkou()
                break
            FinStr = dw.uEKuRfCL(503, 323, 614, 369, "佣兵_取消出战.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                qingkongyouxichuangkou()
                break
            FinStr = dw.uEKuRfCL(513, 323, 599, 363, "佣兵_佣兵出战_灰.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                qingkongyouxichuangkou()
                break
        else:
            xamo.UIKBudj(781,521)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(2)
        if zhongduan_cha() == 1:
            break
        time.sleep(1)
def qingchushuatujilu():
    try:
        config = configparser.ConfigParser()
        config.read("config/记录.ini")
        ret = config.options('完成时间')
        prints('完成时间数量 = ' + str(ret))
        if len(ret) > 0:
            for i in ret:
                config.remove_option("完成时间", i)
        config.write(open("config/记录.ini", "w"))
    except:
        pass
    try:
        config = configparser.ConfigParser()
        config.read("config/记录.ini")
        ret = config.options('完成')
        if len(ret) > 0:
            for i in ret:
                config.remove_option("完成", i)
        config.write(open("config/记录.ini", "w"))
    except:
        pass
def liudiangengxin():
    try:
        temp = get_ini("config/记录.ini", "更新", '六点更新',"")
        d2 = datetime.datetime.now()
        print("d1 = " + temp + ",d2 = " + d2.strftime("%Y-%m-%d %H:%M:%S"))
        if temp != "":
            d1 = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S')
            days = d2.day - d1.day
            day = d2 - d1
            if day.days >= 1:
                qingchushuatujilu()
                shuaxinliebiao()
                prints('六点更新成功')
                set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
            elif days > 1:
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
            set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
    except:
        prints('六点更新失败')
def saotubiao():
    xamo.UIKBudj(689, 945)
    xamo.UIKBudj(1266, 945)
def chushoudianquan():
    prints('兑换点券')
    int_quan = 0
    while True:
        FinStr = dw.RsJCdWDvHA(578, 401, 784, 560, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            number = dw.ghKWigkPfdBCtSd(intx - 178, inty + 45, intx - 124, inty + 69, "e6c89b-000000", 1)
            number = re.sub("\D", "", number)
            prints('点券 = ' + number)
            if int(number) >= 1000:
                if int(number) >= 4500:
                    int_quan = 1
                break
            else:
                return 0
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(2)
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
        FinStr = dw.RsJCdWDvHA(41, 534,114, 566, "寄售金币", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.uEKuRfCL(160, 545, 191, 573, "商城.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                xamo.UIKBudj(761, 24)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(2)
            FinStr = dw.RsJCdWDvHA(34, 148, 89, 418, wenzi, "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 3)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                #搜索
                xamo.UIKBudj(516, 89)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                for i in range(10):
                    FinStr = dw.RsJCdWDvHA(484, 122, 540, 309, '购买', "ffb400-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        #购买
                        xamo.UIKBudj(570, 290)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.5)
                        xamo.UIKBudj(570+55, 290+12)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.5)
                        xamo.UIKBudj(570+55+57, 290+12+23)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(6)
                        aq_ret = 安全模式()
                        if aq_ret == 1:
                           break
                        FinStr = dw.RsJCdWDvHA(293, 235, 503, 356, '拍卖行不存在', "ffffff-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            xamo.UIKBudj(400, 319)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                            while True:
                                FinStr = dw.uEKuRfCL(160, 545, 191, 573, "商城.bmp", "000000", "0.9", 0)
                                pos = FinStr.split('|')
                                if int(pos[1]) > 0:
                                    xamo.UIKBudj(400, 557)
                                    time.sleep(0.5)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(0.5)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(2)
                                    xamo.UIKBudj(761, 24)
                                    time.sleep(0.5)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(2)
                                    break
                                else:
                                    xamo.UIKBudj(483, 580)
                                    time.sleep(0.5)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(3)
                            break
                        FinStr = dw.RsJCdWDvHA(293, 235, 503, 356, '完成竞拍', "ffffff-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            xamo.UIKBudj(400, 319)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                            break
                    #红色购买
                    FinStr = dw.RsJCdWDvHA(484, 122, 540, 309, '购买', "ff3232-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        if wenzi == '一千万':
                            wenzi = '一百万'
                        elif wenzi == '一百万':
                            wenzi = ""
                        break
                    time.sleep(0.5)
            else:
                xamo.UIKBudj(37, 136)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
        else:
            xamo.UIKBudj(386, 576)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            xamo.UIKBudj(367, 538)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(1)
def jieshouyoujian():
        FinStr = dw.uEKuRfCL(263, 462, 533, 551, "邮件.bmp|邮件1.bmp", "202020", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 3)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(3)
            FinStr = dw.RsJCdWDvHA(338, 138, 419, 169, "邮件保管箱", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                time.sleep(1)
                xamo.UIKBudj(298, 465)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(3)
                for i in range(10):
                    FinStr = dw.RsJCdWDvHA(345, 275, 450, 308, "邮件领取完毕", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        break
                    time.sleep(1)
def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            return fp
def jinqizhicai():
    FinStr = dw.RsJCdWDvHA(812, 26, 1114, 114, "近期出现异常|制裁", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
        a = dw.ghKWigkPfdBCtSd(812, 26, 1114, 114, "e6c89b-000000", 1)
        if a.find('小时') > -1:
            arr = a.split('小时')
            temp_h = re.sub("\D", "", arr[0])
            d1 = datetime.datetime.now()
            # 制裁的小时+1
            # 转换成秒加到当前时间
            prints('制裁' + str(int(temp_h) + 1) + '小时')
            log('制裁', account.hao, str(int(temp_h) + 1) + '小时')
            z_time = (int(temp_h) + 1) * 60 * 60
            delta = datetime.timedelta(seconds=z_time)
            n_days = d1 + delta
            set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
            prints("出现制裁,已记录制裁时间，换号")
            end_exsit(2)
            time.sleep(2)
        else:
            d1 = datetime.datetime.now()
            # 也可以用days加天数,seconds加秒
            # 制裁时间无法识别，先加一小时
            delta = datetime.timedelta(seconds=3600)
            n_days = d1 + delta
            set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
            prints("出现制裁等待一小时，换号")
            prints('近期制裁，请把文件夹中的截图发给作者')
            dw.BRjQifPapFtzcvC(812, 26, 1114, 114, os.getcwd() + '/' + str(time.time()) + '.bmp')
            end_exsit(2)
            time.sleep(2)
        return 1
    return 0
def 捡取():
    jianqucishu = 0
    my_x_py = 10
    my_y_py = 190
    wp_x_py = 12
    wp_y_py = -10
    jianqu_time = datetime.datetime.now()
    while True:
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        jianqu_time_now = datetime.datetime.now()
        d3 = jianqu_time_now - jianqu_time
        if d3.seconds > 20:
            jianqu_time = datetime.datetime.now()
            jianqucishu += 1
            if jianqucishu > 2:
                break
            if xamo.CJdsfDH(37) == 1:
                向右()
                time.sleep(0.5)
                弹起()
            elif xamo.CJdsfDH(39) == 1:
                向左()
                time.sleep(0.5)
                弹起()
            else:
                Rnd = random.randint(1,4)
                if Rnd == 1:
                    向上()
                    time.sleep(1)
                    弹起()
                elif Rnd == 2:
                    向下()
                    time.sleep(1)
                    弹起()
                elif Rnd == 3:
                    向左()
                    time.sleep(0.5)
                    弹起()
                elif Rnd == 4:
                    向右()
                    time.sleep(0.5)
                    弹起()
                break
        FinStr = dw.uEKuRfCL(0,78,799,552,"捡1.bmp|捡2.bmp|捡3.bmp|捡4.bmp","050505","0.95",0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            time.sleep(0.1)
            xamo.KJDfekiHDh(88,1)
            time.sleep(0.5)
        else:
            FinStr = dw.uEKuRfCL(0, 78, 799, 552, "my.bmp", "000000", "1", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                my_x = int(pos[1])
                my_y = int(pos[2])
            else:
                Rnd = random.randint(1, 4)
                if Rnd == 1:
                    向上()
                    time.sleep(1)
                    弹起()
                elif Rnd == 2:
                    向下()
                    time.sleep(1)
                    弹起()
                elif Rnd == 3:
                    向左()
                    time.sleep(0.5)
                    弹起()
                elif Rnd == 4:
                    向右()
                    time.sleep(0.5)
                    弹起()
            FinStr = dw.uEKuRfCL(0,78,799,552,"wp.bmp","000000","1",1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                wp_x = int(pos[1])
                wp_y = int(pos[2])
            else:
                弹起()
                break
        if my_x > 0 and my_y > 0 and wp_x > 0 and wp_y > 0:
            if abs((my_x+my_x_py) - (wp_x+wp_x_py)) < 10:
                if my_y+my_y_py > wp_y+wp_y_py:
                    向上()
                elif my_y+my_y_py < wp_y+wp_y_py:
                    向下()
            elif my_x+my_x_py > wp_x+wp_x_py:
                if  abs((my_y+my_y_py) - (wp_y+wp_y_py)) < 10:
                    向左()
                elif my_y+my_y_py > wp_y+wp_y_py:
                    左上()
                elif my_y+my_y_py < wp_y+wp_y_py:
                    左下()
            elif my_x+my_x_py < wp_x+wp_x_py:
                if  abs((my_y+my_y_py) - (wp_y+wp_y_py)) < 10:
                    向右()
                elif my_y+my_y_py > wp_y+wp_y_py:
                    右上()
                elif my_y+my_y_py < wp_y+wp_y_py:
                    右下()
        time.sleep(0.02)
def 判断方向(num):
    if num == 1:
        return "右"
    elif num == 2:
        return "右"
    elif num == 3:
        return "下"
    elif num == 4:
        return "下"
    elif num == 5:
        return "右"
    elif num == 6:
        return "上"
    elif num == 8:
        return "右"
    elif num == 9:
        return "右"
def 检查关卡():
    #第八关第九关为最左边的关卡正常不会走到那里
    x = [730, 748, 766, 766, 766, 784,784, 748, 748]
    y = [55, 55, 55, 73, 91, 91,74, 91, 74]
    for i in range(9):
        color = dw.LYqISzEsHWMD(x[i],y[i])
        if color == "0000ff":
            return i + 1
    return 0
def 找门(guanqia,p,jianqu):
    #p = 0 正常的问号找门
    #p = 1 错关找门
    prints("找门")
    d1 = datetime.datetime.now()
    my_x_py = 10
    my_y_py = 190
    wp_x_py = 12
    wp_y_py = 14
    z_g = 检查关卡()
    fangxiang = 判断方向(guanqia)
    if fangxiang == "右":
        x,y,x1,y1 = 689,130,791,525
        pic = "左右门.bmp"
        wp_x_py = 10
        wp_y_py = 75
    elif fangxiang == "上":
        x,y,x1,y1 = 0,119,798,345
        pic = "上门.bmp"
        wp_x_py = 35
        wp_y_py = -20
    elif fangxiang == "下":
        x,y,x1,y1 = 0,340,798,529
        pic = "下门.bmp"
        wp_x_py = 35
        wp_y_py = 100
    while True:
        time.sleep(0.05)
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        # FinStr = dw.uEKuRfCL(0,78,799,552, "可破坏.bmp", "000000", "0.9", 0)
        # pos = FinStr.split('|')
        # if int(pos[1]) > 0:
        #     打石头()
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        else:
            Rnd = random.randint(1, 4)
            if Rnd == 1:
                向上()
                time.sleep(1)
                弹起()
            elif Rnd == 2:
                向下()
                time.sleep(1)
                弹起()
            elif Rnd == 3:
                向左()
                time.sleep(0.5)
                弹起()
            elif Rnd == 4:
                向右()
                time.sleep(0.5)
                弹起()
        FinStr = dw.uEKuRfCL(x,y,x1,y1,pic,"000000","0.9",0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            wp_x = int(pos[1])
            wp_y = int(pos[2])
        else:
            if fangxiang == "左":
                向左()
            elif fangxiang == "右":
                向右()
            elif fangxiang == "上":
                向上()
            elif fangxiang == "下":
                向下()
        if my_x > 0 and my_y > 0 and wp_x > 0 and wp_y > 0:
            if abs((my_x+my_x_py) - (wp_x+wp_x_py)) < 10:
                if my_y+my_y_py > wp_y+wp_y_py:
                    向上()
                elif my_y+my_y_py < wp_y+wp_y_py:
                    向下()
            elif my_x+my_x_py > wp_x+wp_x_py:
                if  abs((my_y+my_y_py) - (wp_y+wp_y_py)) < 10:
                    向左()
                elif my_y+my_y_py > wp_y+wp_y_py:
                    左上()
                elif my_y+my_y_py < wp_y+wp_y_py:
                    左下()
            elif my_x+my_x_py < wp_x+wp_x_py:
                if  abs((my_y+my_y_py) - (wp_y+wp_y_py)) < 10:
                    向右()
                elif my_y+my_y_py > wp_y+wp_y_py:
                    右上()
                elif my_y+my_y_py < wp_y+wp_y_py:
                    右下()
        if jianqu == '真':
            FinStr = dw.uEKuRfCL(0,78,799,552,"wp.bmp","000000","0.9",0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                捡取()
        if p == 0:
            FinStr = dw.uEKuRfCL(718,25,795,105, "问号绿.bmp|问号黄.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                弹起()
                break
        if p == 1:
            x_g = 检查关卡()
            if x_g != z_g:
                弹起()
                break
        d2 = datetime.datetime.now()
        d3 = d2 - d1
        if d3.seconds > 15:
            Rnd = random.randint(1,4)
            if Rnd == 1:
                向上()
                time.sleep(1)
                弹起()
            elif Rnd == 2:
                向下()
                time.sleep(1)
                弹起()
            elif Rnd == 3:
                向左()
                time.sleep(0.5)
                弹起()
            elif Rnd == 4:
                向右()
                time.sleep(0.5)
                弹起()
            break
def 打石头():
    my_x_py = 10
    my_y_py = 170
    wp_x_py = 12
    wp_y_py = 40
    dst_time = datetime.datetime.now()
    while True:
        time.sleep(0.05)
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        dst_time_now = datetime.datetime.now()
        d3 = dst_time_now - dst_time
        if d3.seconds > 20:
            Rnd = random.randint(1,4)
            if Rnd == 1:
                向上()
                time.sleep(1)
                弹起()
            elif Rnd == 2:
                向下()
                time.sleep(1)
                弹起()
            elif Rnd == 3:
                向左()
                time.sleep(0.5)
                弹起()
            elif Rnd == 4:
                向右()
                time.sleep(0.5)
                弹起()
            break
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "可破坏.bmp", "000000", "0.9", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            wp_x = int(pos[1])
            wp_y = int(pos[2])
        else:
            弹起()
            break
        if my_x > 0 and my_y > 0 and wp_x > 0 and wp_y > 0:
            FinStr = dw.uEKuRfCL(my_x - 80, my_y + 125, my_x + 140, my_y + 200, "可破坏.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                FinStr = dw.uEKuRfCL(530, 561, 562, 593, "鞭子.bmp|双翼风刃.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    xamo.KJDfekiHDh(65,1)
                    time.sleep(0.5)
                else:
                    xamo.KJDfekiHDh(88,1)
                    time.sleep(0.5)
            if abs((my_x + my_x_py) - (wp_x + wp_x_py)) < 10:
                if my_y + my_y_py > wp_y + wp_y_py:
                    向上()
                elif my_y + my_y_py < wp_y + wp_y_py:
                    向下()
            elif my_x + my_x_py > wp_x + wp_x_py:
                if abs((my_y + my_y_py) - (wp_y + wp_y_py)) < 10:
                    向左()
                elif my_y + my_y_py > wp_y + wp_y_py:
                    左上()
                elif my_y + my_y_py < wp_y + wp_y_py:
                    左下()
            elif my_x + my_x_py < wp_x + wp_x_py:
                if abs((my_y + my_y_py) - (wp_y + wp_y_py)) < 10:
                    向右()
                elif my_y + my_y_py > wp_y + wp_y_py:
                    右上()
                elif my_y + my_y_py < wp_y + wp_y_py:
                    右下()
def 技能(leixing):
    if leixing == 1:
        prints('召唤兽唤出')
        temp_name = ['弗利特','桑德尔','牛头王','路易斯','伊伽贝拉','赫德尔','冰','火','光','暗']
        for i in range(len(temp_name)):
            xamo.KJDfekiHDh(jn_key[temp_name[i]],3)
            time.sleep(jn_sf_time[temp_name[i]])
            jn_now_time[temp_name[i]] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        xamo.KJDfekiHDh(40,1)
        xamo.KJDfekiHDh(38,1)
        xamo.KJDfekiHDh(32,1)

    elif leixing == 2:
        temp_name = ['伊伽贝拉','冰','火','光','暗']
        for i in range(len(temp_name)):
            d1 = datetime.datetime.now()
            d2 = datetime.datetime.strptime(jn_now_time[temp_name[i]],'%Y-%m-%d %H:%M:%S')
            d3 = d1 - d2
            if d3.seconds > jn_time[temp_name[i]]:
                xamo.KJDfekiHDh(jn_key[temp_name[i]],3)
                time.sleep(1.2)
                jn_now_time[temp_name[i]] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def 躲避地火(jianqu):
    my_x_py = 10
    my_y_py = 195
    wp_x_py = -100
    wp_y_py = -60
    while True:
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = dw.AIdCpitUAXsF(0, 78, 799, 492, "0000ff-000000", "1", 5)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            wp_x = int(pos[0])
            wp_y = int(pos[1])
            if wp_y < 320:
                wp_y_py = 150
        else:
            弹起()
            break
        if my_x > 0 and my_y > 0 and wp_x > 0 and wp_y > 0:
            if abs((my_x + my_x_py) - (wp_x + wp_x_py)) < 10:
                if my_y + my_y_py > wp_y + wp_y_py:
                    向上()
                elif my_y + my_y_py < wp_y + wp_y_py:
                    向下()
            elif my_x + my_x_py > wp_x + wp_x_py:
                if abs((my_y + my_y_py) - (wp_y + wp_y_py)) < 10:
                    向左()
                elif my_y + my_y_py > wp_y + wp_y_py:
                    左上()
                elif my_y + my_y_py < wp_y + wp_y_py:
                    左下()
            elif my_x + my_x_py < wp_x + wp_x_py:
                if abs((my_y + my_y_py) - (wp_y + wp_y_py)) < 10:
                    向右()
                elif my_y + my_y_py > wp_y + wp_y_py:
                    右上()
                elif my_y + my_y_py < wp_y + wp_y_py:
                    右下()
        if jianqu == '真':
            FinStr = dw.uEKuRfCL(0, 78, 799, 552, "wp.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                捡取()
        FinStr = dw.uEKuRfCL(337, 29, 451, 97, "奖励.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
        FinStr = dw.uEKuRfCL(612, 132, 735, 164, "通关.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
def fanhuichengzhen():
    try:
        while True:
            FinStr = dw.RsJCdWDvHA(451, 427, 535, 501, "返回城镇", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty - 10)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                break
            else:
                xamo.UIKBudj(1, 1)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.KJDfekiHDh(27,1)
                time.sleep(2)
    except:
        print("报错######清空游戏窗口失败")
def 清理游戏窗口():
    xamo.UIKBudj(1, 1)
    time.sleep(0.5)
    xamo.PPWEbxbar(1)
    time.sleep(0.5)
    while True:
        FinStr = dw.RsJCdWDvHA(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(594, 127)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            break
        else:
            xamo.KJDfekiHDh(27,1)
            time.sleep(1)
def 出售分解(ZZ):
    zizhuangshuliang = 0
    FinStr = dw.RsJCdWDvHA(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        intx = int(pos[1])
        inty = int(pos[2])
        xamo.UIKBudj(intx+10, inty + 30)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(2)
        xamo.UIKBudj(intx + 58 + 10, inty + 34 + 30)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        FinStr = dw.RsJCdWDvHA(578, 401, 784, 560, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #装备需要修理自动弹出
            FinStr = dw.RsJCdWDvHA(396, 218, 465, 352, "取消", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 5, inty + 3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            time.sleep(1)
            #点击装备栏
            xamo.UIKBudj(497, 245)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            #点击整理
            xamo.UIKBudj(685, 485)
            time.sleep(0.2)
            xamo.PPWEbxbar(3)
            time.sleep(1)
            #出售
            xamo.UIKBudj(181, 522)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            y = 262
            x_py = 30
            y_py = 30
            no_zhuangbei = False
            for i in range(4):
                x = 474
                for j in range(8):
                    aq_ret = 安全模式()
                    if aq_ret == 1:
                        # 出售
                        xamo.UIKBudj(181, 522)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                    Color = dw.LYqISzEsHWMD(x + 5, y)
                    if Color == '4c9bad':
                        #高级装备
                        zizhuangshuliang += 1
                    elif Color == '656565' or Color == '874747' or Color == '766c79':
                        #普通装备
                        zizhuangshuliang += 1
                    elif Color == 'ab83f7' or Color == 'b85bac':
                        #紫色装备
                        xamo.UIKBudj(x + 14, y + 14)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(2)
                        time.sleep(1)
                    elif Color == 'be00c0':
                        #粉色装备
                        pass
                    elif Color == '3d0642':
                        #不可出售粉色装备
                        pass
                    elif Color == '382c4e':
                        # 不可出售橙色装备
                        pass
                    elif Color == 'ffbb22' or Color == 'f38318':
                        # 可穿戴橙色装备
                        pass
                    elif Color == 'bb00cc':
                        #圣物装备
                        pass
                    else:
                        no_zhuangbei = True
                        break
                    x += x_py
                if no_zhuangbei:
                    break
                y += y_py
            #检查下HP药剂
            FinStr = dw.uEKuRfCL(92, 562, 120, 589, "hp.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                # 点击消耗栏
                xamo.UIKBudj(543, 245)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.UIKBudj(586, 182)
                time.sleep(0.5)
                FinStr = dw.uEKuRfCL(472, 257, 717, 469, "hp.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.5)
                    xamo.XKkncvhe(1)
                    time.sleep(0.5)
                    xamo.cndjGdsbSdg()
                    time.sleep(0.5)
                    xamo.UIKBudj(102, 573)
                    time.sleep(0.5)
                    xamo.mboHdjGsV()
                    time.sleep(0.5)
            清理游戏窗口()
    if zizhuangshuliang == 0:
        return 0
    FinStr = dw.RsJCdWDvHA(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        intx = int(pos[1])
        inty = int(pos[2])
        xamo.UIKBudj(intx + 10, inty + 30)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(1)
        xamo.UIKBudj(intx + 58 + 10, inty + 55 + 30)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        FinStr = dw.RsJCdWDvHA(578, 401, 784, 560, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(255, 350)
            time.sleep(1)
            FinStr = dw.RsJCdWDvHA(323, 370, 335, 382, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                xamo.UIKBudj(323 + 7, 370 + 7)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
            FinStr = dw.RsJCdWDvHA(323, 384, 335, 396, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                xamo.UIKBudj(323 + 7, 384 + 7)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
            xamo.UIKBudj(255, 350)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(2)
            FinStr = dw.RsJCdWDvHA(316, 269, 480, 313, "缺少分解道具", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                清理游戏窗口()
                return 1
            else:
                xamo.KJDfekiHDh(13,1)
                time.sleep(4)
                安全模式()
                清理游戏窗口()
                return 1
def 安全模式():
    FinStr = dw.RsJCdWDvHA(335, 319, 396, 350, "确定解除", "ddc593-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        xgis = get_ini('config/cfg.ini', '小果配置', '小果解安全',"假")
        xguer = get_ini('config/cfg.ini', '小果配置', '小果账号',"")
        xgpwd = get_ini('config/cfg.ini', '小果配置', '小果密码',"")
        prints(account.hao + '|' + account.mi + "出现安全模式，等待解除")
        if xgis == '真':
            prints(account.hao + '|' + account.mi + "出现安全模式，等待解除")
            prints('小果解除安全模式')
            p_qq = get_ini("config/记录.ini", "刷号记录", "当前账号","")
            xaoguo_return = xiaoguo.jiandanjieanquan(p_qq, xguer, xgpwd)
            if xaoguo_return == True:
                prints('小果解除安全模式 成功')
                while True:
                    prints(account.hao + '|' + account.mi + "出现安全模式，等待小果解除")
                    time.sleep(5)
                    FinStr = dw.RsJCdWDvHA(312, 272, 483, 295, "解除安全模式", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        xamo.UIKBudj(400, 307)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        xamo.UIKBudj(442, 332)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        break
            else:
                prints('小果解除安全模式 失败')

        else:
            while True:
                prints(account.hao + '|' + account.mi + "出现安全模式，等待手动解除")
                time.sleep(5)
                FinStr = dw.RsJCdWDvHA(312, 272, 483, 295, "解除安全模式", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    xamo.UIKBudj(400, 307)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    xamo.UIKBudj(442, 332)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    break
        return 1
    return 0
def 移动():
    prints('移动')
    index = 0
    yd_time = datetime.datetime.now()
    while True:
        yd_time_now = datetime.datetime.now()
        d3 = yd_time_now - yd_time
        if d3.seconds > 100:
            弹起()
            return 1
        time.sleep(0.2)
        if index == 0:
            向下()
            FinStr = dw.RsJCdWDvHA(652, 26, 743, 52, "斯曼工业基地", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                向右()
                time.sleep(1)
                弹起()
                向上()
                time.sleep(1)
                弹起()
                index = 1
            FinStr = dw.RsJCdWDvHA(652, 26, 743, 52, "克洛诺斯岛", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                time.sleep(1)
                弹起()
                index = 2.1
        elif index == 1:
            右上()
            FinStr = dw.RsJCdWDvHA(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                break
        elif index == 2.1:
            左上()
            FinStr = dw.RsJCdWDvHA(660, 26, 743, 52, "斯曼工业基地", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                向下()
                time.sleep(1)
                弹起()
                index = 2.2
        elif index == 2.2:
            左上()
            FinStr = dw.uEKuRfCL(0, 16, 521, 234, "地图中转.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                index = 2.3
        elif index == 2.3:
            向右()
            FinStr = dw.RsJCdWDvHA(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                break
    return 0
def 点击技能(x, y, x1, y1,is_tuodong):
    #学满技能
    xamo.UIKBudj(x, y)
    time.sleep(0.5)
    xamo.PPWEbxbar(1)
    time.sleep(0.5)
    xamo.LKDFemrrh(16)
    time.sleep(0.5)
    xamo.PPWEbxbar(1)
    time.sleep(0.5)
    xamo.LJDFnmeFSD(16)
    time.sleep(1)
    if is_tuodong == True:
    #拖动技能
        xamo.UIKBudj(x + 3, y + 3)
        time.sleep(0.5)
        xamo.cndjGdsbSdg()
        time.sleep(0.5)
        xamo.UIKBudj(x + 5, y + 5)
        time.sleep(0.5)
        xamo.UIKBudj(x1, y1)
        time.sleep(0.5)
        xamo.UIKBudj(x1+3, y1+3)
        time.sleep(0.5)
        xamo.mboHdjGsV()
        time.sleep(0.5)
def 学习技能(zhiye):
    prints('学习技能')
    for t in range(3):
        is_wz = True
        if zhiye == 2: #风法
            #检查技能摆放
            for i in range(9):
                FinStr = dw.uEKuRfCL(528, 523, 715, 593, "风法技能" + str(i + 1) + ".bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    pass
                else:
                    is_wz = False
                    break
            if is_wz == False:
                while True:
                    FinStr = dw.RsJCdWDvHA(376, 28, 429, 51, "技能栏", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        time.sleep(1)
                        #关闭学习技能帮助界面
                        FinStr = dw.RsJCdWDvHA(24, 132, 89, 164, "学习技能", "ffee88-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            xamo.UIKBudj(519, 295)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        for it in range(10):
                            xamo.UIKBudj(547, 196)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        time.sleep(1)
                        #物理暴击
                        点击技能(224, 141, 0, 0, False)
                        #物理背击
                        点击技能(304, 141, 0, 0, False)
                        #流风决
                        点击技能(285, 475, 0, 0, False)
                        #棍棒精通
                        点击技能(426, 410, 0, 0, False)
                        for t in range(5):
                            xamo.UIKBudj(547, 517)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        #凤鸣冲击
                        点击技能(239, 209, 672, 571, True)
                        #游离之风
                        点击技能(332, 210, 638, 571, True)
                        #双翼风刃
                        点击技能(333, 277, 605, 571, True)
                        #风暴之眼
                        点击技能(333, 343, 605, 536, True)
                        #真空旋风破
                        点击技能(287, 410, 705, 571, True)
                        #风暴之拳
                        点击技能(191, 477, 738, 571, True)
                        for t in range(7):
                            xamo.UIKBudj(547, 517)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        #万象风龙阵
                        点击技能(239, 274, 736, 536, True)
                        #御风之力
                        点击技能(331, 274, 0, 0, False)
                        #风神决
                        点击技能(191, 411, 0, 0, False)
                        #风卷残云
                        点击技能(285, 411, 672, 536, True)
                        #游龙惊风破
                        点击技能(333, 411, 640, 539, True)
                        #九霄风雷
                        点击技能(191, 476, 704, 536, True)
                        #无限风域
                        点击技能(379, 476, 771, 536, True)
                        time.sleep(1)
                        #学习
                        xamo.UIKBudj(209, 553)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        #确认
                        xamo.KJDfekiHDh(13,1)
                        time.sleep(1)
                        清理游戏窗口()
                        break
                    else:
                        xamo.KJDfekiHDh(75,1)
                        time.sleep(1)
        elif zhiye == 1: #召唤
            #检查技能摆放
            for i in range(12):
                FinStr = dw.uEKuRfCL(528, 523, 715, 593, "召唤技能" + str(i + 1) + ".bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    pass
                else:
                    is_wz = False
                    break
            if is_wz == False:
                while True:
                    FinStr = dw.RsJCdWDvHA(376, 28, 429, 51, "技能栏", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        time.sleep(1)
                        #关闭学习技能帮助界面
                        FinStr = dw.RsJCdWDvHA(24, 132, 89, 164, "学习技能", "ffee88-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            xamo.UIKBudj(519, 295)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        for it in range(10):
                            xamo.UIKBudj(547, 196)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        time.sleep(1)
                        #魔法暴击
                        点击技能(265, 141, 0, 0, False)
                        #魔法背击
                        点击技能(346, 141, 0, 0, False)
                        #赫德尔
                        点击技能(424, 273, 638, 571, True)
                        #弗利特
                        点击技能(424, 476, 605, 539, True)
                        #鞭子
                        点击技能(238, 338, 605, 571, True)
                        for t in range(5):
                            xamo.UIKBudj(547, 517)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        #桑德尔
                        点击技能(426, 209, 638, 536, True)
                        #狂化
                        点击技能(379, 274, 769, 536, True)
                        #冰
                        点击技能(49, 274, 670, 571, True)
                        #火
                        点击技能(97, 274, 703, 571, True)
                        #光
                        点击技能(143, 274, 737, 571, True)
                        #暗
                        点击技能(191, 274, 770, 571, True)
                        #路易斯
                        点击技能(426, 341, 704, 536, True)
                        #伊伽贝拉
                        点击技能(285, 411, 737, 539, True)
                        #牛王
                        点击技能(427, 475, 671, 539, True)
                        time.sleep(1)
                        #学习
                        xamo.UIKBudj(209, 553)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        #确认
                        xamo.KJDfekiHDh(13,1)
                        time.sleep(1)
                        清理游戏窗口()
                        break
                    else:
                        xamo.KJDfekiHDh(75,1)
                        time.sleep(1)
def 检查负重():
    for i in range(10):
        FinStr = dw.RsJCdWDvHA(430, 366, 588, 586, "重量", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(0.5)
            intx = int(pos[1])
            inty = int(pos[2])
            color = dw.LYqISzEsHWMD(intx + 95, inty + 8)
            prints(color)
            if color == 'd62929':
                return 1
            elif color == '202020':
                return 0
            else:
                return 1
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(1)
    return 0
def 检查累积在线奖励():
    FinStr = dw.RsJCdWDvHA(148,11, 418, 72, "累积在线得好礼", "ffc800-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        intx = int(pos[1])
        inty = int(pos[2])
        xamo.UIKBudj(intx + 23, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.5)
        xamo.UIKBudj(intx + 74, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.5)
        xamo.UIKBudj(intx + 126, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.5)
        xamo.UIKBudj(intx + 179, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.5)
def 购买物品(name,num):
    gmwp_time = datetime.datetime.now()
    while True:
        FinStr = dw.RsJCdWDvHA(609, 75, 669, 110, "默认设置", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(1)
            intx = int(pos[1])
            inty = int(pos[2])
            #默认设置
            xamo.UIKBudj(intx + 10, inty + 3)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            #点击输入框
            xamo.UIKBudj(144, 92)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            hwnd = dw.bcGT("地下城与勇士", "地下城与勇士")
            if hwnd > 0:
                dw.gshNarIzNfhm(hwnd, name)
            time.sleep(1)
            #搜索
            xamo.UIKBudj(589, 89)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)


        else:
            #按B打开拍卖行
            xamo.KJDfekiHDh(66,1)
            time.sleep(1)
def 购买免修():
    prints('检查自动修理')
    清理游戏窗口()
    gmmx_time = datetime.datetime.now()
    while True:
        FinStr = dw.uEKuRfCL(0, 0, 800, 600, "服务列表.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 5)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        else:
            break
        FinStr = dw.RsJCdWDvHA(0, 0, 800, 600, "优惠券礼盒", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.RsJCdWDvHA(0, 0, 800, 600, "自动修理", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 1
            else:
                break
        gmmx_time_now = datetime.datetime.now()
        d3 = gmmx_time_now - gmmx_time
        if d3.seconds > 100:
            return 0
    prints('购买自动修理')
    while True:
        FinStr = dw.RsJCdWDvHA(92, 540, 171, 579, "积分", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            number = dw.ghKWigkPfdBCtSd(325, 547, 410, 570, "ffffff-000000", 1)
            number = re.sub("\D", "", number)
            if int(number) > 500:
                break
            else:
                prints('点券不够购买免修服务请充值')
                time.sleep(5)
                #刷新点券
                xamo.UIKBudj(400, 557)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
        else:
            xamo.UIKBudj(481, 577)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            gmmx_time_now = datetime.datetime.now()
            d3 = gmmx_time_now - gmmx_time
            if d3.seconds > 100:
                return 0

    gmmx_time = datetime.datetime.now()
    while True:
        time.sleep(0.2)
        gmmx_time_now = datetime.datetime.now()
        d3 = gmmx_time_now - gmmx_time
        if d3.seconds > 100:
            return 0
        FinStr = dw.RsJCdWDvHA(575, 45, 631, 79, "装饰类", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #点击优惠类
            xamo.UIKBudj(520, 58)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            for tn in range(3):
                FinStr = dw.RsJCdWDvHA(17, 107, 419, 527, "魔王之契约", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx + 34, inty + 76)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                else:
                    xamo.UIKBudj(403, 98)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
        else:
            #点击道具类
            xamo.UIKBudj(414, 23)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.RsJCdWDvHA(370, 98, 431, 122, "结算窗口", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #点击下拉
            xamo.UIKBudj(428, 201)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            #选择30天
            xamo.UIKBudj(384, 235)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            #购买
            xamo.UIKBudj(503, 476)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(2)
            xamo.KJDfekiHDh(13,1)
            清理游戏窗口()
            break
def boss关捡取():
    xamo.KJDfekiHDh(86,1)
    time.sleep(1)
    for ic in range(10):
        xamo.KJDfekiHDh(88,1)
        time.sleep(0.2)
def 打怪_风法():
    my_x_py = 10
    my_y_py = 170
    gw_x_py = 28
    gw_y_py = 30
    jl_x = 230
    jl_y = 60
    while True:
        my_x = 0
        my_y = 0
        gw_x = 0
        gw_y = 0
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "my.bmp", "000000", "1", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        else:
            Rnd = random.randint(1, 4)
            if Rnd == 1:
                向上()
                time.sleep(1)
                弹起()
            elif Rnd == 2:
                向下()
                time.sleep(1)
                弹起()
            elif Rnd == 3:
                向左()
                time.sleep(0.5)
                弹起()
            elif Rnd == 4:
                向右()
                time.sleep(0.5)
                弹起()
        FinStr = dw.AIdCpitUAXsF(0, 78, 799, 552, "ff0094-101010|ff00ff-101010", 1.0, 0)
        pos = FinStr.split('|')
        if int(pos[0]) > 0:
            gw_x = int(pos[0])
            gw_y = int(pos[1])
        else:
            弹起()
            break
        if my_x > 0 and my_y > 0 and gw_x > 0 and gw_y > 0:
            if  abs((my_x + my_x_py) - (gw_x + gw_x_py)) < jl_x:
                if abs((my_y + my_y_py) - (gw_y + gw_y_py)) < jl_y:
                    弹起()
                    if my_x + my_x_py > gw_x + gw_x_py:
                        #转向左边
                        xamo.KJDfekiHDh(37, 1)
                        time.sleep(0.1)
                    elif my_x + my_x_py < gw_x + gw_x_py:
                        #转向右边
                        xamo.KJDfekiHDh(39, 1)
                        time.sleep(0.1)
                    FinStr = dw.uEKuRfCL(531, 561, 715, 596, "双翼风刃.bmp|游离之风.bmp|凤鸣冲击.bmp|真空旋风破.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        if int(pos[0]) == 0:
                            xamo.KJDfekiHDh(65, 1)
                            time.sleep(0.5)
                        elif int(pos[0]) == 1:
                            xamo.KJDfekiHDh(83, 1)
                            time.sleep(0.5)
                        elif int(pos[0]) == 2:
                            xamo.KJDfekiHDh(68, 1)
                            time.sleep(0.8)
                        elif int(pos[0]) == 3:
                            xamo.KJDfekiHDh(70, 1)
                            time.sleep(0.6)
                    else:
                        xamo.KJDfekiHDh(88, 3)
                        time.sleep(0.5)
            if abs((my_x + my_x_py) - (gw_x + gw_x_py)) < jl_x:
                if my_y + my_y_py > gw_y + gw_y_py:
                    向上()
                elif my_y + my_y_py < gw_y + gw_y_py:
                    向下()
            elif my_x + my_x_py > gw_x + gw_x_py:
                if abs((my_y + my_y_py) - (gw_y + gw_y_py)) < jl_y:
                    向左()
                elif my_y + my_y_py > gw_y + gw_y_py:
                    左上()
                elif my_y + my_y_py < gw_y + gw_y_py:
                    左下()
            elif my_x + my_x_py < gw_x + gw_x_py:
                if abs((my_y + my_y_py) - (gw_y + gw_y_py)) < jl_y:
                    向右()
                elif my_y + my_y_py > gw_y + gw_y_py:
                    右上()
                elif my_y + my_y_py < gw_y + gw_y_py:
                    右下()
        time.sleep(0.02)
def 图内_风法():
    xingwei = True
    guanqia = 0
    duobidihuo = False
    Imok = True
    time_is = True
    while_time = datetime.datetime.now()
    # 游戏内循环执行
    prints('进入副本')
    while True:
        time.sleep(0.05)
        if zhongduan_cha() == 1:
            Imok = False
            break
        if guanqia == 0:
            guanqia = 检查关卡()
        if xingwei:
            # 关卡7再次检查确认
            # 如果还能在小地图找到人物，证明走错了关卡，就按关卡检查的返回
            if guanqia == 7:
                guanqia_temp = 检查关卡()
                if guanqia_temp > 0:
                    guanqia = guanqia_temp
            prints('关卡 = ' + str(guanqia))
            if guanqia > 0:
                if guanqia == 4:
                    xamo.KJDfekiHDh(37, 1)
                elif guanqia == 5:
                    xamo.KJDfekiHDh(39, 1)
                if guanqia > 1:
                    xamo.KJDfekiHDh(65, 1)
                    time.sleep(0.8)
                xingwei = False
            if guanqia == 1:
                技能(1)
                time.sleep(1)
                xamo.KJDfekiHDh(65, 1)
                time.sleep(0.8)
                xamo.KJDfekiHDh(89, 1)
                time.sleep(1)
                FinStr = dw.uEKuRfCL(14, 129, 124, 181, "DPS.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    myX = int(pos[1])
                    myY = int(pos[2]) + 10
                    xamo.UIKBudj(myX + 5, myY + 5)
                    time.sleep(0.2)
                    xamo.cndjGdsbSdg()
                    time.sleep(0.5)
                    for i in range(myY - 20):
                        xamo.UIKBudj(myX + 5, myY - i)
                        time.sleep(0.005)
                    time.sleep(0.5)
                    xamo.mboHdjGsV()
                    time.sleep(0.5)
            elif guanqia == 2:
                pass
            elif guanqia == 3:
                向右()
                time.sleep(2)
                弹起()
            elif guanqia == 4:
                pass
            elif guanqia == 5:
                xamo.KJDfekiHDh(89, 1)
                time.sleep(1)
                向下()
                time.sleep(3)
                弹起()
            elif guanqia == 6:
                技能(2)
                右下()
                time.sleep(2)
                弹起()
            elif guanqia == 7:
                技能(2)
                xamo.KJDfekiHDh(89, 1)
                time.sleep(1)
                duobidihuo = True
        FinStr = dw.uEKuRfCL(718, 25, 795, 105, "问号绿.bmp|问号黄.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            找门(guanqia, 0)
            time.sleep(1)
            xingwei = True
            guanqia = 0
            continue
        # 走到错误的关卡,Boss前一关按照走错处理
        FinStr = dw.uEKuRfCL(718, 25, 795, 105, "错关.bmp|错关1.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            找门(guanqia, 1)
            time.sleep(1)
            xingwei = True
            if guanqia == 6:
                guanqia += 1
            else:
                guanqia = 0
            continue
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "可破坏.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            打石头()
        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "wp.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            捡取()
        FinStr = dw.uEKuRfCL(612, 132, 735, 164, "通关.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            duobidihuo = False
            弹起()
            捡取()
            弹起()
            清理游戏窗口()
            color = dw.LYqISzEsHWMD(339, 553)
            if color == "0b0b0b" or color == "333333":
                print('返回城镇')
                fanhuichengzhen()
                time.sleep(3)
                break
            else:
                fz_ret = 检查负重()
                if fz_ret == 1:
                    fanhuichengzhen()
                    time.sleep(3)
                    break
                else:
                    xamo.KJDfekiHDh(121, 1)
                    time.sleep(1)
                    xamo.KJDfekiHDh(121, 1)
                    time.sleep(1)
                    xamo.KJDfekiHDh(121, 1)
                    time.sleep(5)
                    break
        FinStr = dw.RsJCdWDvHA(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            break
        # 图内超时判断
        FinStr = dw.RsJCdWDvHA(333, 571, 473, 597, "只能城镇交易", "ffff00-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time_is = True
            while_time = datetime.datetime.now()
        if time_is == True:
            while_time_now = datetime.datetime.now()
            time_temp = while_time_now.minute - while_time.minute
            if time_temp > 6:
                prints("图内超时，重上")
                end_exsit(2)
                time.sleep(2)
                Imok = False
                break
    return Imok
def 设置():
    prints('设置')
    sz_time = datetime.datetime.now()
    while True:
        sz_time_now = datetime.datetime.now()
        d3 = sz_time_now - sz_time
        if d3.seconds > 100:
            弹起()
            return 0
        FinStr = dw.RsJCdWDvHA(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(279, 442)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            break
        else:
            xamo.KJDfekiHDh(27,1)
            time.sleep(1)
    while True:
        sz_time_now = datetime.datetime.now()
        d3 = sz_time_now - sz_time
        if d3.seconds > 100:
            弹起()
            return 0
        FinStr = dw.RsJCdWDvHA(163, 421, 260, 478, "快捷键设置", "ddcc99-000000|ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 10, inty + 3)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.RsJCdWDvHA(328, 296, 418, 346, "聊天快捷键", "96ff1e-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 10, inty + 3)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            #点击输入框
            xamo.UIKBudj(189, 362)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            xamo.KJDfekiHDh(8,10)
            hwnd = dw.bcGT("地下城与勇士", "地下城与勇士")
            if hwnd > 0:
                dw.gshNarIzNfhm(hwnd, '//移动物品')
            #点击输入框
            xamo.UIKBudj(327, 362)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            xamo.KJDfekiHDh(86, 1)
            #点击保存
            xamo.UIKBudj(569, 513)
            time.sleep(0.2)
            xamo.PPWEbxbar(3)
            time.sleep(1)
            清理游戏窗口()
            return 1
def 购买礼盒():
    gmlh_time = datetime.datetime.now()
    while True:
        FinStr = dw.RsJCdWDvHA(92, 540, 171, 579, "积分", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            number = dw.ghKWigkPfdBCtSd(325, 547, 410, 570, "ffffff-000000", 1)
            number = re.sub("\D", "", number)
            if int(number) >= 520:
                break
            else:
                prints("点券不够，再充值" + str(520-int(number)) + "点")
                time.sleep(5)
                # 刷新点券
                xamo.UIKBudj(400, 557)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
        else:
            xamo.UIKBudj(481, 577)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            gmlh_time_now = datetime.datetime.now()
            d3 = gmlh_time_now - gmlh_time
            if d3.seconds > 300:
                return 0
    while True:
        FinStr = dw.RsJCdWDvHA(575, 45, 631, 79, "装饰类", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            # 点击道具
            xamo.UIKBudj(281, 58)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            FinStr = dw.RsJCdWDvHA(21, 110, 423, 225, "浪漫之约礼包", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 46, inty + 76)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            else:
                xamo.UIKBudj(281, 58)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
        else:
            # 点击道具大类
            xamo.UIKBudj(414, 23)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.RsJCdWDvHA(353, 88, 443, 133, "结算窗口", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #购买
            xamo.UIKBudj(503, 476)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(2)
            xamo.KJDfekiHDh(13,1)
            return 1
def 打开礼盒():
    while True:
        FinStr = dw.RsJCdWDvHA(578, 401, 784, 560, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx - 131, inty - 233)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            FinStr = dw.uEKuRfCL(452, 198, 737, 465, "浪漫之约礼包.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx +5, inty + 5)
                time.sleep(0.2)
                xamo.XKkncvhe(3)
                time.sleep(1)
                return  1
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(2)
def 检查礼盒():
    while True:
        FinStr = dw.RsJCdWDvHA(578, 401, 784, 560, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx - 131, inty - 233)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            FinStr = dw.uEKuRfCL(452, 198, 737, 465, "浪漫心动礼盒.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 1
            return 0
        else:
            xamo.KJDfekiHDh(73, 1)
            time.sleep(2)
def 上架礼盒():
    sjlh_time = datetime.datetime.now()
    while True:
        FinStr = dw.RsJCdWDvHA(609, 75, 669, 110, "默认设置", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(1)
            xamo.UIKBudj(76, 547)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            break
        else:
            # 按B打开拍卖行
            xamo.KJDfekiHDh(66, 1)
            time.sleep(1)
        sjlh_time_now = datetime.datetime.now()
        d3 = sjlh_time_now - sjlh_time
        if d3.seconds > 100:
            return 0
    sjlh_time = datetime.datetime.now()
    while True:
        FinStr = dw.RsJCdWDvHA(215, 448, 267, 473, "竞拍价", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #点击消耗栏
            xamo.UIKBudj(543, 246)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            FinStr = dw.uEKuRfCL(466, 252, 721, 420, "浪漫心动礼盒.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                x = int(pos[1])
                y = int(pos[2])
                x1 = 228
                y1 = 285
                xamo.UIKBudj(x + 3, y + 3)
                time.sleep(0.5)
                xamo.cndjGdsbSdg()
                time.sleep(0.5)
                xamo.UIKBudj(x + 5, y + 5)
                time.sleep(0.5)
                xamo.UIKBudj(x1, y1)
                time.sleep(0.5)
                xamo.UIKBudj(x1 + 3, y1 + 3)
                time.sleep(0.5)
                xamo.mboHdjGsV()
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.UIKBudj(x1 - 30, y1 - 30)
                time.sleep(1)

                break
        else:
            xamo.UIKBudj(76, 547)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        sjlh_time_now = datetime.datetime.now()
        d3 = sjlh_time_now - sjlh_time
        if d3.seconds > 200:
            return 0

    sjlh_time = datetime.datetime.now()
    while True:
        sjlh_time_now = datetime.datetime.now()
        d3 = sjlh_time_now - sjlh_time
        if d3.seconds > 200:
            return 0
        FinStr = dw.RsJCdWDvHA(317, 328, 356, 425, "每个", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            number = dw.ghKWigkPfdBCtSd(314, 376, 441, 393, "ddc593-000000", 1)
            number = re.sub("\D", "", number)
            #一口价
            xamo.UIKBudj(417, 480)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            xamo.KJDfekiHDh(8, 10)
            xamo.LbferJhd(number)
            time.sleep(1)
            xamo.KJDfekiHDh(13, 1)
            time.sleep(4)
            aq_ret = 安全模式()
            if aq_ret == 1:
                return 3
            return 1
def 关卡构造(zhiye,guanqia):
    duobidihuo = False
    if zhiye == 1:
        if guanqia == 4:
            xamo.KJDfekiHDh(37, 1)
        elif guanqia == 5:
            xamo.KJDfekiHDh(39, 1)
        if guanqia > 1:
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.8)
    if guanqia == 1:
        if zhiye == 1:
            技能(1)
            time.sleep(1)
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.8)
            xamo.KJDfekiHDh(89, 1)
            time.sleep(1)
        elif zhiye == 2:
            # 流风决 右 右 空格
            xamo.KJDfekiHDh(39, 1)
            time.sleep(0.05)
            xamo.KJDfekiHDh(39, 1)
            time.sleep(0.05)
            xamo.KJDfekiHDh(32, 1)
            time.sleep(0.5)
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 1)
            time.sleep(0.5)
            # 双翼风刃 A
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.2)
            # 游离之风 S
            xamo.KJDfekiHDh(83, 1)
            time.sleep(0.2)
        FinStr = dw.uEKuRfCL(14, 129, 124, 181, "DPS.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            myX = int(pos[1])
            myY = int(pos[2]) + 10
            xamo.UIKBudj(myX + 5, myY + 5)
            time.sleep(0.2)
            xamo.cndjGdsbSdg()
            time.sleep(0.5)
            for i in range(myY - 20):
                xamo.UIKBudj(myX + 5, myY - i)
                time.sleep(0.005)
            time.sleep(0.5)
            xamo.mboHdjGsV()
            time.sleep(0.5)
    elif guanqia == 2:
        if zhiye == 2:
            向右()
            time.sleep(0.5)
            弹起()
            # 游龙惊风破 W
            xamo.KJDfekiHDh(87, 1)
            time.sleep(1.5)
            # 游离之风 S
            xamo.KJDfekiHDh(83, 1)
            time.sleep(0.5)
    elif guanqia == 3:
        if zhiye == 1:
            向右()
            time.sleep(2)
            弹起()
        elif zhiye == 2:
            向右()
            time.sleep(0.6)
            弹起()
            # 风卷残云 E
            xamo.KJDfekiHDh(69, 1)
            time.sleep(1)
    elif guanqia == 4:
        if zhiye == 2:
            #点击左
            xamo.KJDfekiHDh(37, 1)
            time.sleep(0.1)
            FinStr = dw.uEKuRfCL(531, 561, 715, 596, "双翼风刃.bmp|游离之风.bmp|凤鸣冲击.bmp|真空旋风破.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if int(pos[0]) == 0:
                    xamo.KJDfekiHDh(65, 1)
                    time.sleep(0.5)
                elif int(pos[0]) == 1:
                    xamo.KJDfekiHDh(83, 1)
                    time.sleep(0.5)
                elif int(pos[0]) == 2:
                    xamo.KJDfekiHDh(68, 1)
                    time.sleep(0.8)
                elif int(pos[0]) == 3:
                    xamo.KJDfekiHDh(70, 1)
                    time.sleep(0.6)
            向下()
            time.sleep(0.7)
            弹起()
            # 左转
            xamo.KJDfekiHDh(37, 1)
            time.sleep(0.5)
            # 九霄风雷 R
            xamo.KJDfekiHDh(82, 1)
            time.sleep(1.8)
    elif guanqia == 5:
        if zhiye == 1:
            xamo.KJDfekiHDh(89, 1)
            time.sleep(1)
            向下()
            time.sleep(3)
            弹起()
        elif zhiye == 2:
            #点击右
            xamo.KJDfekiHDh(39, 1)
            time.sleep(0.1)
            FinStr = dw.uEKuRfCL(531, 561, 715, 596, "双翼风刃.bmp|游离之风.bmp|凤鸣冲击.bmp|真空旋风破.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if int(pos[0]) == 0:
                    xamo.KJDfekiHDh(65, 1)
                    time.sleep(0.5)
                elif int(pos[0]) == 1:
                    xamo.KJDfekiHDh(83, 1)
                    time.sleep(0.5)
                elif int(pos[0]) == 2:
                    xamo.KJDfekiHDh(68, 1)
                    time.sleep(0.8)
                elif int(pos[0]) == 3:
                    xamo.KJDfekiHDh(70, 1)
                    time.sleep(0.6)
            左下()
            time.sleep(0.4)
            弹起()
            # 万象风龙阵 T
            xamo.KJDfekiHDh(84, 1)
            time.sleep(3)
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 1)
            time.sleep(0.5)
            向下()
            time.sleep(1.5)
            弹起()
    elif guanqia == 6:
        if zhiye == 1:
            技能(2)
            右下()
            time.sleep(2)
            弹起()
        elif zhiye == 2:
            向右()
            time.sleep(0.6)
            弹起()
            # 无限风域 Y
            xamo.KJDfekiHDh(89, 1)
            time.sleep(5)
    elif guanqia == 7:
        if zhiye == 1:
            技能(2)
            xamo.KJDfekiHDh(89, 1)
            time.sleep(1)
            duobidihuo = True
        elif zhiye == 2:
            右上()
            time.sleep(0.4)
            向右()
            time.sleep(0.1)
            弹起()
            # 风暴之拳 G
            xamo.KJDfekiHDh(71, 1)
            time.sleep(1.3)
            # 游龙惊风破 W
            xamo.KJDfekiHDh(87, 2)
            time.sleep(1.6)
            # 风卷残云 E
            xamo.KJDfekiHDh(69, 1)
            time.sleep(0.6)
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 1)
            time.sleep(0.6)
            # 双翼风刃 A
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.5)
            # 游离之风 S
            xamo.KJDfekiHDh(83, 1)
            time.sleep(0.5)
    return duobidihuo
def while_():
    # 读取配置文档
    WeGame = get_ini('config/cfg.ini', '主配置', 'WeGame',"")
    number = get_ini('config/cfg.ini', '主配置', '账号路径',"")
    CRuser = get_ini('config/cfg.ini', '主配置', '若快账号',"")
    CRpwd = get_ini('config/cfg.ini', '主配置', '若快密码',"")
    zhuanqian = get_ini('config/cfg.ini', '主配置', '只转钱',"假")
    duihuandianquan = get_ini('config/cfg.ini', '主配置', '兑换点券',"假")
    jianqu = get_ini('config/cfg.ini', '主配置', '捡取',"假")
    x = dw.yTKUBaTqevaYZRU()
    y = dw.vgtwHdrCtErzwk()
    # 职业1 = 召唤：2 = 风法
    zhiye = 0
    prints('捡取 = ' + str(jianqu))
    # 进入正题
    while True:
        is_60m = False
        saotubiao()
        shuaxinliebiao()
        # 游戏内执行一次
        if check_exsit("DNF.exe") == 0:
            # 结束全部进程
            end_exsit(2)
            # 登录成功返回窗口句柄
            login_ret = login(CRuser, CRpwd, number, WeGame, zhuanqian)
            prints('登录成功')
            if login_ret == 0:
                prints("连接频道失败，重上")
                end_exsit(2)
                time.sleep(2)
                continue
            elif login_ret == 3:
                prints("登录超时，重上")
                end_exsit(2)
                time.sleep(2)
                continue
            elif login_ret == 101:
                continue
            time.sleep(3)
            is_60m = True
        hwnd = dw.bcGT("地下城与勇士", "地下城与勇士")
        if hwnd > 0:
            dw.pkSC(hwnd, 0, 0)
            time.sleep(5)
            Imok = True
            while True:
                time.sleep(0.5)
                FinStr = dw.RsJCdWDvHA(0, 0, x, y, "结束游戏", "ddc593-050505|ffffb8-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    time.sleep(5)
                    fenghao_return = fenghaojianhcha()
                    if fenghao_return == 'F5':
                        prints("账号停封5天，换号")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    elif fenghao_return == 'F7':
                        prints("账号停封7天，换号")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    elif fenghao_return == 'F0':
                        prints('只是中断没有封号，重上')
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    elif fenghao_return == 'F100':
                        prints("永久封号，换号")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    elif fenghao_return == 'F101':
                        prints("此ID已在游戏中，重上")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    # 选择角色
                    juesechuli_ret = juesechuli(1)
                    if juesechuli_ret == 0:
                        prints("角色刷完，换号")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    elif juesechuli_ret == 1:
                        prints("角色更换完成")
                    elif juesechuli_ret == 2:
                        prints("网络连接中断，重上")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    elif juesechuli_ret == 3:
                        prints("角色处理超时，重上")
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                        break
                    time.sleep(5)
                    # 刷新列表
                    shuaxinliebiao()
                FinStr = dw.RsJCdWDvHA(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    if jinqizhicai() == 1:
                        Imok = False
                        break
                    time.sleep(3)
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx + 5, inty + 3)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    qingkongyouxichuangkou()
                FinStr = dw.uEKuRfCL(365, 356, 418, 384, "签到.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    if jinqizhicai() == 1:
                        Imok = False
                        break
                    time.sleep(1)
                    qingkongyouxichuangkou()
                FinStr = dw.uEKuRfCL(114, 59, 739, 306, "叉.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    if jinqizhicai() == 1:
                        Imok = False
                        break
                    time.sleep(1)
                    qingkongyouxichuangkou()
                FinStr = dw.RsJCdWDvHA(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    if jinqizhicai() == 1:
                        Imok = False
                        break
                    if is_60m == True:
                        # 职业1 = 召唤：2 = 风法
                        zhiye = 2
                        # 关闭直播视频进程
                        run('taskkill /F /IM CrossProxy.exe', shell=True)
                        prints("等待60秒...")
                        time.sleep(40)
                        # 只兑换点券
                        if zhuanqian == '真':
                            # jieshouyoujian()
                            # 清理游戏窗口()
                            # if 检查礼盒() == 0:
                            #     清理游戏窗口()
                            #     购买礼盒()
                            #     清理游戏窗口()
                            #     jieshouyoujian()
                            #     清理游戏窗口()
                            #     打开礼盒()
                            # 清理游戏窗口()
                            # xm_ret = 上架礼盒()
                            # if xm_ret == 3:
                            #     清理游戏窗口()
                            #     上架礼盒()
                            # 清理游戏窗口()
                            # while True:
                            #     FinStr = dw.uEKuRfCL(263, 462, 533, 551, "邮件.bmp|邮件1.bmp", "202020", "0.9", 0)
                            #     pos = FinStr.split('|')
                            #     if int(pos[1]) > 0:
                            #         jieshouyoujian()
                            #         清理游戏窗口()
                            #         break
                            #     else:
                            #         prints("等待接收金币")
                            #         time.sleep(2)
                            chushoudianquan()
                            清理游戏窗口()
                            jieshouyoujian()
                            清理游戏窗口()
                            fyj_return = fayoujian(CRuser, CRpwd)
                            if fyj_return == 1:
                                # 正常返回
                                pass
                            elif fyj_return == 2:
                                prints('网络连接中断,重上')
                                end_exsit(2)
                                time.sleep(2)
                                Imok = False
                                break
                            elif fyj_return == 3:
                                prints('发送邮件超时,重上')
                                end_exsit(2)
                                time.sleep(2)
                                Imok = False
                                break
                            prints("礼盒处理完成，换号")
                            jiluwanchengshijian_zhuanqian()
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                        检查累积在线奖励()
                        #设置
                        shezhi = get_ini('config/设置.ini', '设置', account.hao + '_' + account.daqu,"假")
                        if shezhi != '真':
                            sz_ret = 设置()
                            if sz_ret == 1:
                                set_ini('config/设置.ini','设置',account.hao + '_' + account.daqu,'真')
                                prints('快捷键设置成功')
                            else:
                                prints('快捷键设置失败')
                        #yongbingchuzhan()
                    购买免修()
                    qingkongyouxichuangkou()
                    if duihuandianquan == "真":
                        csdq_ret = chushoudianquan()
                        qingkongyouxichuangkou()
                        if csdq_ret > 0:
                            jieshouyoujian()
                            qingkongyouxichuangkou()
                    # 学习技能
                    学习技能(zhiye)
                    # 移动到副本门口
                    yd_ret = 移动()
                    if yd_ret == 1:
                        prints('移动位置超时')
                        end_exsit(2)
                        time.sleep(2)
                        Imok = False
                    break
            if Imok == False:
                continue
            # 初始化参数
            maoxiandengji = 5
            Imok = True
            while True:
                while True:
                    print('等待曼斯工业基地')
                    time.sleep(0.05)
                    FinStr = dw.RsJCdWDvHA(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        qingkongyouxichuangkou()
                    if zhongduan_cha() == 1:
                        Imok = False
                        break
                    # 疲劳刷完了
                    color = dw.LYqISzEsHWMD(339, 553)
                    if color == "0b0b0b" or color == "333333":
                        time.sleep(1)
                        FinStr = dw.RsJCdWDvHA(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            break
                        prints('打印任务完成')
                        出售分解(1)
                        jieshouyoujian()
                        # 发送邮件
                        fyj_return = fayoujian(CRuser, CRpwd)
                        if fyj_return == 1:
                            # 正常返回
                            pass
                        elif fyj_return == 2:
                            prints('网络连接中断,重上')
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                        elif fyj_return == 3:
                            prints('发送邮件超时,重上')
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                        # 记录完成时间
                        jiluwanchengshijian()
                        # 换角色
                        prints("PL刷完，换角色")
                        juesechuli_ret = juesechuli(2)
                        if juesechuli_ret == 0:
                            prints("角色刷完，换号")
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                        if juesechuli_ret == 1:
                            # 正常返回
                            pass
                        elif juesechuli_ret == 2:
                            prints("网络连接中断，重上")
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                        elif juesechuli_ret == 3:
                            prints("角色处理超时，重上")
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                        # 刷新列表
                        #tk.trickit()
                        time.sleep(5)
                        qingkongyouxichuangkou()
                        # 换完角色跳出从头开始
                        Imok = False
                        break
                    FinStr = dw.RsJCdWDvHA(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        break
                    FinStr = dw.RsJCdWDvHA(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints('副本门口处理')
                        检查累积在线奖励()
                        FinStr = dw.uEKuRfCL(272, 483, 501, 544, "虚弱.bmp", "000000", "0.9", 0)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            intx = int(pos[1])
                            inty = int(pos[2])
                            xamo.UIKBudj(intx + 3, inty + 3)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(1)
                            xamo.UIKBudj(426, 403)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(10)
                            清理游戏窗口()
                            continue
                        出售分解(1)
                        向左()
                        time.sleep(0.5)
                        向右()
                        while True:
                            time.sleep(0.2)
                            FinStr = dw.RsJCdWDvHA(509, 533, 583, 570, "练习模式", "ddc593-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                time.sleep(1)
                                弹起()
                                FinStr = dw.uEKuRfCL(412, 347, 555, 409, "副本界面_格兰迪.bmp|副本界面_格兰迪1.bmp", "000000", "0.9", 0)
                                pos = FinStr.split('|')
                                if int(pos[1]) > 0:
                                    for i in range(5):
                                        xamo.KJDfekiHDh(37, 1)
                                        time.sleep(0.2)
                                    for i in range(maoxiandengji - 1):
                                        xamo.KJDfekiHDh(39, 1)
                                        time.sleep(0.2)
                                    xamo.KJDfekiHDh(32, 3)
                                    time.sleep(0.2)
                                    xamo.KJDfekiHDh(32, 3)
                                    time.sleep(3)
                                else:
                                    xamo.KJDfekiHDh(38, 1)
                                    time.sleep(1)
                            FinStr = dw.RsJCdWDvHA(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                break
                        break
                if Imok == False:
                    break
                prints('捡取 = ' + str(jianqu))
                xingwei = True
                guanqia = 0
                duobidihuo = False
                Imok = True
                time_is = True
                while_time = datetime.datetime.now()
                # 游戏内循环执行
                prints('进入副本')
                while True:
                    time.sleep(0.05)
                    if zhongduan_cha() == 1:
                        Imok = False
                        break
                    if guanqia == 0:
                        guanqia = 检查关卡()
                    if xingwei:
                        # 关卡7再次检查确认
                        # 如果还能在小地图找到人物，证明走错了关卡，就按关卡检查的返回
                        if guanqia == 7:
                            guanqia_temp = 检查关卡()
                            if guanqia_temp > 0:
                                guanqia = guanqia_temp
                        prints('关卡 = ' + str(guanqia))
                        if guanqia > 0:
                            duobidihuo = 关卡构造(zhiye,guanqia)
                            xingwei = False
                    FinStr = dw.uEKuRfCL(0, 78, 799, 552, "可破坏.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        打石头()
                    if str(jianqu) == '真':
                        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "wp.bmp", "000000", "0.9", 0)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            弹起()
                            捡取()
                            FinStr = dw.uEKuRfCL(0, 78, 799, 552, "可破坏.bmp", "000000", "0.9", 0)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                打石头()
                    FinStr = dw.uEKuRfCL(718, 25, 795, 105, "问号绿.bmp|问号黄.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        找门(guanqia, 0, jianqu)
                        time.sleep(1)
                        xingwei = True
                        guanqia = 0
                        continue
                    else:
                        # 走到错误的关卡,Boss前一关按照走错处理
                        FinStr = dw.uEKuRfCL(718, 25, 795, 105, "错关.bmp|错关1.bmp", "000000", "0.9", 0)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            找门(guanqia, 1, jianqu)
                            time.sleep(1)
                            xingwei = True
                            if guanqia == 6:
                                guanqia += 1
                            else:
                                guanqia = 0
                            continue
                        else:
                            if zhiye == 2:
                                打怪_风法()
                    FinStr = dw.uEKuRfCL(612, 132, 735, 164, "通关.bmp", "000000", "0.9", 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        duobidihuo = False
                        弹起()
                        boss关捡取()
                        弹起()
                        清理游戏窗口()
                        color = dw.LYqISzEsHWMD(339, 553)
                        if color == "0b0b0b" or color == "333333":
                            print('返回城镇')
                            fanhuichengzhen()
                            time.sleep(3)
                            break
                        else:
                            fz_ret = 检查负重()
                            if fz_ret == 1:
                                fanhuichengzhen()
                                time.sleep(3)
                                break
                            else:
                                xamo.KJDfekiHDh(121, 1)
                                time.sleep(1)
                                xamo.KJDfekiHDh(121, 1)
                                time.sleep(1)
                                xamo.KJDfekiHDh(121, 1)
                                time.sleep(5)
                                break
                    FinStr = dw.RsJCdWDvHA(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        弹起()
                        break
                    if zhiye == 1:
                        # 躲避
                        FinStr = dw.uEKuRfCL(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            myX = int(pos[1])
                            myY = int(pos[2])
                            FinStr = dw.AIdCpitUAXsF(myX - 100, myY + 130, myX + 120, myY + 210,"ff0094-101010|ff00ff-101010", 1.0, 0)
                            pos = FinStr.split('|')
                            if int(pos[0]) > 0:
                                rand = random.randint(1, 2)
                                if rand == 1:
                                    向上()
                                    time.sleep(1)
                                    弹起()
                                elif rand == 2:
                                    向下()
                                    time.sleep(1)
                                    弹起()
                        if duobidihuo:
                            躲避地火(jianqu)
                            技能(2)
                            color = dw.LYqISzEsHWMD(52, 566)
                            if color == '000000':
                                xamo.KJDfekiHDh(49, 1)
                    # 图内超时判断
                    FinStr = dw.RsJCdWDvHA(333, 571, 473, 597, "只能城镇交易", "ffff00-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        time_is = True
                        while_time = datetime.datetime.now()
                    if time_is == True:
                        while_time_now = datetime.datetime.now()
                        time_temp = while_time_now.minute - while_time.minute
                        if time_temp > 6:
                            prints("图内超时，重上")
                            end_exsit(2)
                            time.sleep(2)
                            Imok = False
                            break
                if Imok == False:
                    break
            time.sleep(1)
if __name__ == '__main__':
    multiprocessing.freeze_support()
    addfile2autorun(os.getcwd() + '\start.bat')
    # t = threading.Thread(target=loop, name='LoopThread')
    # t.setDaemon(True)
    # t.start()
    while_()