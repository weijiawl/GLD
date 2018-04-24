#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import win32com.client
import ctypes
dll = ctypes.windll.LoadLibrary(os.getcwd() + '/testgame.dll' )
dll.SetDllPathW(os.getcwd() + '/wiwl.dll',1)
dw = win32com.client.Dispatch('tp.ten')
print(dw.oirtfwRuyKtW())
class bw():
    def __init__(self):
        self.dwreg = dw.RpoLrDm("weijiawlb1956e24a37f27f5cb5a7e139c2ecb2a", "python")
        dw.yUfk(os.getcwd() + "/Image")
        dw.MoodklurTCcT(0, os.getcwd() + "/soft.txt")
        dw.eqvC(0)
        try:
            #盾
            # dwreg = dw.fDcGGErqtSAZQ(1,'f1')
            # if dwreg != 1:
            #     print("驱动盾失败")
            #     input()
            #模拟方式4/2/5
            dwreg = dw.pcGYt(2)
            if dwreg != 1:
                print("驱动加载失败")
                input()
            #鼠标真实模拟
            dwreg = dw.VeEHgIhLMHXhfit(2, 12, 22)
            if dwreg != 1:
                print("驱动加载失败")
                input()
            #键盘真实模拟
            dwreg = dw.sksVkrIG(1)
            if dwreg != 1:
                print("驱动加载失败")
                input()
            # dwreg = dw.iMkvZyS('normal',200)
            # if dwreg != 1:
            #     print("驱动加载失败")
            #     input()
            # dwreg = dw.ikewGCvVxiZiv('normal',50)
            # if dwreg != 1:
            #     print("驱动加载失败")
            #     input()
        except:
            print("驱动加载失败")
            input()
        #print("插件版本 = " + dw.oirtfwRuyKtW())
    #############################################鼠标类####################################################
    #鼠标移动到[1:成功,0:失败]
    def MoveTopy(self,x,y):
        return dw.PUvSaRBFFdi(x,y)
    #点击鼠标左键[1:成功,0:失败]
    def LeftClickpy(self):
        return dw.AgGujQrdLvVJF()
    #双击鼠标左键
    def LeftDoubleClickpy(self):
        return dw.QseMw()
    #按住鼠标左键
    def LeftDownpy(self):
        return dw.TCqU()
    #弹起鼠标左键
    def LeftUppy(self):
        return dw.RUenttIIVrXr()
    #点击鼠标右键
    def RightClickpy(self):
        return dw.encDhYQe()
    #按住鼠标右键
    def RightDownpy(self):
        return dw.NmofLRmNukMjMF()
    #弹起鼠标右键
    def RightUppy(self):
        return dw.uRaoRiNkUn()
    #鼠标动作模拟真实操作,带移动轨迹,以及点击延时随机.
    def EnableRealMousepy(self,en,mousedelay,mousestep):
        return dw.VeEHgIhLMHXhfit(en,mousedelay,mousestep)
    #设置鼠标单击或者双击时,鼠标按下和弹起的时间间隔。高级用户使用。某些窗口可能需要调整这个参数才可以正常点击。
    def SetMouseDelaypy(self,type,delay):
        return dw.iMkvZyS(type,delay)
    #############################################键盘类####################################################
    #点击键盘
    def KeyPresspy(self,vk):
        return dw.dFcAmZglfo(vk)
    #按住键盘
    def KeyDownpy(self,vk):
        return dw.VsMX(vk)
    #弹起键盘
    def KeyUppy(self,vk):
        return dw.WFvHJfTAusG(vk)
    #按下指定的虚拟键码
    def KeyPresspyCharpy(self,key_str):
        return dw.zeBZsTU(key_str)
    # 键盘顺序输入
    def KeyPressStrpy(self,key_str,delay):
        return dw.KlKvLfWLhDvXzL(key_str,delay)
    #设置前台键鼠的模拟方式
    def SetSimModepy(self,mode):
        return dw.pcGYt(mode)
    #获取指定的按键状态.(前台信息,不是后台)
    def GetKeyStatepy(self,vk):
        return dw.HjqxV(vk)
    #按住指定的虚拟键码
    def KeyDownCharpy(self,key_str):
        return dw.wXwRT(key_str)
    #弹起指定的虚拟键码
    def KeyUpCharpy(self,key_str):
        return dw.XcTGEBRbaDAaeV(key_str)
    #############################################图色类####################################################
    def FindColorBlockExpy(self,x1,y1,x2,y2,color,sim,count,width,height):
        return dw.kKmdWjFt(x1,y1,x2,y2,color,sim,count,width,height)
    #找图
    def FindPicEpy(self,x1,y1,x2,y2,pic_name,delta_color,sim,dir):
        return dw.wjeZTZcz(x1,y1,x2,y2,pic_name,delta_color,sim,dir)
    #查找指定区域内的所有颜色块
    def FindColorBlockExpy(self,x1,y1,x2,y2,color,sim,count,width,height):
        return dw.kKmdWjFt(x1,y1,x2,y2,color,sim,count,width,height)
    #获取(x,y)的颜色
    def GetColorpy(self,x,y):
        return dw.qxAPybC(x,y)
    #在屏幕范围(x1,y1,x2,y2)内,查找string(可以是任意个字符串的组合),并返回符合color_format的坐标位置,相似度sim同Ocr接口描述
    def FindStrEpy(self,x1,y1,x2,y2,str,color,sim):
        return dw.uTTnPrSfie(x1,y1,x2,y2,str,color,sim)
    #识别屏幕范围(x1,y1,x2,y2)内符合color_format的字符串,并且相似度为sim,sim取值范围(0.1-1.0),
    def Ocrpy(self,x1,y1,x2,y2,color,sim):
        return dw.FBFUq(x1,y1,x2,y2,color,sim)
    #截图
    def Capturepy(self,x1,y1,x2,y2,file):
        return dw.lojyZMXGByK(x1,y1,x2,y2,file)
    #截图
    def CaptureJpgpy(self,x1,y1,x2,y2,file,quality):
        return dw.chfCmKukvYbBrs(x1,y1,x2,y2,file,quality)
    #查找指定区域内的所有颜色,颜色格式"RRGGBB-DRDGDB",
    def FindColorEpy(self,x1,y1,x2,y2,color,sim,dir):
        return dw.FmuaGuTZDP(x1,y1,x2,y2,color,sim,dir)
    #############################################窗口类####################################################
    #查找符合类名或者标题名的顶层可见窗口
    def FindWindowpy(self,class_name,title_name):
        return dw.XxZQDJhKvf(class_name,title_name)
    #移动指定窗口到指定位置
    def MoveWindowpy(self,hwnd,x,y):
        return dw.RNuCT(hwnd,x,y)
    #向指定窗口发送文本数据
    def SendStringpy(self,hwnd,strs):
        return dw.kCiSzKsz(hwnd,strs)
    #设置窗口的大小
    def SetWindowSizepy(self,hwnd,width,height):
        return dw.XoMdHQXl(hwnd,width,height)
    #设置窗口的状态
    def SetWindowStatepy(self,hwnd,flag):
        return dw.MBghJbHdCA(hwnd,flag)
    #############################################系统类####################################################
    #延时
    def Delaypy(self,mis):
        return dw.WUgpBX(mis)
    #运行指定的应用程序
    def RunApppy(self,path,mode):
        return dw.YCxTcNnrgFjR(path,mode)
    #获取屏幕宽度
    def GetScreenWidthpy(self):
        return dw.IkHtfdKQh()
    #获取屏幕高度
    def GetScreenHeightpy(self):
        return dw.YDvVC()
    def TerminateProcesspy(self,pid):
        return dw.ByygUE(pid)
    def EnumProcesspy(self,name):
        return dw.jjuXyhE(name)
    def DmGuardpy(self,enable,type):
        return dw.fDcGGErqtSAZQ(enable,type)