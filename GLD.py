#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import do
import rk
import configparser
import random
import datetime
import os
import time
damo = do.bw()
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
# 读取配置文档
WeGame = get_ini('config/cfg.ini','主配置', 'WeGame')
number = get_ini('config/cfg.ini','主配置', '账号路径')
rkuser = get_ini('config/cfg.ini','主配置', '若快账号')
rkpwd = get_ini('config/cfg.ini','主配置', '若快密码')
print(WeGame, number, rkuser, rkpwd)
def 向左():
    if damo.GetKeyStatepy(38) == 1:
        damo.KeyUppy(38)
    if damo.GetKeyStatepy(39) == 1:
        damo.KeyUppy(39)
    if damo.GetKeyStatepy(40) == 1:
        damo.KeyUppy(40)
    if damo.GetKeyStatepy(37) == 0:
        damo.KeyPresspy(37)
        damo.Delaypy(50)
        damo.KeyDownpy(37)
def 向右():
    if damo.GetKeyStatepy(38) == 1:
        damo.KeyUppy(38)
    if damo.GetKeyStatepy(37) == 1:
        damo.KeyUppy(37)
    if damo.GetKeyStatepy(40) == 1:
        damo.KeyUppy(40)
    if damo.GetKeyStatepy(39) == 0:
        damo.KeyPresspy(39)
        damo.Delaypy(50)
        damo.KeyDownpy(39)
def 向上():
    if damo.GetKeyStatepy(40) == 1:
        damo.KeyUppy(40)
    if damo.GetKeyStatepy(37) == 1:
        damo.KeyUppy(37)
    if damo.GetKeyStatepy(39) == 1:
        damo.KeyUppy(39)
    if damo.GetKeyStatepy(38) == 0:
        damo.KeyDownpy(38)
def 向下():
    if damo.GetKeyStatepy(38) == 1:
        damo.KeyUppy(38)
    if damo.GetKeyStatepy(37) == 1:
        damo.KeyUppy(37)
    if damo.GetKeyStatepy(39) == 1:
        damo.KeyUppy(39)
    if damo.GetKeyStatepy(40) == 0:
        damo.KeyDownpy(40)
def 左上():
    if damo.GetKeyStatepy(39) == 1:
        damo.KeyUppy(39)
    if damo.GetKeyStatepy(40) == 1:
        damo.KeyUppy(40)

    if damo.GetKeyStatepy(37) == 0:
        damo.KeyPresspy(37)
        damo.Delaypy(50)
        damo.KeyDownpy(37)
        damo.Delaypy(100)
    if damo.GetKeyStatepy(38) == 0:
        damo.KeyDownpy(38)
def 左下():
    if damo.GetKeyStatepy(38) == 1:
        damo.KeyUppy(38)
    if damo.GetKeyStatepy(39) == 1:
        damo.KeyUppy(39)

    if damo.GetKeyStatepy(37) == 0:
        damo.KeyPresspy(37)
        damo.Delaypy(50)
        damo.KeyDownpy(37)
        damo.Delaypy(100)
    if damo.GetKeyStatepy(40) == 0:
        damo.KeyDownpy(40)
def 右上():
    if damo.GetKeyStatepy(37) == 1:
        damo.KeyUppy(37)
    if damo.GetKeyStatepy(40) == 1:
        damo.KeyUppy(40)

    if damo.GetKeyStatepy(39) == 0:
        damo.KeyPresspy(39)
        damo.Delaypy(50)
        damo.KeyDownpy(39)
        damo.Delaypy(100)
    if damo.GetKeyStatepy(38) == 0:
        damo.KeyDownpy(38)
def 右下():
    if damo.GetKeyStatepy(37) == 1:
        damo.KeyUppy(37)
    if damo.GetKeyStatepy(38) == 1:
        damo.KeyUppy(38)

    if damo.GetKeyStatepy(39) == 0:
        damo.KeyPresspy(39)
        damo.Delaypy(50)
        damo.KeyDownpy(39)
        damo.Delaypy(100)
    if damo.GetKeyStatepy(40) == 0:
        damo.KeyDownpy(40)
def 弹起():
    if damo.GetKeyStatepy(37) == 1:
        damo.KeyUppy(37)
    if damo.GetKeyStatepy(38) == 1:
        damo.KeyUppy(38)
    if damo.GetKeyStatepy(39) == 1:
        damo.KeyUppy(39)
    if damo.GetKeyStatepy(40) == 1:
        damo.KeyUppy(40)
