#!/usr/bin/python
#-*- coding: UTF-8 -*-
import public
import win32com.client
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
import md5
import tk
import threading
import connect
import os
import ctypes
from PIL import ImageGrab
from PIL import Image
#界面
tk_wins = threading.Thread(target=tk.win)
tk_wins.start()
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
def prints(strs):
    tk.text(strs)
dll = ctypes.windll.LoadLibrary(os.getcwd() + '/testgame.dll')
dll.SetDllPathW(os.getcwd() + '/wiwl.dll',0)
dw = win32com.client.Dispatch('dm.dmsoft')
dw_ret = dw.Reg("weijiawlb1956e24a37f27f5cb5a7e139c2ecb2a", "pythonS")
dw.SetDict(0, "soft.txt")
dw.SetDict(1, "常用7000.txt")
dw.SetDict(2, "number.txt")
dw.UseDict(0)
dw.SetPath("\Image")
pc_name = get_ini('config/cfg.ini', '软件配置', 'pc_name', "")
HZ_ = int(get_ini('config/cfg.ini', '软件配置', '后缀', "0"))
xiaoguo = xg.xgdx()
x = int(get_ini('config/cfg.ini', '主配置', 'x', "0"))
y = int(get_ini('config/cfg.ini', '主配置', 'y', "0"))
xamo = test.HZ(x, y, HZ_, 0xC317, 0xF001)
hwnd = dw.FindWindow("", pc_name + ') - VNC')
if hwnd >= 0:
    dw.MoveWindow(hwnd, -8, -1)
    dw.SetWindowState(hwnd,12)
    print('开始绑定')
    dm_ret = dw.BindWindow(hwnd,"gdi","normal","normal",0)
    time.sleep(1)
    if dm_ret == 1:
        print('绑定成功')
        dw.MoveWindow(hwnd, -2000, -2000)
class account_value:
    def __init__(self, hao="", mi="", daqu="", zongjuese="", dangqianjuesi="",zhanghaobianhao="",zhanghaozongshu="",dituid=0):
        self.hao = hao
        self.mi = mi
        self.daqu = daqu
        self.zongjuese = zongjuese
        self.dangqianjuese = dangqianjuesi
        self.zhanghaobianhao = zhanghaobianhao
        self.zhanghaozongshu = zhanghaozongshu
        self.dituid = dituid
    def get_value(self):
        return self.hao, self.mi, self.daqu, self.zongjuese, self.dangqianjuese
account = account_value()
# 定义参数
jn_key = {'拉莫斯': 81, '桑德尔': 87, '牛头王': 69, '路易斯': 82, '伊伽贝拉': 84, '召唤兽狂化': 89, '鞭子': 65, '海伊伦': 83,'冰': 68, '火': 70, '光': 71, '暗': 72}
jn_time = {'伊伽贝拉': 200, '冰': 200, '火': 200, '光': 200, '暗': 200,'拉莫斯':200,'海伊伦':200}
jn_now_time = {'拉莫斯': '2018-03-30 21:44:09', '桑德尔': '2018-03-30 21:44:09', '牛头王': '2018-03-30 21:44:09','路易斯': '2018-03-30 21:44:09', '伊伽贝拉': '2018-03-30 21:44:09', '召唤兽狂化': '2018-03-30 21:44:09','鞭子': '2018-03-30 21:44:09', '海伊伦': '2018-03-30 21:44:09', '冰': '2018-03-30 21:44:09','火': '2018-03-30 21:44:09', '光': '2018-03-30 21:44:09', '暗': '2018-03-30 21:44:09'}
jn_sf_time = {'拉莫斯': 1.6, '桑德尔': 0.9, '牛头王': 1.3, '路易斯': 1.1, '伊伽贝拉': 1.1, '召唤兽狂化': 0.8, '鞭子': 0.3,'海伊伦': 1.1, '冰': 0.8, '火': 0.8, '光': 0.8, '暗': 0.8}
public_code = md5.get_disk_info() + pc_name
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
def 截图(x,y,x1,y1,name,is_b):
    bbox = (x,y,x1,y1)
    im = ImageGrab.grab(bbox)
    if is_b:
        return im
    im.save(name)   #需要修改
def 发送记录():
    pass
    # try:
    #     with open('config/记录.ini', 'r') as f:
    #         data = f.read()
    #         tcpCliSock.send(('JL' + data).encode('gb2312'))
    # except:
    #     pass
def single_get_first(unicode1):
    str1 = unicode1.encode('gbk')
    try:
        ord(str1)
        return str1
    except:
        asc = str1[0] * 256 + str1[1] - 65536
        if asc >= -20319 and asc <= -20284:
            return 'a'
        if asc >= -20283 and asc <= -19776:
            return 'b'
        if asc >= -19775 and asc <= -19219:
            return 'c'
        if asc >= -19218 and asc <= -18711:
            return 'd'
        if asc >= -18710 and asc <= -18527:
            return 'e'
        if asc >= -18526 and asc <= -18240:
            return 'f'
        if asc >= -18239 and asc <= -17923:
            return 'g'
        if asc >= -17922 and asc <= -17418:
            return 'h'
        if asc >= -17417 and asc <= -16475:
            return 'j'
        if asc >= -16474 and asc <= -16213:
            return 'k'
        if asc >= -16212 and asc <= -15641:
            return 'l'
        if asc >= -15640 and asc <= -15166:
            return 'm'
        if asc >= -15165 and asc <= -14923:
            return 'n'
        if asc >= -14922 and asc <= -14915:
            return 'o'
        if asc >= -14914 and asc <= -14631:
            return 'p'
        if asc >= -14630 and asc <= -14150:
            return 'q'
        if asc >= -14149 and asc <= -14091:
            return 'r'
        if asc >= -14090 and asc <= -13119:
            return 's'
        if asc >= -13118 and asc <= -12839:
            return 't'
        if asc >= -12838 and asc <= -12557:
            return 'w'
        if asc >= -12556 and asc <= -11848:
            return 'x'
        if asc >= -11847 and asc <= -11056:
            return 'y'
        if asc >= -11055 and asc <= -10247:
            return 'z'
        return ''
def getPinyin(string):
    if string == None:
        return None
    lst = list(string)
    charLst = []
    for l in lst:
        charLst.append(single_get_first(l))
    return ''.join(charLst)
def loop():
    pass
    # is_pc_name = True
    # is_zh = True
    # number = get_ini('config/cfg.ini', '主配置', '账号路径', "")
    # numstr = ""
    # while True:
    #     try:
    #         if is_pc_name:
    #             tcpCliSock.send('PC'.encode() + pc_name.encode())
    #             is_pc_name = False
    #         if is_zh:
    #             for t in range(500):
    #                 num = get_ini(number, pc_name, str(t + 1), "")
    #                 if num != '':
    #                     numstr = numstr + str(t + 1) + '='+ num + '\n'
    #                 else:
    #                     break
    #             tcpCliSock.send(('ZH' + numstr).encode('gb2312'))
    #             time.sleep(1)
    #             发送记录()
    #             is_zh = False
    #         while True:
    #             try:
    #                 accept_data = tcpCliSock.recv(1024).decode()
    #                 if accept_data == 'jietu':
    #                     截图(0,0,800,600,os.getcwd() + "/temp.jpg",False)
    #                     with open(os.getcwd() + "/temp.jpg",'rb') as f:
    #                         for data in f:
    #                             tcpCliSock.send('JT'.encode() + data)
    #                             accept_data = tcpCliSock.recv(1024).decode()
    #                     tcpCliSock.send('JS'.encode())
    #             except:
    #                 tcpCliSock.send('RJ'.encode())#检查主机状态顺带发送心跳
    #     except:
    #         is_pc_name = True
    #         public.ShiLian = True
    #         time.sleep(10)
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
def 记录完成时间():
    num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
    juese = get_ini("config/记录.ini", "刷号记录", "当前角色","")
    qu  = get_ini("config/记录.ini", "刷号记录", "当前大区","")
    date = datetime.datetime.now()
    set_ini('config/记录.ini', '完成时间', num + '_' + qu + '_' + juese, date.strftime('%Y-%m-%d %H:%M:%S'))
def 记录完成时间_转钱():
    num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
    set_ini('config/记录.ini', '转账', num,'完成')
def 刷新列表():
    tk.trickit()
