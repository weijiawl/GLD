#!/usr/bin/python
#-*- coding: UTF-8 -*-
import public
from tkinter.ttk import Treeview
import tkinter
from tkinter import *
import configparser
import os
import win_tk
import psutil
import datetime
import time
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
def get_ini(name, section, option,moren):
    try:
        cf = configparser.ConfigParser()
        cf.read(name)
        temp = cf.get(section, option)
        return temp
    except:
        return moren
def gengxintongji():
    F_hao = 0
    Z_hao = 0
    W_hao = 0
    try:
        config = configparser.ConfigParser()
        config.read("config/记录.ini")
        ret = config.options('封号')
        F_hao = len(ret)
    except:
        F_hao = 0
    try:
        config = configparser.ConfigParser()
        config.read("config/记录.ini")
        ret = config.options('制裁')
        Z_hao = len(ret)
    except:
        Z_hao = 0
    try:
        config = configparser.ConfigParser()
        config.read("config/记录.ini")
        ret = config.options('完成时间')
        W_hao = len(ret)
    except:
        W_hao = 0
    win_tk.lb2["text"] = '封号:' + str(F_hao) + '制裁:' + str(Z_hao) + '完成角色:' + str(W_hao)
def trickit():
    print('刷新列表')
    try:
        temp = win_tk.tree.get_children("")
        if len(temp) > 0:
            for _ in map(win_tk.tree.delete, win_tk.tree.get_children("")):
                pass
        xianshihang = 0
        hao_path = get_ini('config/cfg.ini', '主配置', '账号路径', "")
        pc_name = get_ini('config/cfg.ini', '软件配置', 'pc_name', "")
        inde = 0
        for ic in range(500):
            num = get_ini(hao_path, pc_name, str(ic + 1),"")
            if num != "":
                num_arr = num.split('=')
                for i in range(int(num_arr[3])):
                    dangqianjuese = ""
                    zhuangtai = ""
                    shijian = ""
                    temp_ret = get_ini('config/记录.ini', '封号', num_arr[0], "")
                    if temp_ret != "":
                        zhuangtai = '封号'
                        shijian = temp_ret
                    else:
                        temp_ret = get_ini('config/记录.ini', '制裁', num_arr[0], "")
                        if temp_ret != "":
                            zhuangtai = '制裁'
                            shijian = temp_ret
                        else:
                            temp_ret = get_ini('config/记录.ini', '完成时间',num_arr[0] + '_' + num_arr[2] + '_' + str(i + 1), "")
                            if temp_ret != "":
                                zhuangtai = '完成'
                                shijian = temp_ret
                            else:
                                temp_ret = get_ini('config/记录.ini', '刷号记录', '当前账号',"")
                                if temp_ret == num_arr[0]:
                                    temp_ret = get_ini('config/记录.ini', '刷号记录', '当前大区',"")
                                    if temp_ret == num_arr[2]:
                                        temp_ret = get_ini('config/记录.ini', '刷号记录', '当前角色',"")
                                        if temp_ret == str(i + 1):
                                            zhuangtai = '打印中'
                    id = win_tk.tree.insert('', inde, values=[str(inde + 1), num_arr[0], num_arr[2], str(i + 1), dangqianjuese,zhuangtai, shijian])
                    if zhuangtai == '封号':
                        win_tk.tree.item(id, tags=('hongse'))
                    elif zhuangtai == '制裁':
                        win_tk.tree.item(id, tags=('zise'))
                    elif zhuangtai == '完成':
                        win_tk.tree.item(id, tags=('lvse'))
                    elif zhuangtai == '打印中':
                        win_tk.tree.item(id, tags=('lanse'))
                        xianshihang = id
                    win_tk.tree.tag_configure('hongse', background='#FF0000')
                    win_tk.tree.tag_configure('zise', background='#9932CC')
                    win_tk.tree.tag_configure('lvse', background='#00FF00')
                    win_tk.tree.tag_configure('lanse', background='#7B68EE')
                    inde += 1
            else:
                break
        win_tk.tree.see(xianshihang)
        gengxintongji()
    except:
        print('刷新列表失败')
def kill_svchost():
    for i in psutil.pids():
        p = psutil.Process(i)
        if p.name() == 'svchost.exe':
            try:
                print(p.username())
                p_user = p.username()
                if p_user.find('Administrator') >= 0:
                    p.kill()
            except:
                print('访问错误')
def end_jincheng():
    os.system('taskkill /F /IM Login.exe')
    os.system('taskkill /F /IM Login.exe')
    #os.system('taskkill /F /IM DNF.exe')
    os.system('taskkill /F /IM tgp_daemon.exe')
    os.system('taskkill /F /IM TPHelper.exe')
    kill_svchost()
    os.system('结束.bat')
def end_exit():
    public.k = 2
def text(temp):
    d2 = datetime.datetime.now().strftime('%d %H:%M:%S')
    win_tk.lb.insert(END, d2 + ' ' + temp + '\n')
    win_tk.lb.see(END)
def win():
    root = tkinter.Tk()
    root.geometry('800x310+0+601')
    root.resizable(False, False)
    #'疯子打印机0819.1.'
    root.title('疯子打印机V0823.A')
    frame = Frame(root)
    frame.place(x=0, y=10, width=610, height=300)
    # 滚动条
    scrollBar = tkinter.Scrollbar(frame)
    scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    # Treeview组件，6列，显示表头，带垂直滚动条
    win_tk.tree = Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'), show="headings",
                    yscrollcommand=scrollBar.set)
    frams = Frame(root)
    frams.place(x=610, y=10, width=80, height=300)
    framt = Frame(root)
    scrollBat = tkinter.Scrollbar(framt)
    scrollBat.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    framt.place(x=610, y=70, width=190, height=230)
    win_tk.lb = Text(framt, height=16, width=24, yscrollcommand=scrollBat.set)
    win_tk.lb.pack(fill=tkinter.X, side=tkinter.BOTTOM)
    win_tk.lb2 = Label(framt, foreground='red', text='封号:   制裁:   完成角色: ', )
    win_tk.lb2.pack()
    # 设置每列宽度和对齐方式
    win_tk.tree.column('c1', width=60, anchor='center')
    win_tk.tree.column('c2', width=100, anchor='center')
    win_tk.tree.column('c3', width=80, anchor='center')
    win_tk.tree.column('c4', width=60, anchor='center')
    win_tk.tree.column('c5', width=60, anchor='center')
    win_tk.tree.column('c6', width=90, anchor='center')
    win_tk.tree.column('c7', width=150, anchor='center')
    # 设置每列表头标题文本
    win_tk.tree.heading('c1', text='编号')
    win_tk.tree.heading('c2', text='账号')
    win_tk.tree.heading('c3', text='大区')
    win_tk.tree.heading('c4', text='角色')
    win_tk.tree.heading('c5', text=' ')
    win_tk.tree.heading('c6', text='状态')
    win_tk.tree.heading('c7', text='完成时间')
    win_tk.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
    # Treeview组件与垂直滚动条结合
    scrollBar.config(command=win_tk.tree.yview)
    # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
    #Button(frams, text='打印机启动', command=t_start).pack(side=TOP, anchor=S, fill=NONE, expand=NO)
    Button(frams, text='打印机结束', command=end_exit).pack(side=TOP, anchor=S, fill=NONE, expand=NO)
    # Button(frams, text='Bottom').pack(side=TOP, anchor=S, fill=NONE , expand=NO)

    root.protocol("WM_DELETE_WINDOW",end_exit)
    root.mainloop()