def 捡取():
    print("捡取")
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
            Rnd = random.randint(1,4)
            if Rnd == 1:
                向上()
                damo.Delaypy(1000)
                弹起()
            elif Rnd == 2:
                向下()
                damo.Delaypy(1000)
                弹起()
            elif Rnd == 3:
                向左()
                damo.Delaypy(500)
                弹起()
            elif Rnd == 4:
                向右()
                damo.Delaypy(500)
                弹起()
            jianqu_time = datetime.datetime.now()
        FinStr = damo.FindPicEpy(0,78,799,552,"捡.bmp|捡1.bmp","000000","0.9",0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            damo.Delaypy(200)
            damo.KeyPresspy(88)
            damo.Delaypy(500)
        else:
            FinStr = damo.FindPicEpy(0,78,799,552,"my.bmp","000000","0.9",0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                my_x = int(pos[1])
                my_y = int(pos[2])
            FinStr = damo.FindPicEpy(0,78,799,552,"wp.bmp","000000","0.9",1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                wp_x = int(pos[1])
                wp_y = int(pos[2])
            else:
                弹起()
                print("没有东西")
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
def 检查关卡():
    x = [730, 748, 766, 766, 766, 784,784]
    y = [55, 55, 55, 73, 91, 91,74]
    for i in range(0,7):
        color = damo.GetColorpy(x[i],y[i])
        if color == "0000ff":
            return i+1
    print(0)
    return 0
def 找门(guanqia):
    print("找门")
    d1 = datetime.datetime.now()
    my_x_py = 10
    my_y_py = 190
    wp_x_py = 12
    wp_y_py = 14
    fangxiang = 判断方向(guanqia)
    if fangxiang == "左":
        pass
    elif fangxiang == "右":
        x,y,x1,y1 = 689,130,791,525
        pic = "左右门.bmp"
        wp_x_py = 10
        wp_y_py = 65
    elif fangxiang == "上":
        x,y,x1,y1 = 0,119,798,345
        pic = "上门.bmp"
        wp_x_py = 35
        wp_y_py = -20
    elif fangxiang == "下":
        x,y,x1,y1 = 0,340,798,529
        pic = "下门.bmp"
        wp_x_py = 35
        wp_y_py = 140
    while True:
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        FinStr = damo.FindPicEpy(0,78,799,552, "可破坏.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            打石头()
        FinStr = damo.FindPicEpy(0,78,799,552,"my.bmp","000000","0.9",0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = damo.FindPicEpy(x,y,x1,y1,pic,"000000","0.9",0)
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
        FinStr = damo.FindPicEpy(0,78,799,552,"wp.bmp","000000","0.9",0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            捡取()
        FinStr = damo.FindPicEpy(718,25,795,105, "问号绿.bmp|问号黄.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            pass
        else:
            if guanqia == 6:
                FinStr = damo.FindPicEpy(604,21,799,162, "my_小地图.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    pass
                else:
                    弹起()
                    print("找门成功")
                    break
            else:
                弹起()
                print("找门成功")
                break
        d2 = datetime.datetime.now()
        d3 = d2 - d1
        if d3.seconds > 10:
            if fangxiang == "左":
                弹起()
                向右()
                damo.Delaypy(1000)
                弹起()
            elif fangxiang == "右":
                向左()
                弹起()
                向左()
                damo.Delaypy(1000)
                弹起()
            elif fangxiang == "上":
                弹起()
                向下()
                damo.Delaypy(1000)
                弹起()
            elif fangxiang == "下":
                弹起()
                向上()
                damo.Delaypy(1000)
                弹起()
            d1 = datetime.datetime.now()
def 打石头():
    print("打石头")
    my_x_py = 10
    my_y_py = 190
    wp_x_py = 12
    wp_y_py = 40
    while True:
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        FinStr = damo.FindPicEpy(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = damo.FindPicEpy(0, 78, 799, 552, "可破坏.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            wp_x = int(pos[1])
            wp_y = int(pos[2])
        else:
            弹起()
            print("没有石头")
            break
        if my_x > 0 and my_y > 0 and wp_x > 0 and wp_y > 0:
            FinStr = damo.FindPicEpy(my_x - 80, my_y + 125, my_x + 140, my_y + 200, "可破坏.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                FinStr = damo.FindPicEpy(530, 561, 562, 593, "鞭子.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    damo.KeyPresspy(65)
                    damo.Delaypy(500)
                else:
                    damo.KeyPresspy(88)
                    damo.Delaypy(500)
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
        print('技能1')
        temp_name = ['弗利特','桑德尔','牛头王','路易斯','伊伽贝拉','赫德尔','冰','火','光','暗']
        for i in range(len(temp_name)):
            damo.KeyPresspyCharpy(jn_key[temp_name[i]])
            damo.Delaypy(jn_sf_time[temp_name[i]])
            jn_now_time[temp_name[i]] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    elif leixing == 2:
        print('技能2')
        temp_name = ['伊伽贝拉','冰','火','光','暗']
        for i in range(len(temp_name)):
            d1 = datetime.datetime.now()
            d2 = datetime.datetime.strptime(jn_now_time[temp_name[i]],'%Y-%m-%d %H:%M:%S')
            d3 = d1 - d2
            if d3.seconds > jn_time[temp_name[i]]:
                print('召唤:' + temp_name[i])
                damo.KeyPresspyCharpy(jn_key[temp_name[i]])
                damo.Delaypy(1200)
                jn_now_time[temp_name[i]] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
def 躲避地火():
    my_x_py = 10
    my_y_py = 195
    wp_x_py = -100
    wp_y_py = -60
    while True:
        my_x = 0
        my_y = 0
        wp_x = 0
        wp_y = 0
        FinStr = damo.FindPicEpy(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            my_x = int(pos[1])
            my_y = int(pos[2])
        FinStr = damo.FindPicEpy(0, 78, 799, 492, "地火.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            wp_x = int(pos[1])
            wp_y = int(pos[2])
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
        FinStr = damo.FindPicEpy(337, 29, 451, 97, "奖励.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            break
def fanhuichengzhen():
    try:
        while True:
            FinStr = damo.FindStrEpy(451, 427, 535, 501, "返回城镇", "e6c89b-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                intx = int(pos[1])
                inty = int(pos[2])
                damo.MoveTopy(intx + 10, inty - 10)
                damo.Delaypy(1000)
                damo.LeftClickpy()
                damo.Delaypy(1000)
                break
            else:
                damo.MoveTopy(1, 1)
                damo.Delaypy(500)
                damo.LeftClickpy()
                damo.Delaypy(500)
                damo.KeyPresspy(27)
                damo.Delaypy(2000)
    except:
        print("报错######清空游戏窗口失败")
def 清理游戏窗口():
    while True:
        FinStr = damo.FindStrEpy(195, 189, 260, 216, "我的信息", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            damo.MoveTopy(594, 127)
            damo.Delaypy(200)
            damo.LeftClickpy()
            damo.Delaypy(1000)
            break
        else:
            damo.KeyPresspy(27)
            damo.Delaypy(1000)
def 出售分解(ZZ):
    zizhuangshuliang = 0
    FinStr = damo.FindStrEpy(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        intx = int(pos[1])
        inty = int(pos[2])
        damo.MoveTopy(intx, inty)
        damo.Delaypy(200)
        damo.LeftClickpy()
        damo.Delaypy(1000)
        damo.MoveTopy(intx + 58, inty + 34)
        damo.Delaypy(200)
        damo.LeftClickpy()
        damo.Delaypy(3000)
        FinStr = damo.FindStrEpy(659, 477, 712, 498, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            damo.Delaypy(1000)
            #点击装备栏
            damo.MoveTopy(497, 245)
            damo.Delaypy(200)
            damo.LeftClickpy()
            damo.Delaypy(1000)
            #点击整理
            damo.MoveTopy(685, 485)
            damo.Delaypy(200)
            damo.LeftClickpy()
            damo.Delaypy(1000)
            #出售
            damo.MoveTopy(181, 522)
            damo.Delaypy(200)
            damo.LeftClickpy()
            damo.Delaypy(1000)
            y = 262
            x_py = 31
            y_py = 31
            no_zhuangbei = False
            for i in range(4):
                x = 474
                for j in range(8):
                    Color = damo.GetColorpy(x + 5, y)
                    if Color == '4c9bad':
                        #高级装备
                        damo.MoveTopy(x + 14, y + 14)
                        damo.Delaypy(200)
                        damo.LeftClickpy()
                        damo.Delaypy(1000)
                        damo.LeftClickpy()
                        damo.Delaypy(1000)
                    elif Color == '656565' or Color == '874747' or Color == '766c79':
                        #普通装备
                        damo.MoveTopy(x + 14, y + 14)
                        damo.Delaypy(200)
                        damo.LeftClickpy()
                        damo.Delaypy(1000)
                        damo.LeftClickpy()
                        damo.Delaypy(1000)
                    elif Color == 'ab83f7' or Color == 'b85bac':
                        #紫色装备
                        zizhuangshuliang += 1
                    elif Color == 'be00c0':
                        #粉色装备
                        pass
                    elif Color == '382c4e':
                        # 不可出售装备
                        pass
                    else:
                        print('没有装备')
                        no_zhuangbei = True
                        break
                    x += x_py
                if no_zhuangbei:
                    break
                y += y_py
            清理游戏窗口()
    if zizhuangshuliang == 0:
        return 0
    FinStr = damo.FindStrEpy(166, 53, 611, 249, "装备分解", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        intx = int(pos[1])
        inty = int(pos[2])
        damo.MoveTopy(intx, inty)
        damo.Delaypy(200)
        damo.LeftClickpy()
        damo.Delaypy(1000)
        damo.MoveTopy(intx + 58, inty + 55)
        damo.Delaypy(200)
        damo.LeftClickpy()
        damo.Delaypy(3000)
        FinStr = damo.FindStrEpy(659, 477, 712, 498, "整理", "ddc593-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            damo.MoveTopy(255, 350)
            damo.Delaypy(1000)
            #普通
            FinStr = damo.FindStrEpy(323, 370, 335, 382, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                damo.MoveTopy(323 + 5, 370 + 5)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            #高级
            FinStr = damo.FindStrEpy(323, 384, 335, 396, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                damo.MoveTopy(323 + 5, 384 + 5)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            #紫装
            FinStr = damo.FindStrEpy(323, 398, 335, 410, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                damo.MoveTopy(323 + 5, 398 + 5)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)
            #自身可穿戴装备
            FinStr = damo.FindStrEpy(323, 431, 335, 443, "勾选", "ffae00-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                pass
            else:
                damo.MoveTopy(323 + 5, 431 + 5)
                damo.Delaypy(200)
                damo.LeftClickpy()
                damo.Delaypy(1000)

            damo.MoveTopy(255, 350)
            damo.Delaypy(200)
            damo.LeftClickpy()
            damo.Delaypy(2000)
            FinStr = damo.FindStrEpy(316, 269, 480, 313, "缺少分解道具", "ffffff-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                清理游戏窗口()
                return 1
            else:
                damo.KeyPresspy(13)
                damo.Delaypy(4000)
                清理游戏窗口()
                return 1
def 学习技能():
    pass
def 安全模式():
    FinStr = damo.FindStrEpy(335, 319, 396, 350, "确定解除", "ddc593-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        pass
    FinStr = damo.FindStrEpy(312, 272, 483, 295, "解除安全模式", "ffffff-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        pass
#############################################主程式####################################################
#定义参数
jn_key = {'弗利特':'q','桑德尔':'w','牛头王':'e','路易斯':'r','伊伽贝拉':'t','召唤兽狂化':'y','鞭子':'a','赫德尔':'s','冰':'d','火':'f','光':'g','暗':'h'}
jn_time = {'伊伽贝拉':200,'冰':200,'火':200,'光':200,'暗':200}
jn_now_time = {'弗利特':'2018-03-30 21:44:09','桑德尔':'2018-03-30 21:44:09','牛头王':'2018-03-30 21:44:09','路易斯':'2018-03-30 21:44:09','伊伽贝拉':'2018-03-30 21:44:09','召唤兽狂化':'2018-03-30 21:44:09','鞭子':'2018-03-30 21:44:09','赫德尔':'2018-03-30 21:44:09','冰':'2018-03-30 21:44:09','火':'2018-03-30 21:44:09','光':'2018-03-30 21:44:09','暗':'2018-03-30 21:44:09'}
jn_sf_time ={'弗利特':1000,'桑德尔':1100,'牛头王':1500,'路易斯':1300,'伊伽贝拉':1300,'召唤兽狂化':900,'鞭子':200,'赫德尔':1000,'冰':1000,'火':1000,'光':1000,'暗':1000}
#初始化参数
maoxiandengji = 4
qinglibeibao_cishu = 5
fubencishu = 0

hwnd = damo.FindWindowpy("地下城与勇士", "地下城与勇士")
if hwnd > 0:
    damo.MoveWindowpy(hwnd, 0, 0)
    hwnd = damo.FindWindowpy("", "GLD.exe")
    if hwnd > 0:
        damo.MoveWindowpy(hwnd, 0, 600)
        damo.SetWindowSizepy(hwnd, 800, 170)
while True:
    FinStr = damo.FindStrEpy(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
    pos = FinStr.split('|')
    if int(pos[1]) > 0:
        出售分解(1)
        FinStr = damo.FindPicEpy(272, 483, 501, 544, "虚弱.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            print('虚弱等待')
            continue
        向右()
        while True:
            damo.Delaypy(200)
            FinStr = damo.FindStrEpy(509, 533, 583, 570, "练习模式", "ddc593-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                damo.Delaypy(1000)
                FinStr = damo.FindPicEpy(510, 366, 536, 395, "副本界面_格兰迪.bmp", "000000", "0.9", 0)
                pos = FinStr.split('|')
                if int(pos[1]) > 0:
                    for i in range(5):
                        damo.KeyPresspy(37)
                        damo.Delaypy(200)
                    for i in range(maoxiandengji - 1):
                        damo.KeyPresspy(39)
                        damo.Delaypy(200)
                    damo.KeyPresspy(32)
                    damo.Delaypy(200)
                    damo.KeyPresspy(32)
                    damo.Delaypy(3000)
                else:
                    damo.KeyPresspy(38)
                    damo.Delaypy(1000)
            FinStr = damo.FindStrEpy(593, 0, 691, 28, "格兰迪发电站", "ccc1a7-000000", 1)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                break

    xingwei = True
    guanqia = 0
    duobidihuo = False
    while True:
        damo.Delaypy(200)
        if guanqia == 0:
            guanqia = 检查关卡()
        if xingwei:
            print('关卡 = ' + str(guanqia))
            if guanqia > 0:
                if guanqia == 4:
                    damo.KeyPresspy(37)
                elif guanqia == 5:
                    damo.KeyPresspy(39)
                if guanqia > 1:
                    damo.KeyPresspyCharpy('a')
                    damo.Delaypy(800)
                    damo.KeyPresspyCharpy('y')
                    damo.Delaypy(1000)
                xingwei = False
            if guanqia == 1:
                技能(1)
            elif guanqia == 3:
                向右()
                damo.Delaypy(1500)
                弹起()
            elif guanqia == 5:
                向下()
                damo.Delaypy(2000)
                弹起()
            elif guanqia == 6:
                技能(2)
                右下()
                damo.Delaypy(2000)
                弹起()
            elif guanqia == 7:
                技能(2)
                duobidihuo = True
        FinStr = damo.FindPicEpy(718,25,795,105, "问号绿.bmp|问号黄.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            找门(guanqia)
            xingwei = True
            guanqia = 0
            continue
        elif guanqia == 6:
            color = damo.GetColorpy(766, 90)
            if color == "00ff00":
                找门(guanqia)
                xingwei = True
                #重新检查关卡,第七关除外
                guanqia += 1
                continue
        FinStr = damo.FindPicEpy(0,78,799,552, "可破坏.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            打石头()
        FinStr = damo.FindPicEpy(0, 78, 799, 552, "wp.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            捡取()
        FinStr = damo.FindPicEpy(337,29,451,97, "奖励.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            duobidihuo = False
            FinStr = damo.FindPicEpy(0, 78, 799, 552, "wp.bmp", "000000", "0.9", 0)
            pos = FinStr.split('|')
            if int(pos[1]) > 0:
                弹起()
                捡取()
        FinStr = damo.FindPicEpy(612, 132, 735, 164, "通关.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            duobidihuo = False
            弹起()
            捡取()
            弹起()
            color = damo.GetColorpy(339, 553)
            if color == "0b0b0b" or color == "333333":
                print('返回城镇')
                fanhuichengzhen()
                damo.Delaypy(3000)
                break
            else:
                if fubencishu > 4:
                    print('返回城镇')
                    fanhuichengzhen()
                    damo.Delaypy(3000)
                    fubencishu = 0
                    break
                else:
                    fubencishu += 1
                    damo.KeyPresspyCharpy('f10')
                    damo.Delaypy(5000)
                    break
        FinStr = damo.FindStrEpy(667, 27, 745, 51, "斯曼工业基地", "e6c89b-000000", 1)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            弹起()
            break
        #躲避
        FinStr = damo.FindPicEpy(0, 78, 799, 552, "my.bmp", "000000", "0.9", 0)
        pos = FinStr.split('|')
        if int(pos[1]) > 0:
            myX = int(pos[1])
            myY = int(pos[2])
            FinStr = damo.FindColorEpy(myX-100, myY+130,myX+120, myY+210, "ff0094-101010|ff00ff-101010", 1.0, 0)
            pos = FinStr.split('|')
            if int(pos[0]) > 0:
                rand = random.randint(1, 2)
                if rand == 1:
                    向上()
                    damo.Delaypy(1000)
                    弹起()
                elif rand == 2:
                    向下()
                    damo.Delaypy(1000)
                    弹起()
        if duobidihuo:
            躲避地火()
            技能(2)