def end_exsit():
    x = int(get_ini('config/cfg.ini', '主配置', 'x', "0"))
    y = int(get_ini('config/cfg.ini', '主配置', 'y', "0"))
    prints(str(x) + '：' + str(y))
    for i in range(5):
        FinStr = dw.FindPicE(0, y-500, x + 500, y, "批处理.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx, inty)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.LbferJhd('C:\ql.bat')
            time.sleep(1)
            xamo.UIKBudj(intx, inty)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.KJDfekiHDh(13,2)
            time.sleep(5)
            for i in range(5):
                FinStr = dw.FindPicE(0, y - 500, x + 500, y, "批处理.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(0.5)
                    xamo.LbferJhd('C:\ql.bat')
                    time.sleep(1)
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(0.5)
                    xamo.KJDfekiHDh(13, 2)
                    time.sleep(5)
            break
        else:
            prints('打开批处理')
            xamo.LKDFemrrh(91)
            xamo.KJDfekiHDh(82, 1)
            xamo.LJDFnmeFSD(91)
            time.sleep(1)
def 重启():
    x = int(get_ini('config/cfg.ini', '主配置', 'x', "0"))
    y = int(get_ini('config/cfg.ini', '主配置', 'y', "0"))
    for i in range(5):
        FinStr = dw.FindPicE(0, y-500, x + 500, y, "批处理.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx, inty)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.LbferJhd('shutdown -r -t 0')
            time.sleep(1)
            xamo.UIKBudj(intx, inty)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.KJDfekiHDh(13, 1)
            time.sleep(5)
            for i in range(5):
                FinStr = dw.FindPicE(0, y - 500, x + 500, y, "批处理.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(0.5)
                    xamo.LbferJhd('shutdown -r -t 0')
                    time.sleep(1)
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(0.5)
                    xamo.KJDfekiHDh(13, 1)
                    time.sleep(5)
            break
        else:
            xamo.LKDFemrrh(91)
            xamo.KJDfekiHDh(82, 1)
            xamo.LJDFnmeFSD(91)
            time.sleep(1)
    for m in range(120):
        prints('等待重启 ' + str(m + 1) +'/120')
        time.sleep(1)
def 日期比较(p_now):
    try:
        d1 = datetime.datetime.strptime(p_now, '%Y-%m-%d %H:%M:%S')
        d2 = datetime.datetime.now()
        return d2.__gt__(d1)
    except:
        prints("报错######比较时间失败")
        input()
def 更新(p_now):
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
def 封号查询(num):
    p_now = get_ini("config/记录.ini", "封号", num,"")
    if p_now != "":
        temp = 日期比较(p_now)
        if temp:
            remove_option("config/记录.ini", "封号", num)
            return True
        return False
    else:
        return True
def 制裁查询(num):
    p_now = get_ini("config/记录.ini", "制裁", num,"")
    if p_now != "":
        temp = 日期比较(p_now)
        if temp:
            remove_option("config/记录.ini", "制裁", num)
            return True
        return False
    else:
        return True
def 转账查询(num):
    p_now = get_ini("config/记录.ini", "转账", num,"")
    if p_now != "":
        return False
    return True
def 完成查询(num):
    p_now = get_ini("config/记录.ini", "完成", num,"")
    if p_now != "":
        return False
    return True
def 密码错误查询(num):
    p_now = get_ini("config/记录.ini", "密码错误", num,"")
    if p_now != "":
        return False
    return True
def 冻结查询(num):
    p_now = get_ini("config/记录.ini", "冻结", num,"")
    if p_now != "":
        return False
    return True
def get_account(path):
    prints("获取账号")
    try:
        for ic in range(500):
            num = get_ini(path,pc_name,str(ic + 1),"")
            if num != "":
                arr = num.split("=")
                hao = arr[0]
                juese = arr[3]
                #检查封号,制裁,冻结,密码错误
                if 封号查询(hao) and 制裁查询(hao) and 完成查询(hao+'_'+arr[2]) and 密码错误查询(hao) and 冻结查询(hao):
                    #逐角色判断时间
                    for i in range(int(juese)):
                        returns_now = get_ini('config/记录.ini', '完成时间', hao + '_' + arr[2] + '_' + str(int(i) + 1),"")
                        if returns_now != "":
                            if 更新(returns_now):
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
        for ic in range(500):
            num = get_ini(path,pc_name,str(ic + 1),"")
            if num != "":
                arr = num.split("=")
                hao = arr[0]
                juese = arr[3]
                #检查封号
                if 封号查询(hao) and 转账查询(hao):
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
def 角色处理(leixing):
    prints("选择角色")
    try:
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
        juese_time = time.clock()
        while True:
            time.sleep(0.5)
            FinStr = dw.FindStrE(507, 531, 593, 564, "结束游戏", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) >= 0:
                break
            else:
                xamo.KJDfekiHDh(27,1)
                time.sleep(3)
                FinStr = dw.FindStrE(360, 459, 413, 477, "选择角色", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) >= 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx + 10, inty - 10)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    time.sleep(5)
            time.sleep(1)
            juese_time_now = time.clock()
            time_temp = juese_time_now - juese_time
            if time_temp > 180:
                清理游戏窗口()
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
                if 更新(returns_now):
                    juese = str(i + 1)
                    break
            else:
                juese = str(i+1)
        while True:
            time.sleep(0.5)
            FinStr = dw.FindStrE(507, 531, 593, 564, "结束游戏", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) >= 0:
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
                lv = dw.Ocr(p_x[int(juese) - juese_index], p_y[int(juese) - juese_index], p_x[int(juese) - juese_index] + 60,p_y[int(juese) - juese_index] + 18, "d1b994-000000", 1)
                if lv != "":
                    lv = re.sub("\D", "", lv)
                    if len(lv) >= 3:
                        lv = lv[:2]
                    prints('第'+str(juese)+'个角色等级 = ' + str(lv))
                    #添加角色资料[等级]
                    set_ini("config/账号数据.ini", hao + '_' + qu + '_' + str(juese), '等级', str(lv))
                    if int(lv) < 84:
                        set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                        account.dangqianjuese = juese
                        记录完成时间()
                        prints("等级不够卡图，换下个角色")
                        juese = str(int(juese) + 1)
                        if int(juese) > int(zongjuese):
                            set_ini("config/记录.ini", "完成", hao + '_' + qu, '完成')
                            return 0
                        continue
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
            FinStr = dw.FindStrE(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) >= 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.FindPicE(365, 356, 418, 384, "签到.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.FindStrE(307, 106, 585, 304, "赛丽亚", "f7d65a-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.FindPicE(768, 1, 800, 31, "图外.bmp|图外1.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                account.dangqianjuese = juese
                set_ini('config/记录.ini', '刷号记录', "当前角色", juese)
                return 1
            FinStr = dw.FindStrE(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 2
            time.sleep(1)
            juese_time_now = time.clock()
            time_temp = juese_time_now - juese_time
            if time_temp > 180:
                return 3
    except:
        prints("报错######选择角色失败")
        input()
def 中断_查():
    FinStr = dw.FindStrE(348, 267, 463, 324, "网络连接中断", "ffffff-000000", 1)
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
        FinStr = dw.FindStrE(234, 243, 562, 400, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.FindStrE(234, 243, 562, 335, "第三方模块", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints("第三方模块，重启")
                log('三方', account.hao, '三方模块')
                重启()
                time.sleep(2)
                return 1
            FinStr = dw.FindStrE(234, 243, 562, 335, "制裁1小时", "ffffff-000000", 1)
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
                重启()
                time.sleep(2)
                return 1
            FinStr = dw.FindStrE(234, 243, 562, 335, "制裁一天", "ffffff-000000", 1)
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
                重启()
                time.sleep(2)
                return 1
            FinStr = dw.FindStrE(234, 243, 562, 335, "制裁15天", "ffffff-000000", 1)
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
                重启()
                time.sleep(2)
                return 1
            prints('中断制裁未识别，请把【中断截图】文件夹中的截图发给作者')
            dw.Capture(234, 243, 562, 335, str(time.time()) + '.bmp')
        else:
            prints("只是中断没有制裁，重上")
            end_exsit()
            time.sleep(2)
        return 1
    return 0
def 发邮件(CRuser, CRpwd):
    prints("发送邮件")
    money = get_ini('config/cfg.ini','游戏配置', '邮寄金币上限',"1000000")
    qu = get_ini("config/记录.ini", "刷号记录", "当前大区", "")
    num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
    juese = get_ini("config/记录.ini", "刷号记录", "当前角色","")
    KQ = get_ini('config/跨区数据.ini', '跨区表', qu, "")
    KQ = '跨' + KQ
    prints('跨区 = ' + KQ)
    #3A
    name = get_ini('config/仓库设置.ini', '仓库名称', KQ, "")
    fyj_time = time.clock()
    try:
        while True:
            FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                xamo.UIKBudj(334, 235)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(3)
            else:
                xamo.KJDfekiHDh(27,1)
                time.sleep(3)
            FinStr = dw.FindStrE(338, 138, 419, 169, "邮件保管箱", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                break
            if 中断_查() >0:
                return 2
            fyj_time_now = time.clock()
            if fyj_time_now - fyj_time > 180:
                prints("发邮件超时，取消")
                清理游戏窗口()
                return 3
            time.sleep(0.5)
        if name == "":
            prints("没有仓库号")
            # 检查金币
            number = dw.Ocr(610, 529, 700, 549, "e6c89b-000000", 1)
            if len(number) > 4:
                set_ini('config/账号数据.ini', num + '_' + qu + '_' + juese, '金币', number[:-4])
            清理游戏窗口()
            return
        prints('仓库号信息 = ' + name)
        #跨区仓库
        kuaqu = ""
        name_arr = name.split('|')
        if qu != name_arr[1]:
            #如 江苏5/7区  只用取 江苏5
            index = name_arr[1].find("/")
            if index > 0:
                temp = name_arr[1].split("/")
                kuaqu = temp[0]
            else:
                kuaqu = name_arr[1][0:-1]
        #检查金币
        number = dw.Ocr(610, 529, 700, 549,"e6c89b-000000",1)
        if int(number) < int(money):
            if len(number) > 4:
                set_ini('config/账号数据.ini',num + '_' + qu + '_' + juese,'金币',number[:-4])
            prints("游戏币不够设置的金额")
            清理游戏窗口()
            return
        while True:
            FinStr = dw.FindStrE(278, 139, 341, 171, "发送邮件", "ddc593-000000", 1)
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
            FinStr = dw.FindStrE(202, 169, 246, 191, "收件人", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                is_name = False
                for intemp in range(3):
                    xamo.UIKBudj(intx + 104, inty + 5)
                    time.sleep(1)
                    xamo.PPWEbxbar(1)
                    for tin in range(15):
                        xamo.KJDfekiHDh(8,1)
                        time.sleep(0.05)
                    time.sleep(3)
                    #输入收件人
                    输入汉字(name_arr[0])
                    time.sleep(3)
                    dw.UseDict(1)
                    FinStr = dw.FindStrE(244, 166, 368, 193, name_arr[2], "ffffff-000000", 1)
                    dw.UseDict(0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints('仓库号名称匹配成功')
                        is_name = True
                        break
                if not is_name:
                    prints('仓库号名称匹配失败')
                    return 3
                xamo.UIKBudj(intx + 203, inty + 5)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                break
            if 中断_查() >0:
                return 2
            fyj_time_now = time.clock()
            if fyj_time_now - fyj_time > 180:
                prints("发邮件超时，取消")
                清理游戏窗口()
                return 3
            time.sleep(0.5)
        while True:
            FinStr = dw.FindStrE(315, 261, 451, 294, "选择接收区", "ffffff-000000", 1)
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
                        FinStr = dw.FindStrE(323, 307, 369, 475, kuaqu, "ddc593-000000", 1)
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
                            清理游戏窗口()
                            return
                        time.sleep(0.5)
                    break
            if 中断_查() >0:
                return 2
            fyj_time_now = time.clock()
            if fyj_time_now - fyj_time > 180:
                prints("发邮件超时，取消")
                清理游戏窗口()
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
        while True:
            FinStr = dw.FindPicE(472, 256, 767, 436, "魔刹石.bmp|挑战书.bmp|无尽的永恒.bmp|数据芯片.bmp|迷幻晶石.bmp|强烈之痕迹.bmp|矛盾的结晶体.bmp|浓缩的异界精髓.bmp", "000000", 0.9, 0)
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
            if tianjiashuliang >= 10:
                break
            if 中断_查() >0:
                return 2
            fyj_time_now = time.clock()
            if fyj_time_now - fyj_time > 180:
                prints("发邮件超时，取消")
                清理游戏窗口()
                return 3
        #选择副职业
        xamo.UIKBudj(638, 246)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(3)
        while True:
            FinStr = dw.FindPicE(472, 260, 716, 413, "紫色卡片.bmp|粉色卡片.bmp", "000000", 0.9, 0)
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
            if 中断_查() >0:
                return 2
            fyj_time_now = time.clock()
            if fyj_time_now - fyj_time > 180:
                prints("发邮件超时，取消")
                清理游戏窗口()
                return 3
        #输入金币
        xamo.UIKBudj(333, 412)
        time.sleep(0.5)
        xamo.PPWEbxbar(1)
        time.sleep(0.5)
        prints("税前 = " + number)
        bl = int(number) / 100 * 10
        number = str(int(number) - int(bl))
        prints("税后 = " + number)
        if len(str(int(bl / 2))) > 4:
            set_ini('config/账号数据.ini', num + '_' + qu + '_' + juese, '金币', str(int(bl / 2))[:-4])
        log('支出',account.hao,str(number))
        xamo.LbferJhd(number)
        time.sleep(1)
        if not os.path.exists(os.getcwd() + '/发邮件截图'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs(os.getcwd() + '/发邮件截图')
        dw.CaptureJpg(1, 1, 800, 600, os.getcwd() + '/发邮件截图/' + str(time.time()) + '.jpg', 20)
        #发送
        xamo.UIKBudj(261, 461)
        time.sleep(1)
        xamo.PPWEbxbar(1)
        time.sleep(1)
        xamo.UIKBudj(261 - 60, 461)
        xamo.PPWEbxbar(2)
        time.sleep(3)
        while True:
            FinStr = dw.FindPicE(232, 69, 693, 499, "发邮件验证码.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                time.sleep(1)
                intx = int(pos[1])
                inty = int(pos[2])
                #打码
                dw.Capture(intx - 207, inty - 22, intx - 78, inty + 30, os.getcwd() + "/ver.jpg")
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
                FinStr = dw.FindStrE(346, 278, 449, 309, "已成功发送邮件", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    清理游戏窗口()
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
            if 中断_查() >0:
                return 2
            fyj_time_now = time.clock()
            if fyj_time_now - fyj_time > 180:
                prints("发邮件超时，取消")
                清理游戏窗口()
                return 3
        return 1
    except:
        prints("报错######发送邮件失败")
def 区服选择(x,y,qu):
    FinStr = dw.FindStrE(0, 0, x, y, "区服选择", "f0f0f0-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        time.sleep(1)
        intx = int(pos[1])
        inty = int(pos[2])
        # 拉到最上
        xamo.UIKBudj(intx + 728, inty + 48)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(2)
        fuwuqi = qu[0:2]
        xianlu = ''
        if fuwuqi == '广东' or fuwuqi == '广西'or fuwuqi == '湖南' or fuwuqi == '湖北' or fuwuqi == '上海' or fuwuqi == '江苏':
            xianlu = '电信'
        elif fuwuqi == '浙江' or fuwuqi == '安徽' or fuwuqi == '福建' or fuwuqi =='江西' or fuwuqi == '西北' or fuwuqi =='西南':
            xianlu = '电信'
        elif fuwuqi == '陕西' or fuwuqi == '云贵' or fuwuqi == '四川' or fuwuqi == '重庆' or fuwuqi == '新疆':
            xianlu = '电信'
        elif fuwuqi == '华北' or fuwuqi == '河北' or fuwuqi == '天津' or fuwuqi == '东北' or fuwuqi == '北京' or fuwuqi == '内蒙':
            xianlu = '网通'
        elif fuwuqi == '辽宁' or fuwuqi == '吉林' or fuwuqi == '黑龙' or fuwuqi == '河南' or fuwuqi == '山东' or fuwuqi == '西北':
            xianlu = '网通'
        FinStr = dw.FindStrE(intx, inty, intx + 200, inty + 200, xianlu , "b3b3b3-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(int(pos[1]) + 10, int(pos[2]) + 3)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(2)
            #取出区名里的数字
            qu_temp = re.sub("\D", "", qu)
            #取出第一个数字出现的位置
            qu_weizhi = qu.index(qu_temp[0:1])
            #截取0到数字出现的位置中间的文本
            qu_qianzhui = qu[0:qu_weizhi]
            FinStr = dw.FindStrE(intx, inty, intx + 700, inty + 470, qu_qianzhui + "区", "3c3c3c-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                xamo.UIKBudj(int(pos[1]) + 10, int(pos[2]) + 3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(2)
                #拖动到最下
                xamo.UIKBudj(intx + 728, inty + 458)
                time.sleep(0.2)
                xamo.PPWEbxbar(2)
                time.sleep(2)
                FinStr = dw.FindStrE(intx, inty, intx + 700, inty + 470, qu, "3c3c3c-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    xamo.UIKBudj(int(pos[1]) + 10, int(pos[2]) + 3)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    #确定
                    xamo.UIKBudj(intx + 562, inty + 494)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
def is_xy(im,x,y):
    is_x = True
    is_y = True
    for xt in range(12):
        try:
            temp = im[x + xt, y]
            if temp == 1:
                is_x = False
        except:
            is_x = False
    for yt in range(10):
        try:
            temp = im[x, y + yt]
            if temp == 1:
                is_y = False
        except:
            is_y = False
    if is_x and is_y:
        temp_p = 0
        for xt in range(12):
            try:
                temp = im[x - xt, y]
                temp_p += temp
            except:
                is_x = False
        if temp_p < 9:
            is_x = False
        temp_p = 0
        for yt in range(12):
            try:
                temp = im[x, y - yt]
                temp_p += temp
            except:
                is_y = False
        if temp_p < 9:
            is_y = False
    return is_x,is_y
def imxy(p):
    img = Image.open(p)
    Img = img.convert('L')  # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    threshold = 100  #自定义灰度界限，大于这个值为黑色，小于这个值为白色
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = Img.point(table, '1')  # 图片二值化
    box = (120, 0, 278, 155)  #确定拷贝区域大小
    region = photo.crop(box)  #将im表示的图片对象拷贝到region中，大小为box
    pix = region.load()
    for y in range(500):
        try:
            temp = pix[0, y]
        except:
            break
        for x in range(500):
            try:
                temp = pix[x, y]
                if temp == 0:
                    zs_x, zs_y = is_xy(pix, x, y)
                    if zs_x and zs_y:
                        return x
            except:
                break
    return 0
def 登录游戏(CRuser,CRpwd,path,WeGame,money_is,x,y):
    prints("登录账号")
    account_path = path
    login_time = time.clock()
    while True:
        六点更新()
        if money_is == '真':
            hao, mi, qu, jue = get_account_zhuanqian(account_path)
        else:
            hao, mi, qu, jue = get_account(account_path)
        if hao == "":
            prints('没有可刷账号，等待6点更新')
            time.sleep(30)
        else:
            break
    tk.trickit()
    # 两个地方检查更新、开始时和进入地下城时
    检查更新()
    扫图标()
    for temp in range(100):
        xamo.UIKBudj(1, 1)
        FinStr = dw.FindPicE(0, 0, x, y, "WeGame.bmp|WeGame1.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 10, inty + 10)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            xamo.PPWEbxbar(1)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            break
        else:
            prints('没有找到WeGame图标')
            time.sleep(5)
    # 恢复打印机窗口
    try:
        MC_cishu = 0
        code_cishu = 0
        while True:
            time.sleep(0.5)
            FinStr = dw.FindPicE(0, 0, x, y, "tgp_登录.bmp|tgp_登录1.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                #刷新列表
                FinStr = dw.FindPicE(0, 0, x, y, "QQ账号.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    py1 = 99
                    py2 = 67
                else:
                    py1 = 136
                    py2 = 106
                刷新列表()
                xamo.UIKBudj(intx + 70, inty - py1)
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
                xamo.UIKBudj(intx + 70, inty - py2)
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
                xamo.UIKBudj(intx - 30, inty - 30)
            FinStr = dw.FindStrE(0, 0, x, y, "拖动滑块", "000000-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints('滑块验证码')
                intx = int(pos[1])
                inty = int(pos[2])
                if code_cishu > 0:
                    xamo.UIKBudj(intx + 270, inty + 5)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                time.sleep(2)
                dw.Capture(intx + 1,inty + 22, intx + 280, inty + 179, os.getcwd() + "/ver.bmp")
                dx = imxy(os.getcwd() + "/ver.bmp")
                if dx > 0:
                    time.sleep(0.5)
                    px = intx + 40
                    py = inty + 199
                    xamo.UIKBudj(px, py)
                    time.sleep(1)
                    xamo.cndjGdsbSdg()
                    time.sleep(1)
                    xamo.UIKBudj(intx + 120 + dx + 20, py)
                    time.sleep(1)
                    xamo.mboHdjGsV()
                    time.sleep(5)
                    # 确认后延迟大点
                    code_cishu += 1
                else:
                    xamo.UIKBudj(intx + 270, inty + 5)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)

            FinStr = dw.FindStrE(0, 0, x, y, "查看登陆地", "e9b63b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints('字母验证码')
                intx = int(pos[1])
                inty = int(pos[2])
                time.sleep(2)
                dw.CaptureJpg(intx - 24,inty - 119, intx + 104, inty - 66, os.getcwd() + "/ver.jpg",20)
                with open(os.getcwd() + "/ver.jpg",'rb') as f:
                    im = f.read()
                time.sleep(0.5)
                dc = rk.RClient(CRuser, CRpwd, "16589", "d47ebffa337e6900f3d4b12e8c1214ce")
                yzm = dc.rk_create(im, "2040")
                xy = yzm["Result"]
                prints('返回结果 = ' + xy)
                xamo.UIKBudj(intx + 80, inty - 138)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                for tn in range(5):
                    xamo.KJDfekiHDh(8,1)
                    time.sleep(0.2)
                xamo.LbferJhd(xy)
                time.sleep(1)
                xamo.UIKBudj(intx + 21, inty + 67)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(5)
                #确认后延迟大点
            FinStr = dw.FindPicE(0, 0, x, y, "密错.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                MC_cishu += 1
                if MC_cishu < 5:
                    xamo.UIKBudj(int(pos[1]) + 47, int(pos[2]) + 166)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                else:
                    return 4
            FinStr = dw.FindPicE(0, 0, x, y, "冻结.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 5
            FinStr = dw.FindPicE(0, 0, x, y, "tgp_跳过.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.FindStrE(0, 0, x, y, "今日推荐", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 403, inty + 8)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.FindPicE(0, 0, x, y, "tgp_主页.bmp|tgp_主页1.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 10)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.UIKBudj(10, 10)
                time.sleep(1)
            FinStr = dw.FindPicE(0, 0, x, y, "更新游戏.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 20, inty + 10)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.FindPicE(0, 0, x, y, "tgp_开始游戏.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intxa = int(pos[1])
                intya = int(pos[2])
                FinStr = dw.FindStrE(intxa - 321 , intya - 16, intxa - 199, intya + 30, qu, "3c3c3c-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    xamo.UIKBudj(intxa + 20, intya + 10)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                else:
                    xamo.UIKBudj(intxa - 116, intya + 10)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(2)
                    FinStr = dw.FindStrE(intxa - 326, intya - 186, intxa - 100, intya, qu, "3c3c3c-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx +10, inty + 3)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(2)
                    else:
                        prints('大区列表未找到')
                        FinStr = dw.FindStrE(intxa - 326, intya - 186, intxa - 100, intya, "其他大区", "0095ff-000000",1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            intx = int(pos[1])
                            inty = int(pos[2])
                            xamo.UIKBudj(intx + 10, inty + 3)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(5)
                            区服选择(x,y,qu)
            else:
                FinStr = dw.FindPicE(0, 0, x, y, "tgp_列表_dnf.bmp|tgp_列表_dnf1.bmp", "000000", 1.0, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx, inty)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
            FinStr = dw.FindStrE(0, 0, x, y, "优化跳过", "3c3c3c-000000", 1)
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
            FinStr = dw.FindStrE(0, 0, x, y, "跳过检测", "2098ff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.UIKBudj(0, 0)
                time.sleep(0.5)
            FinStr = dw.FindPicE(0, 0, x, y, "tgp_登录失败.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 101
            FinStr = dw.FindStrE(0, 0, x, y, "连接频道失败", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 0
            FinStr = dw.FindPicE(0, 0, x, y, "登录遮挡图片1.bmp|登录遮挡图片.bmp|登录遮挡图片2.bmp|广告.bmp|广告1.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 10)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            FinStr = dw.FindPicE(0, 0, x, y, "send.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 10)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.KJDfekiHDh(27,1)
                time.sleep(0.5)
            FinStr = dw.FindPicE(0, 0, x, y, "已达游戏上限.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 324, inty + 117)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                FinStr = dw.FindPicE(0, 0, x, y, "tgp_x.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    xamo.UIKBudj(intx + 10, inty + 10)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
            FinStr = dw.FindStrE(0, 0, x, y, "结束游戏", "ddc593-000000|ffffb8-000000", 0.9)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints('角色界面')
                ret_ydck = 移动窗口(x,y)
                if ret_ydck == 0:
                    return 0
                return 1
            login_time_now = time.clock()
            if login_time_now - login_time > 360:
                return 3
    except:
        prints("报错######登录账号失败")
        input()
def 移动窗口(x,y):
    color = 'ddc593'
    for temp_i in range(6):
        FinStr = dw.FindStrE(0, 0, x, y, "结束游戏", "ddc593-000000|ffffb8-000000", 0.9)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            prints('移动窗口')
            intx = int(pos[1])
            inty = int(pos[2])
            time.sleep(3)
            xamo.UIKBudj(intx - 144, inty - 530)
            time.sleep(0.2)
            xamo.cndjGdsbSdg()
            time.sleep(0.2)
            xamo.UIKBudj(379, 11)
            time.sleep(0.2)
            xamo.mboHdjGsV()
            time.sleep(2)
            color1 = dw.GetColor(525, 541)
            color2 = dw.GetColor(569, 551)
            color3 = dw.GetColor(255, 546)
            if color == color1 == color2 == color3:
                prints('移动窗口完成')
                return 1
            else:
                xamo.UIKBudj(379, 11)
                time.sleep(0.2)
                xamo.cndjGdsbSdg()
                time.sleep(0.2)
                xamo.UIKBudj(479, 111)
                time.sleep(0.2)
                xamo.mboHdjGsV()
                time.sleep(2)
    prints('移动窗口失败')
    return 0
def 封号检查():
    FinStr = dw.FindStrE(359, 283, 435, 299, "网络连接中断", "ffffff-000000", 1)
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
        FinStr = dw.FindStrE(234, 243, 562, 400, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.FindStrE(238, 243, 562, 335, "停封5天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                number = dw.Ocr(414, 291, 526, 307, "ffffff-000000", 1)
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
            FinStr = dw.FindStrE(238, 243, 562, 335, "停封7天", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                number = dw.Ocr(414, 291, 526, 307, "ffffff-000000", 1)
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
            FinStr = dw.FindStrE(234, 243, 562, 335, "永久封号", "ffffff-000000", 1)
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
            FinStr = dw.FindStrE(234, 243, 562, 335, "第三方模块", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints("第三方模块，重启")
                log('三方', account.hao, "三方模块")
                end_exsit()
                time.sleep(2)
                return 'F0'
            prints('封号类型未识别，请把【中断截图】文件夹中的截图发给作者')
            dw.Capture(234, 243, 562, 335, str(time.time()) + '.bmp')
        else:
            return 'F0'
    FinStr = dw.FindStrE(234, 243, 562, 335, "此ID已在游戏", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 'F101'
    return ''
def 清除刷图记录():
    try:
        config = configparser.ConfigParser()
        config.read("config/记录.ini")
        ret = config.options('完成时间')
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
def 六点更新():
    try:
        temp = get_ini("config/记录.ini", "更新", '六点更新',"")
        d2 = datetime.datetime.now()
        print("d1 = " + temp + ",d2 = " + d2.strftime("%Y-%m-%d %H:%M:%S"))
        if temp != "":
            d1 = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S')
            days = d2.day - d1.day
            day = d2 - d1
            if day.days >= 1:
                清除刷图记录()
                刷新列表()
                prints('六点更新成功')
                set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
            elif days > 1:
                清除刷图记录()
                刷新列表()
                prints('六点更新成功')
                set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
            elif days == 1:
                    if d2.hour >= 6:
                        清除刷图记录()
                        刷新列表()
                        prints('六点更新成功')
                        set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
            elif days == 0:
                if d1.hour < 6:
                    if d2.hour >= 6:
                        清除刷图记录()
                        刷新列表()
                        prints('六点更新成功')
                        set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            set_ini("config/记录.ini", "更新", '六点更新', d2.strftime("%Y-%m-%d %H:%M:%S"))
    except:
        prints('六点更新失败')
def 扫图标():
    x = int(get_ini('config/cfg.ini', '主配置', 'x', "0"))
    y = int(get_ini('config/cfg.ini', '主配置', 'y', "0"))
    xh = x - 400
    yh = y - 15
    for i in range(200):
        xamo.UIKBudj(xh + i * 2, yh)
def 出售点券():
    prints('兑换点券')
    int_quan = 0
    while True:
        FinStr = dw.FindStrE(397,390,690,552, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            number = dw.Ocr(intx +25 + 44, intx + 93, inty + 69, "e6c89b-000000", 1)
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
    清理游戏窗口()
    if int_quan == 0:
        wenzi = '一百万'
    elif int_quan == 1:
        wenzi = '一千万'
    else:
        wenzi = '一百万'
    while True:
        if wenzi == '':
            return 1
        FinStr = dw.FindStrE(41, 534,114, 566, "寄售金币", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.FindPicE(160, 545, 191, 573, "商城.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                xamo.UIKBudj(761, 24)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(2)
            FinStr = dw.FindStrE(34, 148, 89, 418, wenzi, "ddc593-000000", 1)
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
                    FinStr = dw.FindStrE(484, 122, 540, 309, '购买', "ffb400-000000", 1)
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
                        elif aq_ret == 3:
                            break
                        FinStr = dw.FindStrE(293, 235, 503, 356, '拍卖行不存在', "ffffff-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            xamo.UIKBudj(400, 319)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                            while True:
                                FinStr = dw.FindPicE(160, 545, 191, 573, "商城.bmp", "000000", 0.9, 0)
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
                        FinStr = dw.FindStrE(293, 235, 503, 356, '完成竞拍', "ffffff-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            xamo.UIKBudj(400, 319)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                            break
                    #红色购买
                    FinStr = dw.FindStrE(484, 122, 540, 309, '购买', "ff3232-000000", 1)
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
def 接收邮件():
        FinStr = dw.FindPicE(263, 462, 533, 551, "邮件.bmp|邮件1.bmp", "202020", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 3)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(3)
            FinStr = dw.FindStrE(338, 138, 419, 169, "邮件保管箱", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                time.sleep(1)
                xamo.UIKBudj(298, 465)
                time.sleep(1)
                xamo.PPWEbxbar(1)
                time.sleep(3)
                for i in range(10):
                    FinStr = dw.FindStrE(345, 275, 450, 308, "邮件领取完毕", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        break
                    time.sleep(1)
def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            return fp
def 近期制裁():
    FinStr = dw.FindStrE(812, 26, 1114, 114, "近期出现异常|制裁", "e6c89b-050505|ff3232-050505", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        num = get_ini("config/记录.ini", "刷号记录", "当前账号","")
        a = dw.Ocr(812, 26, 1114, 114, "e6c89b-050505|ff3232-050505", 1)
        if a.find('小时') > -1:
            arr = a.split('小时')
            temp_h = re.sub("\D", "", arr[0][-5:])
            d1 = datetime.datetime.now()
            # 制裁的小时+2
            # 转换成秒加到当前时间
            prints('制裁' + str(int(temp_h)) + '小时')
            log('制裁', account.hao, str(int(temp_h) + 2) + '小时')
            z_time = (int(temp_h) + 2) * 60 * 60
            delta = datetime.timedelta(seconds=z_time)
            n_days = d1 + delta
            set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
            prints("出现制裁,已记录制裁时间，换号")
            重启()
            time.sleep(2)
        else:
            d1 = datetime.datetime.now()
            # 也可以用days加天数,seconds加秒
            # 制裁时间无法识别，先加二小时
            delta = datetime.timedelta(seconds=7200)
            n_days = d1 + delta
            set_ini("config/记录.ini", "制裁", num, n_days.strftime("%Y-%m-%d %H:%M:%S"))
            prints("出现制裁等待一小时，换号")
            prints('近期制裁，请把文件夹中的截图发给作者')
            dw.Capture(812, 26, 1114, 114, os.getcwd() + '/' + str(time.time()) + '.bmp')
            重启()
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
        if d3.seconds > 10:
            jianqu_time = datetime.datetime.now()
            jianqucishu += 1
            if jianqucishu > 3:
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
        FinStr = dw.FindPicE(0,78,799,552,"捡1.bmp|捡2.bmp|捡3.bmp|捡4.bmp","050505","0.95",0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            time.sleep(0.1)
            xamo.KJDfekiHDh(88,1)
            time.sleep(0.5)
        else:
            FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 0.9, 0)
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
            FinStr = dw.FindPicE(0,78,799,552,"wp.bmp","000000","1",1)
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
        time.sleep(0.001)
def 判断方向(num):
    if num == 1:
        return "右"
    elif num == 2:
        return "右"
    elif num == 3:
        return "下"
    elif num == 4:
        FinStr = dw.FindPicE(755, 80, 778, 100, "问号.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            return "下"
        else:
            prints('关卡 = 4*')
            return "左"
    elif num == 5:
        return "右"
    elif num == 6:
        return "上"
    elif num == 8:
        return "右"
    elif num == 9:
        return "下"
def 特殊关卡():
    FinStr = dw.FindPicE(719,44,741,68, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 1
    FinStr = dw.FindPicE(733,47,756,67, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 2
    FinStr = dw.FindPicE(754,47,777,66, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 3
    FinStr = dw.FindPicE(755,63,777,85, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 4
    FinStr = dw.FindPicE(753,77,778,105, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 5
    FinStr = dw.FindPicE(767,80,797,104, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 6
    FinStr = dw.FindPicE(734,60,766,87, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 9
    FinStr = dw.FindPicE(732,82,763,104, "特殊关卡.bmp", "000000", 0.9, 0)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        return 8
    return 0
def 检查关卡():
    #第八关第九关为最左边的关卡正常不会走到那里
    x = [730, 748, 766, 766, 766, 784,784, 748, 748]
    y = [55, 55, 55, 73, 91, 91,74, 91, 74]
    for i in range(9):
        color = dw.GetColor(x[i],y[i])
        if color == "0000ff":
            return i + 1
    return 特殊关卡()
def 找门(guanqia,p,jianqu):
    #p = 0 正常的问号找门
    #p = 1 错关找门
    d1 = time.clock()
    my_x_py = 10
    my_y_py = 190
    wp_x_py = 12
    wp_y_py = 14
    z_g = 检查关卡()
    if guanqia == 0:
        guanqia = 检查关卡()
    fangxiang = 判断方向(guanqia)
    if fangxiang == "左":
        x,y,x1,y1 = 2,117,147,533
        pic = "左右门.bmp"
        wp_x_py = 0
        wp_y_py = 75
    elif fangxiang == "右":
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
        FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 0.9, 0)
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
        FinStr = dw.FindPicE(x,y,x1,y1,pic,"000000","0.9",0)
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
            FinStr = dw.FindPicE(0, 78, 799, 552, "wp.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                捡取()
        if p == 0:
            FinStr = dw.FindPicE(718,25,795,105, "问号.bmp", "000000", 0.9, 0)
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
        d2 = time.clock()
        d3 = d2 - d1
        if d3 > 20:
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
    my_y_py = 190
    wp_x_py = 12
    wp_y_py = 20
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
        FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = dw.FindPicE(0, 78, 799, 552, "可破坏.bmp", "000000", 0.9, 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            wp_x = int(pos[1])
            wp_y = int(pos[2])
        else:
            弹起()
            break
        if my_x > 0 and my_y > 0 and wp_x > 0 and wp_y > 0:
            FinStr = dw.FindPicE(my_x - 80, my_y + 125, my_x + 140, my_y + 200, "可破坏.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                FinStr = dw.FindPicE(530, 561, 562, 593, "鞭子.bmp|双翼风刃.bmp", "000000", 0.9, 0)
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
        temp_name = ['拉莫斯','桑德尔','牛头王','路易斯','伊伽贝拉','海伊伦','冰','火','光','暗']
        for i in range(len(temp_name)):
            xamo.KJDfekiHDh(jn_key[temp_name[i]],3)
            time.sleep(jn_sf_time[temp_name[i]])
            jn_now_time[temp_name[i]] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        xamo.KJDfekiHDh(40,1)
        xamo.KJDfekiHDh(38,1)
        xamo.KJDfekiHDh(32,1)

    elif leixing == 2:
        temp_name = ['伊伽贝拉','冰','火','光','暗','拉莫斯','海伊伦']
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
        FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = dw.FindColorE(0, 78, 799, 492, "0000ff-000000", 1.0, 5)
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
            FinStr = dw.FindPicE(0, 78, 799, 552, "wp.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                捡取()
        FinStr = dw.FindPicE(337, 29, 451, 97, "奖励.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
        FinStr = dw.FindPicE(612, 132, 735, 164, "通关.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
def 返回城镇():
    try:
        while True:
            FinStr = dw.FindStrE(451, 427, 535, 501, "返回城镇", "e6c89b-000000", 1)
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
    xamo.UIKBudj(random.randint(1,6), random.randint(1,6))
    time.sleep(0.2)
    xamo.PPWEbxbar(1)
    time.sleep(0.5)
    ql_time = time.clock()
    while True:
        ql_time_now = time.clock()
        time_temp = ql_time_now - ql_time
        if time_temp > 30:
            prints('清理窗口超时')
            return 0
        FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(594, 127)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            time.sleep(0.5)
            FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                xamo.UIKBudj(594, 127)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            else:
                break
            return 1
        else:
            xamo.UIKBudj(1, 1)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.KJDfekiHDh(27,1)
            time.sleep(0.5)
def 出售分解(ZZ):
    #参数说明0=出售,1=分解
    bz_is = int(get_ini('config/cfg.ini', '游戏配置', '白装处理',"0"))
    zz_is = int(get_ini('config/cfg.ini', '游戏配置', '紫装处理',"0"))
    fenjieshuliang = 0
    FinStr = dw.FindStrE(0, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
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
        FinStr = dw.FindStrE(397,390,690,552, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #装备需要修理自动弹出
            FinStr = dw.FindStrE(396, 218, 465, 352, "取消", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 5, inty + 3)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            time.sleep(1)
            #点击材料
            xamo.UIKBudj(592, 245)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            #检查无色数量
            dw.UseDict(2)   #切换到number.txt
            ws_sl = dw.Ocr(726, 374, 762, 386, "ffffff-000000", 1)
            dw.UseDict(0)   #切换回来
            ws_sl = re.sub("\D", "", ws_sl)
            if ws_sl != '':
                prints("无色数量 = " + ws_sl)
                if int(ws_sl) >= 1000:
                    bz_is = 0
            #点击装备栏
            xamo.UIKBudj(497, 245)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            #点击整理
            xamo.UIKBudj(840, 240)
            time.sleep(0.2)
            xamo.UIKBudj(699, 485)
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
                    elif aq_ret == 3:
                        return 3
                    Color = dw.GetColor(x + 5, y)
                    if Color == '4c9bad':
                        #高级装备
                        if bz_is == 0:
                            xamo.UIKBudj(x + 14, y + 14)
                            time.sleep(0.3)
                            for dj in range(2):
                                xamo.PPWEbxbar(1)
                                time.sleep(0.3)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        else:
                            fenjieshuliang += 1
                    elif Color == '656565' or Color == '874747' or Color == '766c79':
                        #普通装备
                        if bz_is == 0:
                            xamo.UIKBudj(x + 14, y + 14)
                            time.sleep(0.3)
                            for dj in range(2):
                                xamo.PPWEbxbar(1)
                                time.sleep(0.3)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        else:
                            fenjieshuliang += 1
                    elif Color == 'ab83f7' or Color == 'b85bac' or Color == 'c50086':
                        #紫色装备
                        if zz_is == 0:
                            xamo.UIKBudj(x + 14, y + 14)
                            time.sleep(0.3)
                            for dj in range(2):
                                xamo.PPWEbxbar(1)
                                time.sleep(0.3)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        else:
                            fenjieshuliang += 1
                    elif Color == 'be00c0' or Color == 'c3008e':
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
            FinStr = dw.FindPicE(92, 562, 120, 589, "hp.bmp", "000000", 0.9, 0)
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
                FinStr = dw.FindPicE(472, 257, 717, 469, "hp.bmp", "000000", 0.9, 0)
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
    if fenjieshuliang == 0:
        return 0
    FinStr = dw.FindStrE(0, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
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
        FinStr = dw.FindStrE(397,390,690,552, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(255, 350)
            time.sleep(1)
            FinStr = dw.FindStrE(323, 370, 335, 382, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                xamo.UIKBudj(323 + 7, 370 + 7)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
            FinStr = dw.FindStrE(323, 384, 335, 396, "勾选", "ffae00-000000", 1)
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
            FinStr = dw.FindStrE(316, 269, 480, 313, "缺少分解道具", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                清理游戏窗口()
                return 1
            else:
                xamo.KJDfekiHDh(13,1)
                time.sleep(4)
                aq_ret = 安全模式()
                if aq_ret == 3:
                    return 3
                清理游戏窗口()
                return 1
def 安全模式():
    FinStr = dw.FindStrE(335, 319, 396, 350, "确定解除", "ddc593-000000", 1)
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
            if xaoguo_return:
                prints('小果解除安全模式 成功')
                while True:
                    prints(account.hao + '|' + account.mi + "出现安全模式，等待小果解除")
                    time.sleep(5)
                    FinStr = dw.FindStrE(312, 272, 483, 295, "解除安全模式", "ffffff-000000", 1)
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
            aq_time = time.clock()
            while True:
                aq_time_now = time.clock()
                if aq_time_now - aq_time > 1200:
                    return 3
                prints(account.hao + '|' + account.mi + "出现安全模式，等待手动解除")
                time.sleep(5)
                FinStr = dw.FindStrE(312, 272, 483, 295, "解除安全模式", "ffffff-000000", 1)
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
def 移动(can):
    #can == 1 格蓝迪 can == 2 黄龙
    prints('移动')
    coumai_index = 0
    检查累积在线奖励()
    if can == 1:
        prints('曼斯工业基地 --> 格兰迪门口')
        index = 0
        yd_time = time.clock()
        while True:
            yd_time_now = time.clock()
            if yd_time_now - yd_time > 300:
                弹起()
                return 0
            time.sleep(0.2)
            if index == 0:
                向下()
                time.sleep(5)
                弹起()
                清理游戏窗口()
                FinStr = dw.FindStrE(652, 26, 743, 52, "斯曼工业基地", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    向右()
                    time.sleep(1)
                    弹起()
                    向上()
                    time.sleep(1)
                    弹起()
                    index = 1
                else:
                    FinStr = dw.FindStrE(652, 26, 743, 52, "克洛诺斯岛", "e6c89b-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        time.sleep(1)
                        index = 2.1
                    else:
                        while True:
                            FinStr = dw.FindStrE(430, 366, 588, 586, "重", "e6c89b-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                time.sleep(0.5)
                                xamo.UIKBudj(544, 247)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                xamo.UIKBudj(595, 172)
                                time.sleep(0.5)
                                FinStr = dw.FindPicE(474, 262, 715, 469, "瞬间移动药剂.bmp", "000000", 0.9, 0)
                                pos = FinStr.split('|')
                                if int(pos[1]) > 0:
                                    xamo.UIKBudj(int(pos[1]), int(pos[2]))
                                    xamo.XKkncvhe(1)
                                    time.sleep(1)
                                    # 选择地图
                                    xamo.UIKBudj(371, 325)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(2)
                                    # 世界
                                    xamo.UIKBudj(187, 37)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(1)
                                    # 伊顿工业区
                                    xamo.UIKBudj(169, 155)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(1)
                                    # 格蓝迪入口
                                    xamo.UIKBudj(497, 462)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(1)
                                    # 传送
                                    xamo.UIKBudj(372, 325)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(4)
                                    清理游戏窗口()
                                    break
                                else:
                                    xamo.KJDfekiHDh(73, 1)
                                    time.sleep(0.5)
                                    购买物品('瞬间移动药剂', 1)
                                    coumai_index += 1
                                    if coumai_index > 5:
                                        prints('购买次数超限')
                                        return 0
                                    清理游戏窗口()
                                    接收邮件()
                                    清理游戏窗口()
                            else:
                                xamo.KJDfekiHDh(73, 1)
                                time.sleep(1)
                        break
            elif index == 1:
                右上()
                FinStr = dw.FindStrE(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    break
            elif index == 2.1:
                左上()
                FinStr = dw.FindStrE(660, 26, 743, 52, "斯曼工业基地", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    向下()
                    time.sleep(1)
                    弹起()
                    index = 2.2
            elif index == 2.2:
                左上()
                FinStr = dw.FindPicE(0, 16, 521, 234, "地图中转.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    index = 2.3
            elif index == 2.3:
                向右()
                FinStr = dw.FindStrE(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    break
    elif can == 2:
        prints('素喃 --> 黄龙门口')
        index = 0
        yd_time = time.clock()
        while True:
            yd_time_now = time.clock()
            if yd_time_now - yd_time> 300:
                弹起()
                return 0
            time.sleep(0.2)
            if index == 0:
                向下()
                time.sleep(5)
                清理游戏窗口()
                FinStr = dw.FindStrE(658, 24, 751, 53, "素喃", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    index = 1
                else:
                    弹起()
                    while True:
                        FinStr = dw.FindStrE(430, 366, 588, 586, "重", "e6c89b-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            time.sleep(0.5)
                            xamo.UIKBudj(544, 247)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(1)
                            xamo.UIKBudj(595, 172)
                            time.sleep(0.5)
                            FinStr = dw.FindPicE(474, 262, 715, 469, "瞬间移动药剂.bmp", "000000", 0.9, 0)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                xamo.UIKBudj(int(pos[1]), int(pos[2]))
                                xamo.XKkncvhe(1)
                                time.sleep(1)
                                #选择地图
                                xamo.UIKBudj(371, 325)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(2)
                                #世界
                                xamo.UIKBudj(187, 37)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                #素喃
                                xamo.UIKBudj(155, 107)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                #黄龙入口
                                xamo.UIKBudj(379, 275)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                #传送
                                xamo.UIKBudj(372, 325)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(4)
                                清理游戏窗口()
                                break
                            else:
                                xamo.KJDfekiHDh(73, 1)
                                time.sleep(0.5)
                                购买物品('瞬间移动药剂',1)
                                coumai_index += 1
                                if coumai_index > 5:
                                    prints('购买次数超限')
                                    return 0
                                清理游戏窗口()
                                接收邮件()
                                清理游戏窗口()
                        else:
                            xamo.KJDfekiHDh(73, 1)
                            time.sleep(1)
                    break
            if index == 1:
                左上()
                FinStr = dw.FindPicE(7, 76, 607, 383, "地图中转2.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    index = 2
            if index == 2:
                右下()
                FinStr = dw.FindStrE(70, 85, 605, 367, "装备分解", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    break
    elif can == 3:
        prints('素喃 --> 小铁柱')
        index = 0
        yd_time = time.clock()
        while True:
            yd_time_now = time.clock()
            if yd_time_now - yd_time > 300:
                弹起()
                return 0
            time.sleep(0.2)
            if index == 0:
                向下()
                time.sleep(5)
                清理游戏窗口()
                FinStr = dw.FindStrE(658, 24, 751, 53, "素喃", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    index = 1
                else:
                    弹起()
                    while True:
                        FinStr = dw.FindStrE(430, 366, 588, 586, "重", "e6c89b-000000", 1)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            time.sleep(0.5)
                            xamo.UIKBudj(544, 247)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(1)
                            xamo.UIKBudj(595, 172)
                            time.sleep(0.5)
                            FinStr = dw.FindPicE(474, 262, 715, 469, "瞬间移动药剂.bmp", "000000", 0.9, 0)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                xamo.UIKBudj(int(pos[1]), int(pos[2]))
                                xamo.XKkncvhe(1)
                                time.sleep(1)
                                #选择地图
                                xamo.UIKBudj(371, 325)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(2)
                                #世界
                                xamo.UIKBudj(187, 37)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                #素喃
                                xamo.UIKBudj(155, 107)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                #小铁匠
                                xamo.UIKBudj(387, 406)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(1)
                                #传送
                                xamo.UIKBudj(372, 325)
                                time.sleep(0.2)
                                xamo.PPWEbxbar(1)
                                time.sleep(4)
                                清理游戏窗口()
                                break
                            else:
                                xamo.KJDfekiHDh(73, 1)
                                time.sleep(0.5)
                                购买物品('瞬间移动药剂',1)
                                coumai_index += 1
                                if coumai_index > 5:
                                    prints('购买次数超限')
                                    return 0
                                清理游戏窗口()
                                接收邮件()
                                清理游戏窗口()
                        else:
                            xamo.KJDfekiHDh(73, 1)
                            time.sleep(1)
                    break
            if index == 1:
                左下()
                FinStr = dw.FindPicE(88, 84, 354, 479, "地图中转3.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    index = 2
            if index == 2:
                右下()
                FinStr = dw.FindStrE(290, 86, 522, 403, "武器锻造", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    break
    elif can == 4:
        prints('小铁柱 --> 黄龙门口')
        index = 0
        yd_time = time.clock()
        while True:
            yd_time_now = time.clock()
            if yd_time_now - yd_time > 300:
                弹起()
                return 0
            time.sleep(0.2)
            if index == 0:
                左上()
                FinStr = dw.FindPicE(96, 84, 676, 349, "地图中转4.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    index = 1
            if index == 1:
                右上()
                FinStr = dw.FindStrE(70, 85, 605, 367, "装备分解", "e6c89b-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    弹起()
                    向下()
                    time.sleep(3)
                    弹起()
                    break
    return 1
def 点击技能(x, y, x1, y1,is_tuodong,t,back = 0):
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
    time.sleep(0.5)
    if back > 0:
        for ba in range(back):
            xamo.UIKBudj(x, y)
            time.sleep(0.2)
            xamo.XKkncvhe(1)
            time.sleep(0.5)
    if is_tuodong:
        if t != 0:
            #拖动技能
            xamo.UIKBudj(x + 3, y + 3)
            time.sleep(0.2)
            xamo.cndjGdsbSdg()
            time.sleep(0.2)
            xamo.UIKBudj(x + 5, y + 5)
            time.sleep(0.2)
            xamo.UIKBudj(x1, y1)
            time.sleep(0.2)
            xamo.UIKBudj(x1+3, y1+3)
            time.sleep(0.2)
            xamo.mboHdjGsV()
            time.sleep(0.2)
def 清理游戏窗口_学技能():
    xamo.UIKBudj(1, 1)
    time.sleep(0.5)
    xamo.PPWEbxbar(1)
    time.sleep(0.5)
    ql_time = time.clock()
    while True:
        ql_time_now = time.clock()
        time_temp = ql_time_now - ql_time
        if time_temp > 30:
            return 0
        FinStr = dw.FindStrE(378,296,494,369, "关闭", "ddc593-000000|ffffb8-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 3)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(594, 127)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            time.sleep(0.5)
            FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                xamo.UIKBudj(594, 127)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            else:
                break
            return 1
        else:
            xamo.UIKBudj(1, 1)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.KJDfekiHDh(27,1)
            time.sleep(1)
def 学习技能(zhiye):
    prints('学习技能,职业 = ' +str(zhiye))
    is_tp = True
    for t in range(3):
        is_wz = True
        if zhiye == 2: #风法
            #检查技能摆放
            for i in range(12):
                FinStr = dw.FindPicE(528, 523, 715, 593, "风法技能" + str(i + 1) + ".bmp", "050505", 1.0, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    pass
                else:
                    is_wz = False
                    is_tp = False
                    break
            if not is_wz:
                jn_time = time.clock()
                while True:
                    jn_time_now = time.clock()
                    if jn_time_now - jn_time > 180:
                        prints('学习技能超时')
                        return 0
                    FinStr = dw.FindStrE(376, 28, 429, 51, "技能栏", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        FinStr = dw.FindPicE(2, 51, 111, 178, "电视.bmp", "000000", 0.9, 0)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            intx = int(pos[1])
                            inty = int(pos[2])
                            time.sleep(1)
                            xamo.UIKBudj(intx, inty)
                            time.sleep(0.2)
                            xamo.cndjGdsbSdg()
                            time.sleep(0.2)
                            xamo.UIKBudj(15, 28)
                            time.sleep(0.2)
                            xamo.mboHdjGsV()
                            time.sleep(2)
                        #选中SP技能
                        xamo.UIKBudj(19, 104)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(3)
                        time.sleep(0.5)
                        # 关闭学习技能帮助界面
                        FinStr = dw.FindStrE(24, 132, 89, 164, "学习技能", "ffee88-000000", 1)
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
                        #第一次初始化技能
                        if t == 0:
                            xamo.UIKBudj(508, 105)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(2)
                            time.sleep(1)
                            xamo.UIKBudj(362, 327)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(2)
                            time.sleep(1)
                            xamo.UIKBudj(400, 318)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(2)
                            time.sleep(1)
                            prints('技能初始化成功')
                        #物理暴击
                        点击技能(224, 141, 0, 0, False,t)
                        #物理背击
                        点击技能(304, 141, 0, 0, False,t)
                        #流风决
                        点击技能(285, 475, 771, 571, True,t)
                        #棍棒精通
                        点击技能(426, 410, 0, 0, False,t)
                        for temp in range(20):
                            FinStr = dw.FindStrE(4, 257, 27, 273, "30", "8c8c8c-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                break
                            else:
                                FinStr = dw.FindStrE(4, 389, 27, 409, "40", "8c8c8c-000000", 1)
                                pos = FinStr.split('|')
                                if int(pos[1]) > 0:
                                    break
                                else:
                                    xamo.UIKBudj(547, 517)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(0.5)
                        #凤鸣冲击
                        点击技能(239, 209, 672, 571, True,t,10)
                        #游离之风
                        点击技能(332, 210, 638, 571, True,t,10)
                        #双翼风刃
                        点击技能(333, 277, 605, 571, True,t)
                        #风暴之眼
                        点击技能(333, 343, 605, 536, True,t)
                        #真空旋风破
                        点击技能(287, 410, 705, 571, True,t)
                        #风暴之拳
                        点击技能(191, 477, 738, 571, True,t)
                        for temp in range(8):
                            xamo.UIKBudj(547, 517)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        #万象风龙阵
                        点击技能(239, 274, 736, 536, True,t)
                        #御风之力
                        点击技能(331, 274, 0, 0, False,t)
                        #风神决
                        点击技能(191, 411, 0, 0, False,t)
                        #风卷残云
                        点击技能(285, 411, 672, 536, True,t)
                        #游龙惊风破
                        点击技能(333, 411, 640, 539, True,t)
                        #九霄风雷
                        点击技能(191, 476, 704, 536, True,t)
                        #无限风域
                        点击技能(379, 476, 771, 536, True,t)
                        time.sleep(1)
                        #学习
                        xamo.UIKBudj(209, 553)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        #确认
                        xamo.UIKBudj(362, 320)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        xamo.UIKBudj(362, 320)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        ret_ql = 清理游戏窗口_学技能()
                        if ret_ql == 0:
                            return 0
                        break
                    else:
                        xamo.KJDfekiHDh(75,1)
                        time.sleep(1)
        elif zhiye == 1: #召唤
            #检查技能摆放
            for i in range(12):
                FinStr = dw.FindPicE(528, 523, 715, 593, "召唤技能" + str(i + 1) + ".bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    pass
                else:
                    is_wz = False
                    is_tp = False
                    break
            if not is_wz:
                jn_time = time.clock()
                while True:
                    jn_time_now = time.clock()
                    if jn_time_now - jn_time > 180:
                        prints('学习技能超时')
                        return 0
                    FinStr = dw.FindStrE(376, 28, 429, 51,  "技能栏", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        time.sleep(1)
                        #关闭学习技能帮助界面
                        FinStr = dw.FindStrE(24, 132, 89, 164, "学习技能", "ffee88-000000", 1)
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
                        #第一次初始化技能
                        if t == 0:
                            xamo.UIKBudj(508, 105)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(2)
                            time.sleep(1)
                            xamo.UIKBudj(362, 327)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(2)
                            time.sleep(1)
                            xamo.UIKBudj(400, 318)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(2)
                            time.sleep(1)
                            prints('技能初始化成功')
                        #魔法暴击
                        点击技能(265, 141, 0, 0, False,t)
                        #魔法背击
                        点击技能(346, 141, 0, 0, False,t)
                        #鞭子
                        点击技能(238, 338, 605, 571, True,t)
                        #召唤兽强化
                        点击技能(285, 410, 0, 0, False,t)
                        for temp in range(20):
                            FinStr = dw.FindStrE(2,255,28,274, "30", "8c8c8c-000000", 1)
                            pos = FinStr.split('|')
                            if int(pos[1]) > 0:
                                break
                            else:
                                FinStr = dw.FindStrE(4,388,26,409, "40", "8c8c8c-000000", 1)
                                pos = FinStr.split('|')
                                if int(pos[1]) > 0:
                                    break
                                else:
                                    xamo.UIKBudj(547, 517)
                                    time.sleep(0.2)
                                    xamo.PPWEbxbar(1)
                                    time.sleep(0.5)
                        #桑德尔
                        点击技能(426, 209, 638, 539, True,t)
                        #狂化
                        点击技能(379, 274, 769, 539, True,t)
                        #冰
                        点击技能(49, 274, 670, 571, True,t)
                        #火
                        点击技能(97, 274, 703, 571, True,t)
                        #光
                        点击技能(143, 274, 737, 571, True,t)
                        #暗
                        点击技能(191, 274, 770, 571, True,t)
                        #路易斯
                        点击技能(426, 341, 704, 539, True,t)
                        #伊伽贝拉
                        点击技能(285, 411, 737, 539, True,t)
                        #牛王
                        点击技能(427, 475, 671, 539, True,t)
                        for temp in range(6):
                            xamo.UIKBudj(547, 517)
                            time.sleep(0.2)
                            xamo.PPWEbxbar(1)
                            time.sleep(0.5)
                        #灵魂支配
                        点击技能(332, 275, 0, 0, False,t)
                        #融合精灵
                        点击技能(143, 344, 638, 571, True,t)
                        #蚀月附灵
                        点击技能(98, 409, 0, 0, False,t)
                        #融合精灵
                        点击技能(239, 476, 605, 539, True,t)
                        time.sleep(1)
                        #学习
                        xamo.UIKBudj(209, 553)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                        #确认
                        xamo.KJDfekiHDh(13,1)
                        time.sleep(1)
                        ret_ql = 清理游戏窗口()
                        if ret_ql == 0:
                            return 0
                        break
                    else:
                        xamo.KJDfekiHDh(75,1)
                        time.sleep(1)
    if not is_tp:
        if zhiye == 1:
            jn_time = time.clock()
            while True:
                jn_time_now = time.clock()
                if jn_time_now - jn_time > 120:
                    prints('学习TP能超时')
                    return 0
                FinStr = dw.FindStrE(376, 28, 429, 51, "技能栏", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    # TP技能学习
                    xamo.UIKBudj(208, 104)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    # 强化-牛头王
                    点击技能(145, 476, 0, 0, False, 0)
                    # 强化-精灵王
                    点击技能(96, 476, 0, 0, False, 0)
                    # 强化-路易斯
                    点击技能(49, 476, 0, 0, False, 0)
                    # 强化-桑德尔
                    点击技能(191, 342, 0, 0, False, 0)
                    time.sleep(1)
                    # 学习
                    xamo.UIKBudj(209, 553)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    # 确认
                    xamo.UIKBudj(362, 320)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    xamo.UIKBudj(362, 320)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    ret_ql = 清理游戏窗口_学技能()
                    if ret_ql == 0:
                        return 0
                    break
                else:
                    xamo.KJDfekiHDh(75, 1)
                    time.sleep(1)
        elif zhiye == 2:
            jn_time = time.clock()
            while True:
                jn_time_now = time.clock()
                if jn_time_now - jn_time > 120:
                    prints('学习TP能超时')
                    return 0
                FinStr = dw.FindStrE(376, 28, 429, 51, "技能栏", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    # TP技能学习
                    xamo.UIKBudj(208, 104)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    # 强化-风暴之拳
                    点击技能(424, 340, 0, 0, False, 0)
                    # 强化-风暴之眼
                    点击技能(330, 340, 0, 0, False, 0)
                    # 强化-双翼之风
                    点击技能(285, 340, 0, 0, False, 0)
                    # 强化-游离之风
                    点击技能(143, 340, 0, 0, False, 0)
                    time.sleep(1)
                    # 学习
                    xamo.UIKBudj(209, 553)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    # 确认
                    xamo.UIKBudj(362, 320)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    xamo.UIKBudj(362, 320)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    ret_ql = 清理游戏窗口_学技能()
                    if ret_ql == 0:
                        return 0
                    break
                else:
                    xamo.KJDfekiHDh(75, 1)
                    time.sleep(1)
    return 1
def 检查负重():
    for i in range(10):
        FinStr = dw.FindStrE(430, 366, 588, 586, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(0.5)
            intx = int(pos[1])
            inty = int(pos[2])
            color = dw.GetColor(intx + 120, inty + 1)
            if color == 'ad9494':
                xamo.KJDfekiHDh(73, 1)
                return 1
            elif color == '101010':
                xamo.KJDfekiHDh(73, 1)
                return 0
            else:
                xamo.KJDfekiHDh(73, 1)
                return 1
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(1)
    return 0
def 检查物品数量(wp_tab,name,num):
    for i in range(10):
        FinStr = dw.FindStrE(430, 366, 588, 586, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(0.5)
            intx = int(pos[1])
            inty = int(pos[2])
            if wp_tab == 1:
                xamo.UIKBudj(intx + 20, inty - 235)
            elif wp_tab == 2:
                xamo.UIKBudj(intx + 67, inty - 235)
            elif wp_tab == 3:
                xamo.UIKBudj(intx + 115, inty - 235)
            elif wp_tab == 4:
                xamo.UIKBudj(intx + 162, inty - 235)
            elif wp_tab == 5:
                xamo.UIKBudj(intx + 212, inty - 235)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            xamo.UIKBudj(595, 172)
            time.sleep(0.5)
            FinStr = dw.FindPicE(474, 262, 769, 469, name + ".bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                wp_sl = dw.Ocr(int(pos[1]) - 4, int(pos[2]) - 10, int(pos[1]) + 22, int(pos[2]),"ffffff-000000", 1)
                if wp_sl != '':
                    wp_sl = re.sub("\D", "", wp_sl)
                    if int(wp_sl) >= num:
                        return 1
                    else:
                        return int(wp_sl)
                else:
                    return 2
            else:
                return 2
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(1)
    return 0
def 检查累积在线奖励():
    FinStr = dw.FindStrE(148,11, 418, 72, "累计在线得好礼", "ffc800-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        intx = int(pos[1])
        inty = int(pos[2])
        xamo.UIKBudj(intx + 23, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 74, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 126, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 179, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 179, inty + 78)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 23, inty + 183)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 74, inty + 183)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 126, inty + 183)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 179, inty + 183)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
        xamo.UIKBudj(intx + 179, inty + 183)
        time.sleep(0.2)
        xamo.PPWEbxbar(1)
        time.sleep(0.2)
def 输入汉字(str):
    x = int(get_ini('config/cfg.ini', '主配置', 'x', "0"))
    y = int(get_ini('config/cfg.ini', '主配置', 'y', "0"))
    Imsrf = False
    for i in range(10):
        FinStr = dw.FindPicE(0, y - 42, x, y, "搜狗_图标1.bmp|搜狗_图标2.bmp|搜狗_图标3.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            Imsrf = not Imsrf
            break
        else:
            time.sleep(2)
            xamo.LKDFemrrh(17)
            xamo.KJDfekiHDh(16,1)
            xamo.LJDFnmeFSD(17)
            time.sleep(2)
    if not Imsrf:
        prints('未安装搜狗输入法或隐藏了右下角小任务栏')
        input()
    if str == '瞬间移动药剂':
        xamo.LbferJhd('sjydyj')
    elif str == '//移动物品':
        xamo.LbferJhd('ydwp')
    else:
        xamo.LbferJhd(str)
    time.sleep(0.5)
    xamo.KJDfekiHDh(49,1)
    time.sleep(0.5)
    #关闭输入法
    xamo.LKDFemrrh(17)
    xamo.KJDfekiHDh(16, 1)
    xamo.LJDFnmeFSD(17)
    time.sleep(0.5)
def 购买物品(name,num):
    prints('购买物品')
    prints('购买' + str(num) + '个' + name)
    shuliang = num
    gmwp_time = datetime.datetime.now()
    while True:
        gmwp_time_now = datetime.datetime.now()
        d3 = gmwp_time_now - gmwp_time
        if d3.seconds > 200:
            弹起()
            return 0
        FinStr = dw.FindStrE(609, 75, 669, 110, "默认设置", "ddc593-000000", 1)
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
            输入汉字(name)
            time.sleep(1)
            Fok = False
            for i in range(20):
                FinStr = dw.FindStrE(483, 115, 544, 497, "一口价", "ffb400-000000|ff3232-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    Fok = True
                    #从第五个开始购买
                    xamo.UIKBudj(614, 278)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    #一口价
                    xamo.UIKBudj(614 + 52, 278 + 33)
                    time.sleep(0.5)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    FinStr = dw.FindStrE(474, 104, 761, 531, "数量", "ffe3ab-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        wp_sl = dw.Ocr(int(pos[1]) + 24, int(pos[2]) - 3, int(pos[1]) + 80, int(pos[2]) + 16, "ffe3ab-000000", 1)
                        if wp_sl != '':
                            wp_sl = re.sub("\D", "", wp_sl)
                            if int(wp_sl) > shuliang:
                                ls_sl = shuliang
                                xamo.LbferJhd(str(shuliang))
                            else:
                                ls_sl = int(wp_sl)
                        else:
                            return 0
                    else:
                        return 0
                    xamo.KJDfekiHDh(13, 2)
                    time.sleep(3)
                    aq_ret = 安全模式()
                    if aq_ret == 1:
                        return 0
                    elif aq_ret == 3:
                        return 0
                    FinStr = dw.FindStrE(278, 251, 507, 343, "所持金币不足", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        prints('金币不足，等待60秒，筹够钱后回到这个界面')
                        time.sleep(60)
                    FinStr = dw.FindStrE(308, 233, 490, 354, "完成竞拍", "ffffff-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        xamo.KJDfekiHDh(13, 1)
                        shuliang = shuliang - ls_sl
                        prints('还需要购买' + str(shuliang) + '个')
                        if shuliang <= 0:
                            return 1
                    else:
                        xamo.KJDfekiHDh(13, 1)
                    # 搜索
                    xamo.UIKBudj(589, 89)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(3)
                else:
                    # 搜索
                    xamo.UIKBudj(589, 89)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(3)
                gmwp_time_now = datetime.datetime.now()
                d3 = gmwp_time_now - gmwp_time
                if d3.seconds > 200:
                    弹起()
                    return 0
            if not Fok:
                return 0
        else:
            #按B打开拍卖行
            xamo.KJDfekiHDh(66,1)
            time.sleep(1)
def 购买免修黄金牌(p):
    if p == 1:
        prints('检查自动修理')
    elif p == 2:
        prints('检查黄金翻牌')
    ret_ql = 清理游戏窗口()
    if ret_ql == 0:
        return 0
    gmmx_time = time.clock()
    while True:
        FinStr = dw.FindPicE(240, 490, 550, 620, "服务列表.bmp", "000000", 0.9, 0)
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
        FinStr = dw.FindStrE(191, 99, 647, 276, "优惠券礼盒", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if p == 1:
                FinStr = dw.FindStrE(140, 158, 615, 501, "自动修理", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    return 1
                else:
                    break
            elif p == 2:
                FinStr = dw.FindStrE(140, 158, 615, 501, "黄金卡牌免费翻", "ffffff-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    return 1
                else:
                    break
        gmmx_time_now = time.clock()
        d3 = gmmx_time_now - gmmx_time
        if d3 > 300:
            return 0
    ret_ql = 清理游戏窗口()
    if ret_ql == 0:
        return 0
    prints('购买自动修理')
    while True:
        FinStr = dw.FindStrE(92, 540, 171, 579, "积分", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            number = dw.Ocr(325, 547, 410, 570, "ffffff-000000", 1)
            number = re.sub("\D", "", number)
            if int(number) >= 500:
                break
            else:
                if p == 1:
                    prints('点券不够购买免修服务请充值*500')
                elif p == 2:
                    prints('点券不够购买黄金卡牌服务请充值*500')
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
        gmmx_time_now = time.clock()
        d3 = gmmx_time_now - gmmx_time
        if d3 > 600:
            return 0
    gmmx_time = time.clock()
    while True:
        time.sleep(0.2)
        gmmx_time_now = time.clock()
        d3 = gmmx_time_now - gmmx_time
        if d3 > 100:
            return 0
        FinStr = dw.FindStrE(425, 40, 720, 79, "装饰类", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #点击优惠类
            xamo.UIKBudj(481, 58)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            for tn in range(3):
                FinStr = dw.FindStrE(17, 107, 419, 527, "魔王之契约", "ffffff-000000", 1)
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
            xamo.UIKBudj(365, 23)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.FindStrE(370, 98, 431, 122, "结算窗口", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if p == 1:
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
            elif p == 2:
                #取消自动修理
                xamo.UIKBudj(407, 183)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                #选择黄金卡牌免费翻
                xamo.UIKBudj(407, 328)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                # 点击下拉
                xamo.UIKBudj(428, 348)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                # 选择30天
                xamo.UIKBudj(224, 381)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            #购买
            xamo.UIKBudj(503, 476)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(2)
            xamo.KJDfekiHDh(13,1)
            time.sleep(1)
            ret_ql = 清理游戏窗口()
            if ret_ql == 0:
                return 0
            break
def boss关捡取():
    xamo.KJDfekiHDh(86,1)
    time.sleep(1)
    for ic in range(10):
        xamo.KJDfekiHDh(88,1)
        time.sleep(0.2)
def 打怪_风法(GK):
    my_x_py = 10
    my_y_py = 170
    gw_x_py = 28
    gw_y_py = 30
    jl_x = 300
    jl_y = 60
    dgff_time = time.clock()
    while True:
        my_x = 0
        my_y = 0
        gw_x = 0
        gw_y = 0
        dgff_time_now = time.clock()
        d3 = dgff_time_now - dgff_time
        if d3 > 30:
            break
        FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 1.0, 0)
        pos = FinStr.split('|')
        if int(pos[1]) >= 0:
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
        FinStr = dw.FindColorE(0, 78, 799, 552, "ff0094-101010|ff00ff-101010", 1.0, 0)
        pos = FinStr.split('|')
        if int(pos[0]) >= 0:
            gw_x = int(pos[0])
            gw_y = int(pos[1])
        else:
            弹起()
            break
        if my_x >= 0 and my_y >= 0 and gw_x >= 0 and gw_y >= 0:
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
                    if GK == 7:
                        x = 533
                        y = 533
                        for c in range(4):
                            FinStr = dw.FindColorE(x, y, x + 22, y + 20, "ffffff-000000", 1.0, 0)
                            pos = FinStr.split('|')
                            if int(pos[0]) >= 0:
                                pass
                            else:
                                if c == 0:
                                    xamo.KJDfekiHDh(81, 1)
                                    time.sleep(0.5)
                                    break
                                elif c == 1:
                                    xamo.KJDfekiHDh(87, 1)
                                    time.sleep(0.5)
                                    break
                                elif c == 2:
                                    xamo.KJDfekiHDh(69, 1)
                                    time.sleep(0.5)
                                    break
                                elif c == 3:
                                    xamo.KJDfekiHDh(82, 1)
                                    time.sleep(0.5)
                                    break
                            x += 30
                    FinStr = dw.FindPicE(531, 561, 715, 596, "双翼风刃.bmp|游离之风.bmp|凤鸣冲击.bmp|真空旋风破.bmp", "000000", 0.9, 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) >= 0:
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
        time.sleep(0.001)
def 设置():
    prints('设置')
    sz_time = time.clock()
    while True:
        sz_time_now = time.clock()
        d3 = sz_time_now - sz_time
        if d3 > 100:
            弹起()
            return 0
        FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(279, 442)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            break
        else:
            xamo.KJDfekiHDh(27,1)
            time.sleep(1)
    sz_time = time.clock()
    while True:
        sz_time_now = time.clock()
        d3 = sz_time_now - sz_time
        if d3 > 100:
            弹起()
            return 0
        FinStr = dw.FindStrE(163, 421, 260, 478, "快捷键设置", "ddcc99-000000|ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(1)
            for temp_i in range(12):
                xamo.UIKBudj(635, 419)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
            FinStr = dw.FindStrE(389, 361, 476, 387, "查看全身时装", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                for temp_i in range(12):
                    FinStr = dw.FindStrE(257,206,522,389, "勾选", "ffae00-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 1, inty + 1)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.2)
                        xamo.UIKBudj(224, 309)
                        time.sleep(0.2)
                #特效低
                xamo.UIKBudj(287, 294)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                #技能透明
                xamo.UIKBudj(281, 396)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
                xamo.UIKBudj(281, 415)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(0.5)
            else:
                break
            xamo.UIKBudj(370, 445)
            time.sleep(0.2)
            xamo.PPWEbxbar(2)
            time.sleep(5)
            break
    sz_time = time.clock()
    while True:
        sz_time_now = time.clock()
        d3 = sz_time_now - sz_time
        if d3 > 100:
            弹起()
            return 0
        FinStr = dw.FindStrE(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            xamo.UIKBudj(279, 442)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            break
        else:
            xamo.KJDfekiHDh(27,1)
            time.sleep(1)
    while True:
        sz_time_now = time.clock()
        d3 = sz_time_now - sz_time
        if d3 > 100:
            弹起()
            return 0
        FinStr = dw.FindStrE(163, 421, 260, 478, "快捷键设置", "ddcc99-000000|ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 10, inty + 3)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.FindStrE(328, 296, 418, 346, "聊天快捷键", "96ff1e-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            #恢复默认
            xamo.UIKBudj(116, 512)
            time.sleep(0.2)
            xamo.PPWEbxbar(2)
            time.sleep(1)
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
            输入汉字('//移动物品')
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
def 上架礼盒():
    sjlh_time = time.clock()
    while True:
        FinStr = dw.FindStrE(609, 75, 669, 110, "默认设置", "ddc593-000000", 1)
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
        sjlh_time_now = time.clock()
        d3 = sjlh_time_now - sjlh_time
        if d3 > 100:
            return 0
    sjlh_time = time.clock()
    while True:
        FinStr = dw.FindStrE(215, 448, 267, 473, "竞拍价", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #点击消耗栏
            xamo.UIKBudj(543, 246)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            FinStr = dw.FindPicE(466, 252, 721, 420, "浪漫心动礼盒.bmp", "000000", 0.9, 0)
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
        sjlh_time_now = time.clock()
        d3 = sjlh_time_now - sjlh_time
        if d3 > 200:
            return 0
    sjlh_time = time.clock()
    while True:
        sjlh_time_now = time.clock()
        d3 = sjlh_time_now - sjlh_time
        if d3 > 200:
            return 0
        FinStr = dw.FindStrE(317, 328, 356, 425, "每个", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            number = dw.Ocr(314, 376, 441, 393, "ddc593-000000", 1)
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
            elif aq_ret == 3:
                return 0
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
        FinStr = dw.FindPicE(0, 78, 799, 552, "图内验证1.bmp|图内验证2.bmp|图内验证3.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            prints('出现图内验证')
            CRuser = get_ini('config/cfg.ini', '主配置', '若快账号', "")
            CRpwd = get_ini('config/cfg.ini', '主配置', '若快密码', "")
            xx = int(pos[1])
            yy = int(pos[2])
            dw.CaptureJpg(xx - 45, yy - 145, xx + 74, yy - 85, os.getcwd() + "/ver.jpg", 20)
            with open(os.getcwd() + "/ver.jpg", 'rb') as f:
                im = f.read()
            time.sleep(0.5)
            dc = rk.RClient(CRuser, CRpwd, "16589", "d47ebffa337e6900f3d4b12e8c1214ce")
            yzm = dc.rk_create(im, "2040")
            xy = yzm["Result"]
            prints('返回结果 = ' + xy)
            xamo.UIKBudj(xx + 201, yy - 110)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            for tn in range(5):
                xamo.KJDfekiHDh(8, 1)
                time.sleep(0.2)
            xamo.LbferJhd(xy)
            time.sleep(0.5)
            xamo.UIKBudj(xx + 20, yy + 10)
            time.sleep(0.5)
            xamo.PPWEbxbar(2)
            time.sleep(2)
        if zhiye == 1:
            技能(1)
            time.sleep(1)
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.8)
            xamo.KJDfekiHDh(89, 1)
            time.sleep(1)
        elif zhiye == 2:
            # 流风决 右 右 空格
            time.sleep(1)
            xamo.KJDfekiHDh(72, 1)
            time.sleep(0.5)
            向右()
            time.sleep(0.5)
            弹起()
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 1)
            time.sleep(0.5)
            # 双翼风刃 A
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.2)
            # 游离之风 S
            xamo.KJDfekiHDh(83, 1)
            time.sleep(0.2)
        FinStr = dw.FindPicE(0, 78, 799, 552, "图内验证1.bmp|图内验证2.bmp|图内验证3.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            prints('出现图内验证')
            CRuser = get_ini('config/cfg.ini', '主配置', '若快账号', "")
            CRpwd = get_ini('config/cfg.ini', '主配置', '若快密码', "")
            xx = int(pos[1])
            yy = int(pos[2])
            dw.CaptureJpg(xx - 45, yy - 145, xx + 74, yy - 85, os.getcwd() + "/ver.jpg", 20)
            with open(os.getcwd() + "/ver.jpg", 'rb') as f:
                im = f.read()
            time.sleep(0.5)
            dc = rk.RClient(CRuser, CRpwd, "16589", "d47ebffa337e6900f3d4b12e8c1214ce")
            yzm = dc.rk_create(im, "2040")
            xy = yzm["Result"]
            prints('返回结果 = ' + xy)
            xamo.UIKBudj(xx + 201, yy - 110)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            for tn in range(5):
                xamo.KJDfekiHDh(8, 1)
                time.sleep(0.2)
            xamo.LbferJhd(xy)
            time.sleep(0.5)
            xamo.UIKBudj(xx + 20, yy + 10)
            time.sleep(0.5)
            xamo.PPWEbxbar(2)
            time.sleep(2)
        FinStr = dw.FindPicE(14, 129, 124, 181, "DPS.bmp", "000000", 0.9, 0)
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
            xamo.KJDfekiHDh(87, 2)
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
            time.sleep(0.7)
            向右()
            time.sleep(0.4)
            弹起()
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 1)
            time.sleep(0.5)
    elif guanqia == 4:
        if zhiye == 2:
            #点击左
            xamo.KJDfekiHDh(37, 1)
            time.sleep(0.1)
            FinStr = dw.FindPicE(531, 561, 715, 596, "双翼风刃.bmp|游离之风.bmp|凤鸣冲击.bmp|真空旋风破.bmp", "000000", 0.9, 0)
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
            # 九霄风雷 R
            xamo.KJDfekiHDh(82, 2)
            time.sleep(2)
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 2)
            time.sleep(0.6)
    elif guanqia == 5:
        if zhiye == 1:
            xamo.KJDfekiHDh(89, 1)
            time.sleep(1)
            向下()
            time.sleep(3)
            弹起()
        elif zhiye == 2:
            FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[1]) >= 0:
                my_y = int(pos[2])
                if my_y > 160:
                    右上()
                    time.sleep(0.8)
                    向上()
                    time.sleep(0.5)
                    弹起()
                else:
                    #点击右
                    xamo.KJDfekiHDh(39, 1)
                    time.sleep(0.1)
                    FinStr = dw.FindPicE(531, 561, 715, 596, "双翼风刃.bmp|游离之风.bmp|凤鸣冲击.bmp|真空旋风破.bmp", "000000", 0.9, 0)
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
                    time.sleep(0.3)
                    弹起()
            # 万象风龙阵 T
            xamo.KJDfekiHDh(84, 4)
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
            右上()
            time.sleep(0.4)
            向右()
            time.sleep(0.4)
            弹起()
            # 无限风域 Y
            xamo.KJDfekiHDh(89, 2)
            time.sleep(5)
    elif guanqia == 7:
        if zhiye == 1:
            技能(2)
            xamo.KJDfekiHDh(89, 1)
            time.sleep(1)
            duobidihuo = True
        elif zhiye == 2:
            右上()
            time.sleep(0.2)
            向右()
            time.sleep(0.2)
            弹起()
            # 风卷残云 E
            xamo.KJDfekiHDh(69, 2)
            time.sleep(0.3)
            # 风暴之拳 G
            xamo.KJDfekiHDh(71, 1)
            time.sleep(1.2)
            for i in range(3):
                # 游龙惊风破 W
                xamo.KJDfekiHDh(87, 1)
                time.sleep(0.2)
            time.sleep(1.6)
            for i in range(3):
                # 九霄风雷 R
                xamo.KJDfekiHDh(82, 1)
                time.sleep(0.2)
            time.sleep(1.7)
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 2)
            time.sleep(0.5)
            # 双翼风刃 A
            xamo.KJDfekiHDh(65, 1)
            time.sleep(0.5)
            # 游离之风 S
            xamo.KJDfekiHDh(83, 1)
            time.sleep(0.5)
    elif guanqia == 9:
        if zhiye == 1:
            pass
        elif zhiye == 2:
            # 游龙惊风破 W
            xamo.KJDfekiHDh(87, 2)
            time.sleep(1.5)
            # 游离之风 S
            xamo.KJDfekiHDh(83, 1)
            time.sleep(0.5)
    elif guanqia == 8:
        if zhiye == 1:
            pass
        elif zhiye == 2:
            向下()
            time.sleep(0.3)
            右下()
            time.sleep(0.3)
            弹起()
            time.sleep(0.1)
            #点击左
            xamo.KJDfekiHDh(37, 1)
            time.sleep(0.1)
            # 风卷残云 E
            xamo.KJDfekiHDh(69, 1)
            time.sleep(0.8)
            向左()
            time.sleep(0.3)
            弹起()
            # 风暴之眼 Q
            xamo.KJDfekiHDh(81, 1)
            time.sleep(0.5)
    return duobidihuo
def 异常文本(str):
    file = open('异常文本.txt', 'w')
    file.write(str)  # 写入内容信息
    file.close()
    dw.RunApp('异常文本.txt', 0)
def 获取本地版本号():
    try:
        f = open('ver', 'r')
        f.close()
    except IOError:
        xxoo = os.getcwd() + '/ver'  # 在当前py文件所在路径下的new文件中创建txt
        file = open(xxoo, 'w')
        file.write('1')  # 写入内容信息
        file.close()
    with open('ver', 'r') as f:
        ver = f.read()
    return ver
def 检查更新():
    ver = 获取本地版本号()
    #prints('本机版本 = ' + ver)
    # 检查更新
    is_temp = os.path.isfile(os.path.dirname(os.getcwd()) + '/ver')
    if is_temp:
        with open(os.path.dirname(os.getcwd()) + '/ver', 'r') as f:
            strs = f.read()
        #prints('本地版本 = ' + strs)
        if strs != '0' and strs != '':
            if ver != strs:
                if 检查更新锁(1):
                    with open('ver', 'w') as f:
                        f.write(strs)
                    弹起()
                    prints('发现新版本即将更新')
                    with open('v.txt', 'w') as f:
                        f.write('bendi')
                    time.sleep(3)
                    dw.RunApp('update.exe', 0)
                    os._exit(1)
            else:
                #连接服务器检查版本
                try:
                   strs = str(connect.getver(''))
                   #prints('服务器版本 = ' + strs)
                   if strs != '0' and strs != '':
                       if isinstance(strs, str):
                           if ver != strs:
                               if 检查更新锁(1):
                                   with open('ver', 'w') as f:
                                       f.write(strs)
                                   with open(os.path.dirname(os.getcwd()) + '/ver', 'w') as f:
                                       f.write(strs)
                                   弹起()
                                   prints('发现新版本即将更新')
                                   with open('v.txt', 'w') as f:
                                       f.write('yuancheng')
                                   time.sleep(3)
                                   dw.RunApp('update.exe', 0)
                                   os._exit(1)
                except:
                      print('检查版本失败')
def 检查更新锁(t):
    if t == 1:
        p = 'C:/Ver.ini'
        is_temp = os.path.isfile(p)
        if not is_temp:
            fp = open(p, 'w')
            fp.close()
            set_ini('C:/Ver.ini', '更新锁', '锁', pc_name)
            return True
        temp = get_ini('C:/Ver.ini', '更新锁', '锁', "0")
        if temp == '0' or temp == '':
            set_ini('C:/Ver.ini', '更新锁', '锁', pc_name)
            return True
        elif temp == pc_name:
            return True
        else:
            return False
    elif t == 2:
        temp = get_ini('C:/Ver.ini', '更新锁', '锁', "0")
        prints('更新锁' + temp)
        if temp == pc_name:
            set_ini('C:/Ver.ini', '更新锁', '锁', '0')
def 获取职业():
    # 职业1 = 召唤：2 = 风法
    prints('检查职业')
    hqrwzy_time= time.clock()
    while True:
        hqrwzy_time_now = time.clock()
        if hqrwzy_time_now - hqrwzy_time > 20:
            return 3
        FinStr = dw.FindStrE(131, 94, 230, 143, "个人信息", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.FindStrE(142, 286, 223, 306, "召唤师|月之女皇|月蚀", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 1
            FinStr = dw.FindStrE(142, 286, 223, 306, "风神", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                return 2
            return 0
        else:
            xamo.KJDfekiHDh(77,1)
            time.sleep(1)
def 检查黑钻():
    #鼠标移动到疲劳上
    xamo.UIKBudj(447, 553)
    time.sleep(1)
    xamo.PPWEbxbar(1)
    time.sleep(1)
    FinStr = dw.FindStrE(155,424,488,565, "疲劳值", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        FinStr = dw.FindStrE(155, 424, 488, 565, "黑钻疲劳", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            set_ini('config/账号数据.ini', account.hao, '黑钻', '真')
        else:
            set_ini('config/账号数据.ini', account.hao, '黑钻', '假')
def 购买盒子():
    prints('购买盒子')
    int_hezi = 0
    sx = int(get_ini('config/cfg.ini', '主配置', '超过点券', "200000"))
    gmhz_time = time.clock()
    while True:
        gmhz_time_now = time.clock()
        d3 = gmhz_time_now - gmhz_time
        if d3 > 300:
            return 3
        FinStr = dw.FindStrE(397, 390, 690, 552, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            number = dw.Ocr(intx +25,inty + 44, intx + 93, inty + 69, "e6c89b-000000", 1)
            number = re.sub("\D", "", number)
            prints('点券 = ' + number)
            if int(number) >= sx + 300:
                int_hezi = int((int(number) - sx) / 300)
                prints('准备购买' + str(int_hezi) + '个盒子')
                break
            else:
                return 0
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(2)
    gmhz_time = time.clock()
    while True:
        gmhz_time_now = time.clock()
        d3 = gmhz_time_now - gmhz_time
        if d3 > 300:
            return 3
        FinStr = dw.FindStrE(92, 540, 171, 579, "积分", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            pass
        else:
            xamo.UIKBudj(481, 577)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.FindStrE(425, 40, 720, 79, "装饰类", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #点击道具
            xamo.UIKBudj(242, 57)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            for tn in range(6):
                FinStr = dw.FindPicE(16, 88, 424, 521, "盒子.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    intx = int(pos[1])
                    inty = int(pos[2])
                    for temp in range(int_hezi):
                        xamo.UIKBudj(intx + 109, inty + 78)
                        time.sleep(0.2)
                        xamo.PPWEbxbar(1)
                        time.sleep(1)
                    #全部购买
                    xamo.UIKBudj(558, 560)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
                    break
                else:
                    xamo.UIKBudj(403, 98)
                    time.sleep(0.2)
                    xamo.PPWEbxbar(1)
                    time.sleep(1)
        else:
            #点击道具分类
            xamo.UIKBudj(365, 23)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.FindStrE(370, 98, 431, 122, "结算窗口", "ffffff-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            #购买
            xamo.UIKBudj(503, 476)
            time.sleep(0.2)
            xamo.PPWEbxbar(1)
            time.sleep(2)
            xamo.KJDfekiHDh(13,1)
            time.sleep(1)
            return 1
def 开盒子(p):
    prints('开盒子')
    khz_time = time.clock()
    khz_k = True
    while True:
        khz_time_now = time.clock()
        d3 = khz_time_now - khz_time
        if d3 > 300:
            return 3
        FinStr = dw.FindStrE(397, 390, 690, 552, "重", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            #点击消耗栏
            xamo.UIKBudj(intx + 72, inty - 233)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(0.5)
            xamo.UIKBudj(592, 171)
            time.sleep(0.1)
            if p == 1:
                for temp in range(20):
                    FinStr = dw.FindPicE(470, 242, 718, 475, "赛丽亚的幸运.bmp", "000000", 0.9, 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 5, inty + 5)
                        time.sleep(0.5)
                        xamo.XKkncvhe(1)
                        time.sleep(1)
                        xamo.UIKBudj(592, 171)
                        time.sleep(0.5)
                    if khz_k:
                        FinStr = dw.FindPicE(470, 242, 718, 475, "背包盒子.bmp", "000000", 0.9, 0)
                        pos = FinStr.split('|')
                        if int(pos[1]) > 0:
                            intx = int(pos[1])
                            inty = int(pos[2])
                            xamo.UIKBudj(intx + 5, inty + 5)
                            time.sleep(0.5)
                            xamo.XKkncvhe(1)
                            time.sleep(0.5)
                            xamo.UIKBudj(intx - 10, inty + 5)
                            time.sleep(0.5)
                            xamo.PPWEbxbar(1)
                            time.sleep(1)
                            xamo.UIKBudj(592, 171)
                            time.sleep(0.5)
                    FinStr = dw.FindStrE(100, 56, 519, 547, "确认", "ffffb8-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        FinStr_ = dw.FindStrE(301, 237, 490, 381, "魔锤不足", "ffffff-000000", 1)
                        pos_ = FinStr_.split('|')
                        if int(pos_[1]) > 0:
                            khz_k = False
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 10, inty + 5)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.5)
                        xamo.UIKBudj(592, 171)
                        time.sleep(0.5)
                break
            elif p == 2:
                for temp in range(8):
                    FinStr = dw.FindPicE(470, 242, 718, 475, "特别快递礼盒.bmp", "000000", 0.9, 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 5, inty + 5)
                        time.sleep(0.5)
                        xamo.XKkncvhe(1)
                        time.sleep(1)
                        xamo.UIKBudj(592, 171)
                        time.sleep(0.5)
                    FinStr = dw.FindStrE(100, 56, 519, 547, "确认", "ffffb8-000000", 1)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 10, inty + 5)
                        time.sleep(0.5)
                        xamo.PPWEbxbar(1)
                        time.sleep(0.5)
                        xamo.UIKBudj(592, 171)
                        time.sleep(0.5)
                    FinStr = dw.FindPicE(470, 242, 718, 475, "代币券.bmp", "000000", 0.9, 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        intx = int(pos[1])
                        inty = int(pos[2])
                        xamo.UIKBudj(intx + 5, inty + 5)
                        time.sleep(0.5)
                        xamo.XKkncvhe(1)
                        time.sleep(1)
                        xamo.UIKBudj(592, 171)
                        time.sleep(0.5)
                break
        else:
            xamo.KJDfekiHDh(73,1)
            time.sleep(2)
def 特别快递():
    for i in range(5):
        FinStr = dw.FindPicE(270, 487, 502, 556, "特别快递.bmp|特别快递1.bmp|特别快递2.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 5)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(1)
        FinStr = dw.FindPicE(370, 313, 436, 347, "特别快递领取.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 10, inty + 5)
            time.sleep(0.5)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            return 1
    return 0
def 赛丽亚房间(is_60m,CRuser, CRpwd,x,y):
    duihuandianquan = get_ini('config/cfg.ini', '主配置', '兑换点券',"假")
    goumaimianxiu = get_ini('config/cfg.ini', '主配置', '购买免修',"假")
    goumaihuangjinpai = get_ini('config/cfg.ini', '主配置', '购买黄金牌',"假")
    zhuanqian = get_ini('config/cfg.ini', '主配置', '只转钱', "假")
    zhiye = ''
    time.sleep(5)
    Imok = True
    youjianxiang = True
    sly_time = time.clock()
    while True:
        sly_time_now = time.clock()
        d3 = sly_time_now - sly_time
        if d3 > 60:
            Imok = False
            break
        发送记录()
        time.sleep(0.5)
        FinStr = dw.FindStrE(0, 0, x, y, "结束游戏", "ddc593-050505|ffffb8-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            prints('检查封号中断')
            time.sleep(5)
            fenghao_return = 封号检查()
            if fenghao_return == 'F5':
                prints("账号停封5天，换号")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif fenghao_return == 'F7':
                prints("账号停封7天，换号")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif fenghao_return == 'F0':
                prints('只是中断没有封号，重上')
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif fenghao_return == 'F100':
                prints("永久封号，换号")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif fenghao_return == 'F101':
                prints("此ID已在游戏中，重上")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            # 选择角色
            juesechuli_ret = 角色处理(1)
            if juesechuli_ret == 0:
                prints("角色刷完，换号")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif juesechuli_ret == 1:
                prints("角色更换完成")
            elif juesechuli_ret == 2:
                prints("网络连接中断，重上")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif juesechuli_ret == 3:
                prints("角色处理超时，重上")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            time.sleep(10)
            # 刷新列表
            刷新列表()
        if youjianxiang:
            FinStr = dw.FindStrE(712, 300, 788, 364, "邮件箱", "f7d65a-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                if 近期制裁() == 1:
                    Imok = False
                    break
                time.sleep(1)
                清理游戏窗口()
                youjianxiang = False
        FinStr = dw.FindStrE(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if 近期制裁() == 1:
                Imok = False
                break
            time.sleep(3)
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 3)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            time.sleep(1)
            清理游戏窗口()
        FinStr = dw.FindStrE(369, 512, 431, 541, "确认", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if 近期制裁() == 1:
                Imok = False
                break
            time.sleep(1)
            清理游戏窗口()
        FinStr = dw.FindStrE(345,132,452,172, "优惠券礼盒", "ffffff-000000|aaaaaa-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if 近期制裁() == 1:
                Imok = False
                break
            time.sleep(1)
            清理游戏窗口()
        FinStr = dw.FindPicE(365, 356, 418, 384, "签到.bmp|签到2.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time.sleep(3)
            intx = int(pos[1])
            inty = int(pos[2])
            xamo.UIKBudj(intx + 5, inty + 3)
            time.sleep(1)
            xamo.PPWEbxbar(1)
            if 近期制裁() == 1:
                Imok = False
                break
            time.sleep(1)
            清理游戏窗口()
        FinStr = dw.FindPicE(114, 59, 739, 306, "叉.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if 近期制裁() == 1:
                Imok = False
                break
            time.sleep(1)
            清理游戏窗口()
        FinStr = dw.FindStrE(307, 106, 585, 304, "赛丽亚", "f7d65a-000000|5ac5f7-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            if 近期制裁() == 1:
                Imok = False
                break
            if is_60m:
                # 职业1 = 召唤：2 = 风法
                prints("等待60秒...")
                time.sleep(10)
                xamo.UIKBudj(1119, 43)
                time.sleep(0.5)
                xamo.PPWEbxbar(1)
                time.sleep(1)
                xamo.UIKBudj(1119, 108)
                time.sleep(0.5)
                xamo.PPWEbxbar(2)
                time.sleep(1)
                if 近期制裁() == 1:
                    Imok = False
                    break
                time.sleep(30)
                # 只兑换点券
                if zhuanqian == '真':
                    出售点券()
                    清理游戏窗口()
                    接收邮件()
                    清理游戏窗口()
                    fyj_return = 发邮件(CRuser, CRpwd)
                    if fyj_return == 1:
                        # 正常返回
                        pass
                    elif fyj_return == 2:
                        prints('网络连接中断,重上')
                        end_exsit()
                        time.sleep(2)
                        Imok = False
                        break
                    elif fyj_return == 3:
                        prints('发送邮件超时,重上')
                        end_exsit()
                        time.sleep(2)
                        Imok = False
                        break
                    prints("礼盒处理完成，换号")
                    记录完成时间_转钱()
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                检查累积在线奖励()
                检查黑钻()
                # 设置
                shezhi = get_ini('config/设置.ini', '设置', account.hao + '_' + account.daqu, "假")
                if shezhi != '真':
                    sz_ret = 设置()
                    if sz_ret == 1:
                        set_ini('config/设置.ini', '设置', account.hao + '_' + account.daqu, '真')
                        prints('快捷键设置成功')
                    else:
                        prints('快捷键设置失败')
            #从这里开始是每个角色都要执行的操作

            zhiye = int(get_ini('config/账号数据.ini', account.hao + '_' + account.daqu + '_' + account.dangqianjuese, '职业', "0"))
            if zhiye == 0:
                zhiye = 获取职业()
                if zhiye == 3 or zhiye == 0:
                    prints('获取职业超时或错误')
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                else:
                    set_ini('config/账号数据.ini', account.hao + '_' + account.daqu + '_' + account.dangqianjuese, '职业',
                            str(zhiye))
                ret_ql = 清理游戏窗口()
                if ret_ql == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
            set_ini('config/记录.ini', '刷号记录', '职业', str(zhiye))
            if goumaimianxiu == '真':
                ret_gmmx = 购买免修黄金牌(1)
                if ret_gmmx == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                ret_ql = 清理游戏窗口()
                if ret_ql == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
            if goumaihuangjinpai == '真':
                ret_gmmx = 购买免修黄金牌(2)
                if ret_gmmx == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                ret_ql = 清理游戏窗口()
                if ret_ql == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
            gmhz_ret = 购买盒子()
            ret_ql = 清理游戏窗口()
            if ret_ql == 0:
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            if gmhz_ret == 1:
                khz_ret = 开盒子(1)
                if khz_ret == 3:
                    prints('开盒子超时,重上')
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
            elif gmhz_ret == 3:
                prints('购买盒子超时,重上')
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            tbkd_ret = 特别快递()
            if tbkd_ret == 1:
                ret_ql = 清理游戏窗口()
                if ret_ql == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                接收邮件()
                ret_ql = 清理游戏窗口()
                if ret_ql == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                开盒子(2)
                ret_ql = 清理游戏窗口()
                if ret_ql == 0:
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
            if duihuandianquan == "真":
                csdq_ret = 出售点券()
                清理游戏窗口()
                if csdq_ret > 0:
                    接收邮件()
                    清理游戏窗口()
            # 刷新列表
            刷新列表()
            # 格兰迪才学习技能
            # 学习技能
            ret_jn = 学习技能(zhiye)
            if ret_jn == 0:
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            # 移动到副本门口
            yd_ret = 移动(1)
            if yd_ret == 0:
                prints('移动位置超时')
                end_exsit()
                time.sleep(2)
                Imok = False
            break
        FinStr = dw.FindStrE(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
        FinStr = dw.FindStrE(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
    return Imok
def 副本门口(pl_color,CRuser, CRpwd):
    maoxiandengji = int(get_ini('config/cfg.ini', '游戏配置', '冒险等级', "4"))
    Imok = True
    XR_num = 0
    menkou_time = time.clock()
    while True:
        time.sleep(0.05)
        menkou_time_now = time.clock()
        time_temp = menkou_time_now - menkou_time
        if time_temp > 360:
            prints("图外超时，重上")
            end_exsit()
            time.sleep(2)
            Imok = False
            break
        FinStr = dw.FindStrE(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
        FinStr = dw.FindStrE(379, 441, 437, 468, "关闭", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            清理游戏窗口()
        if 中断_查() == 1:
            Imok = False
            break
        # 疲劳刷完了
        color = dw.GetColor(339, 553)
        if color == "0b0b0b" or color == "333333" or color == pl_color:
            time.sleep(1)
            FinStr = dw.FindStrE(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                break
            prints('打印任务完成')
            ret_csfj = 出售分解(1)
            #安全模式等待超时
            if ret_csfj == 3:
                prints('安全模式等待超时')
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            接收邮件()
            # 发送邮件
            fyj_return = 发邮件(CRuser, CRpwd)
            if fyj_return == 1:
                # 正常返回
                pass
            elif fyj_return == 2:
                prints('网络连接中断,重上')
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif fyj_return == 3:
                prints('发送邮件超时,重上')
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            # 记录完成时间
            记录完成时间()
            # 刷新列表
            tk.trickit()
            # 换角色
            prints("PL刷完，换角色")
            juesechuli_ret = 角色处理(2)
            if juesechuli_ret == 0:
                prints("角色刷完，换号")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            if juesechuli_ret == 1:
                # 正常返回
                prints('角色处理完成')
                pass
            elif juesechuli_ret == 2:
                prints("网络连接中断，重上")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            elif juesechuli_ret == 3:
                prints("角色处理超时，重上")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
            # 刷新列表
            tk.trickit()
            time.sleep(5)
            清理游戏窗口()
            # 换完角色跳出从头开始
            Imok = False
            break
        FinStr = dw.FindStrE(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
        FinStr = dw.FindStrE(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.FindPicE(272, 460, 501, 544, "虚弱.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                prints('虚弱等待')
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
                XR_num += 1
                if XR_num >= 42:
                    prints('虚弱等待超时，重上')
                    end_exsit()
                    Imok = False
                    break
                清理游戏窗口()
                menkou_time = time.clock()
                continue
            prints('副本门口处理')
            检查累积在线奖励()
            出售分解(1)
            检查更新()
            六点更新()
            向左()
            time.sleep(0.5)
            向右()
            xuantu_time = time.clock()
            while True:
                time.sleep(0.05)
                xuantu_time_now = time.clock()
                time_temp = xuantu_time_now - xuantu_time
                if time_temp > 120:
                    prints("选图超时，重上")
                    end_exsit()
                    time.sleep(2)
                    Imok = False
                    break
                if 中断_查() == 1:
                    Imok = False
                    break
                time.sleep(0.2)
                FinStr = dw.FindStrE(509, 533, 583, 570, "练习模式", "ddc593-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    time.sleep(1)
                    弹起()
                    FinStr = dw.FindPicE(412, 347, 555, 409, "副本界面_格兰迪.bmp|副本界面_格兰迪1.bmp", "000000", 0.9, 0)
                    pos = FinStr.split('|')
                    if int(pos[1]) > 0:
                        for i in range(5):
                            xamo.KJDfekiHDh(37, 1)
                            time.sleep(0.2)
                        for i in range(maoxiandengji):
                            xamo.KJDfekiHDh(39, 1)
                            time.sleep(0.2)
                        xamo.KJDfekiHDh(32, 3)
                        time.sleep(0.2)
                        xamo.KJDfekiHDh(32, 3)
                        time.sleep(3)
                    else:
                        xamo.KJDfekiHDh(38, 1)
                        time.sleep(0.5)
                FinStr = dw.FindStrE(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    break
            break
    return Imok
def 格蓝迪图内(jianqu,pl_color):
    prints('捡取 = ' + str(jianqu))
    xingwei = True
    guanqia = 0
    duobidihuo = False
    Imok = True
    time_is = True
    zhiye = int(get_ini('config/记录.ini', '刷号记录', '职业', '0'))
    prints('职业 = ' + str(zhiye))
    while_time = time.clock()
    # 游戏内循环执行
    prints('进入副本')
    while True:
        time.sleep(0.05)
        # 图内超时判断
        if time_is:
            while_time_now = time.clock()
            time_temp = while_time_now - while_time
            if time_temp > 300:
                if not os.path.exists(os.getcwd() + '/图内超时截图'):  # 判断当前路径是否存在，没有则创建new文件夹
                    os.makedirs(os.getcwd() + '/图内超时截图')
                dw.CaptureJpg(1, 1, 800, 600, os.getcwd() + '/图内超时截图/' + str(time.time())  + '.jpg', 20)
                prints("图内超时，重上")
                end_exsit()
                time.sleep(2)
                Imok = False
                break
        if 中断_查() == 1:
            Imok = False
            break
        if guanqia == 0:
            guanqia = 检查关卡()
            prints('关卡 = ' + str(guanqia))
        if xingwei:
            # 关卡7再次检查确认
            # 如果还能在小地图找到人物，证明走错了关卡，就按关卡检查的返回
            if guanqia == 7:
                guanqia_temp = 检查关卡()
                if guanqia_temp > 0:
                    guanqia = guanqia_temp
            if guanqia > 0:
                duobidihuo = 关卡构造(zhiye, guanqia)
                xingwei = not xingwei
        FinStr = dw.FindPicE(0, 78, 799, 552, "可破坏.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            打石头()
        if str(jianqu) == '真':
            FinStr = dw.FindPicE(0, 78, 799, 552, "wp.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                捡取()
                FinStr = dw.FindPicE(0, 78, 799, 552, "可破坏.bmp", "000000", 0.9, 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    打石头()
        FinStr = dw.FindPicE(718, 25, 795, 105, "问号.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            找门(guanqia, 1, jianqu)
            time.sleep(1)
            xingwei = True
            if guanqia == 6:
                guanqia += 1
                prints('关卡 = BOSS关')
            else:
                guanqia = 0
            continue
        else:
            if zhiye == 2:
                if guanqia == 5:
                    向左()
                    time.sleep(0.5)
                    弹起()
                打怪_风法(guanqia)
        FinStr = dw.FindPicE(690, 67, 787, 104, "跳过ESC.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            FinStr = dw.FindPicE(418,438,549,477, "黄金牌.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 10, inty + 10)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
                time.sleep(1)
            else:
                xamo.KJDfekiHDh(27, 2)
                time.sleep(1)
        FinStr = dw.FindPicE(612, 132, 735, 164, "通关.bmp", "000000", 0.9, 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            duobidihuo = False
            弹起()
            boss关捡取()
            弹起()
            清理游戏窗口()
            color = dw.GetColor(339, 553)
            if color == "0b0b0b" or color == "333333" or color == pl_color:
                print('返回城镇')
                返回城镇()
                time.sleep(3)
                break
            else:
                fz_ret = 检查负重()
                if fz_ret == 1:
                    返回城镇()
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
        FinStr = dw.FindStrE(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            break
        if zhiye == 1:
            # 躲避
            FinStr = dw.FindPicE(0, 78, 799, 552, "my.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                myX = int(pos[1])
                myY = int(pos[2])
                FinStr = dw.FindColorE(myX - 100, myY + 130, myX + 120, myY + 210, "ff0094-101010|ff00ff-101010", 1.0,
                                         0)
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
                color = dw.GetColor(52, 566)
                if color == '000000':
                    xamo.KJDfekiHDh(49, 1)
        FinStr = dw.FindStrE(333, 571, 473, 597, "只能城镇交易", "ffff00-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            time_is = True
            while_time = time.clock()
    return Imok
def while_():
    CDK = get_ini('注册码.ini', '注册码', pc_name, "")
    if CDK == '':
        #没有注册码
        print('没有注册码')
        异常文本('没有注册码')
        os._exit(1)
    else:
        ret = connect.login(CDK + '|' + public_code)
        if ret == '0':
            # 登录异常
            print('登录异常')
            异常文本('登录异常')
            os._exit(1)
        elif ret == '102':
            # 注册码到期
            print('注册码到期')
            异常文本('注册码到期')
            os._exit(1)
        elif ret == '1':
            #正常
            pass
    #读取配置文档
    x = int(get_ini('config/cfg.ini', '主配置', 'x',"0"))
    y = int(get_ini('config/cfg.ini', '主配置', 'y',"0"))
    WeGame = get_ini('config/cfg.ini', '主配置', 'WeGame',"")
    number = get_ini('config/cfg.ini', '主配置', '账号路径',"")
    CRuser = get_ini('config/cfg.ini', '主配置', '若快账号',"")
    CRpwd = get_ini('config/cfg.ini', '主配置', '若快密码',"")
    jianqu = get_ini('config/cfg.ini', '主配置', '捡取',"假")
    ditu = get_ini('config/cfg.ini', '游戏配置', '地图',"假")
    pl = get_ini('config/cfg.ini', '游戏配置', '疲劳处理',"1")
    zhuanqian = get_ini('config/cfg.ini', '主配置', '只转钱', "假")
    pl_color = 'ffffff'
    if pl == '1':
        pl_color = 'b30026'
    if ditu == '假':
        prints('未选择地图，停止')
        input()
    account.dituid = int(ditu)
    # zy = get_ini('config/cfg.ini', '主配置', '职业', '101')
    # if zy == '101':
    #     zhiye = 2
    # else:
    #     zhiye = int(zy) + 1
    # 职业1 = 召唤：2 = 风法
    prints('捡取 = ' + str(jianqu))
    # 进入正题
    检查更新锁(2)#解锁
    tk.trickit()
    while True:
        is_60m = False
        xamo.UIKBudj(10, 10)
        time.sleep(1)
        color = dw.GetColor(1, 1)
        prints('color = ' + color)
        if color == '3a6ea5':
            扫图标()
            刷新列表()
            # 游戏内执行一次
            end_exsit()
            # 登录成功返回窗口句柄
            login_ret = 登录游戏(CRuser, CRpwd, number, WeGame, zhuanqian,x,y)
            prints('登录成功')
            if login_ret == 0:
                prints("连接频道失败，重上")
                end_exsit()
                time.sleep(2)
                continue
            elif login_ret == 3:
                prints("登录超时，重上")
                end_exsit()
                time.sleep(2)
                continue
            elif login_ret == 4:
                login_num = get_ini("config/记录.ini", "刷号记录", "当前账号", "")
                set_ini("config/记录.ini", "密码错误", login_num, '密码错误')
                prints("密码错误，重上")
                end_exsit()
                time.sleep(2)
                continue
            elif login_ret == 5:
                login_num = get_ini("config/记录.ini", "刷号记录", "当前账号", "")
                set_ini("config/记录.ini", "冻结", login_num, '冻结')
                prints("账号冻结，重上")
                end_exsit()
                time.sleep(2)
                continue
            elif login_ret == 101:
                prints("账号登录失败,检查账号状态")
                time.sleep(10)
                end_exsit()
                time.sleep(2)
                continue
                continue
            time.sleep(3)
            is_60m = True
        Imok = 赛丽亚房间(is_60m,CRuser, CRpwd,x,y)
        if not Imok:
            continue
        if account.dituid == 1:
            while True:
                # 格兰迪
                Imok = 副本门口(pl_color,CRuser, CRpwd)
                if not Imok:
                    break
                Imok = 格蓝迪图内(jianqu,pl_color)
                if not Imok:
                    break
        time.sleep(1)
if __name__ == '__main__':
    multiprocessing.freeze_support()
    t = threading.Thread(target=while_, name='MainThread')
    #t.setDaemon(True)
    t.start()
    # 局域网中控暂时关闭
    # t1 = threading.Thread(target=loop, name='MainThread_loop')
    # t1.start()
    pc_n = pc_name
    CD = get_ini('注册码.ini', '注册码', pc_n, "")
    ip = get_ini('config/主机设置.ini', '设置', 'ip', "192.168.0.66")
    t = 0
    j = 0
    S = 0
    yc = 0
    while True:
        j += 1
        if j >= 300:
            #跳动
            ret_td = connect.get(CD + '|' + public_code)
            if ret_td != '':
                if ret_td == '101':
                    #注册码在别的机器登录
                    print('注册码在别的机器登录')
                    end_exsit()
                    异常文本('注册码在别的机器登录')
                    yc = 0
                    os._exit(1)
                elif ret_td == '0':
                    #查询异常
                    print('查询异常')
                    异常文本('查询异常' + str(y))
                    yc += 1
                elif ret_td == '102':
                    #到期
                    end_exsit()
                    print('注册码到期')
                    异常文本('注册码到期')
                    yc = 0
                    os._exit(1)
                elif ret_td == '1':
                    #正常
                    yc = 0
            else:
                yc += 1
            if yc > 10:
                #跳动异常退出
                end_exsit()
                print('网络异常')
                异常文本('网络异常')
                os._exit(1)
            j = 0
        if public.k == 2:
            弹起()
            os._exit(1)
        # 局域网服务器失联
        # if public.ShiLian:
        #     if S >= 60:
        #         try:
        #             HOST = ip
        #             PORT = 8989
        #             BUFSIZ = 1024
        #             ADDR = (HOST, PORT)
        #             tcpCliSock = socket(AF_INET, SOCK_STREAM)
        #             tcpCliSock.connect(ADDR)
        #             tcpCliSock.settimeout(60)
        #             public.ShiLian = False
        #         except:
        #             print("主机不在线")
        #             S = 0
        #     else:
        #         S += 1
        time.sleep(1)
        t += 1
        if t > 30:
            FinStr = dw.FindPicE(0, 0, x, y, "腾讯高速下载停止.bmp|腾讯安全保护停止.bmp", "000000", 0.9, 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                xamo.UIKBudj(intx + 400, inty - 28)
                time.sleep(0.2)
                xamo.PPWEbxbar(1)
            t = 0