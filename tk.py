import tkinter
#!/usr/bin/python
#-*- coding: UTF-8 -*-
from tkinter.ttk import Treeview
import tkinter
from tkinter import *
import time
import configparser
import os
import win_tk
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
def get_ini(name, section, option):
    try:
        cf = configparser.ConfigParser()
        cf.read(name)
        temp = cf.get(section, option)
        return temp
    except:
        return ""
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
        xianshihang = ""
        ids = ""
        hao_path = get_ini('config/cfg.ini', '主配置', '账号路径')
        pc_name = os.environ['COMPUTERNAME']
        for ic in range(500):
            num = get_ini(hao_path, pc_name, str(ic + 1))
            if num != "":
                shijian = ""
                zhuangtai = ""
                dangqianjuese = ""
                num_arr = num.split('=')
                num_zt = get_ini('config/记录.ini', '封号', num_arr[0])
                if num_zt == "":
                    num_zt = get_ini('config/记录.ini', '制裁', num_arr[0])
                    if num_zt == "":
                        num_zt = get_ini('config/记录.ini', '完成', num_arr[0] + '_' + num_arr[2])
                        if num_zt == "":
                            num_zt = get_ini('config/记录.ini', '刷号记录', '当前账号')
                            if num_zt != "":
                                if num_zt == num_arr[0]:
                                    if xianshihang == "":
                                        xianshihang = num_zt
                                    num_zt = get_ini('config/记录.ini', '刷号记录', '当前大区')
                                    if num_zt == num_arr[2]:
                                        zhuangtai = "打印中"
                                        shijian = ""
                        else:
                            zhuangtai = "完成"
                            shijian = ""
                    else:
                        zhuangtai = "制裁"
                        shijian = num_zt
                else:
                    zhuangtai = "封号"
                    shijian = num_zt

                if zhuangtai == '完成':
                    dangqianjuese = num_arr[3]
                elif zhuangtai == '打印中':
                    dangqianjuese = get_ini('config/记录.ini', '刷号记录', "当前角色")
                else:
                    for i in range(int(num_arr[3])):
                        dangqianjuese_str = get_ini('config/记录.ini', '完成时间',num_arr[0] + '_' + num_arr[2] + '_' + str(i + 1))
                        if dangqianjuese_str != "":
                            dangqianjuese = str(i + 1)
                            break
                id = win_tk.tree.insert('', ic,values=[str(ic + 1), num_arr[0], num_arr[2], num_arr[3], dangqianjuese,zhuangtai, shijian])
                if ids == "":
                    if xianshihang == num_arr[0]:
                        ids = id
            else:
                break
        if ids == "":
            ids = id
        win_tk.tree.see(ids)
        set_ini("config/记录.ini", "更新", '刷新列表', 'False')
        gengxintongji()
    except:
        print('刷新列表失败')
def end_jincheng():
    command = 'taskkill /F /IM Login.exe'
    os.system(command)
    command = 'taskkill /F /IM Login.exe'
    os.system(command)
def text(temp):
    win_tk.lb.insert(END, temp + '\n')
    win_tk.lb.see(END)
def win():
    root = tkinter.Tk()
    root.geometry('800x310+0+601')
    root.resizable(False, False)
    root.title('疯子打印机V2.0')
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
    win_tk.tree.heading('c5', text='完成角色')
    win_tk.tree.heading('c6', text='状态')
    win_tk.tree.heading('c7', text='完成时间')
    win_tk.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
    # Treeview组件与垂直滚动条结合
    scrollBar.config(command=win_tk.tree.yview)
    #gengxinyihang()
    # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
    #Button(frams, text='打印机启动', command=t_start).pack(side=TOP, anchor=S, fill=NONE, expand=NO)
    Button(frams, text='打印机结束', command=end_jincheng).pack(side=TOP, anchor=S, fill=NONE, expand=NO)
    # Button(frams, text='Bottom').pack(side=TOP, anchor=S, fill=NONE , expand=NO)
    def donothing():
        os.system('TASKKILL /F /IM Login.exe"')
        root.destroy()
    root.protocol("WM_DELETE_WINDOW",donothing)
    root.mainloop()