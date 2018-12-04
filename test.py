# -*- coding: cp936 -*-
import ctypes
import tk
from ctypes import *  # 导入 ctypes 库中所有模块
class HZ:
    def __init__(self,x,y,nbr,VID=0x0,PID=0x0):
        self.objdll = ctypes.windll.LoadLibrary('dk.dll')
        if VID > 0x0:
            self.hdl = self.objdll.M_Open_VidPid(VID,PID + nbr)
            b = bytes([108,100,119,108,50,48,49,56,47,42,46])
            self.ret = self.objdll.M_VerifyUserData(self.hdl, 11, b)
            if self.ret == 0:
                self.objdll.M_ResolutionUsed(self.hdl, x, y)
                #print('发现双头盒子 ID = ' + str(self.hdl))
                tk.text('发现双头盒子 ID = ' + str(self.hdl))
            else:
                #print('发现非法盒子')
                tk.text('发现非法盒子')
            #self.objdll.M_ResolutionUsed(self.hdl, x, y)
            #tk.text('发现双头盒子 ID = ' + str(self.hdl))
        else:
            self.hdl = self.objdll.M_Open(nbr)
            self.objdll.M_ResolutionUsed(self.hdl, x, y)
            #tk.text('发现单头盒子 ID = self.hdl')
    #-----------------------------------键盘----------------------------------
    # 单击
    def KJDfekiHDh(self, KeyInt, Nbr):
        return self.objdll.M_KeyPress2(self.hdl, KeyInt, Nbr)
    # 按住
    def LKDFemrrh(self, KeyInt):
        return self.objdll.M_KeyDown2(self.hdl, KeyInt)
    #弹起
    def LJDFnmeFSD(self,KeyInt):
        return self.objdll.M_KeyUp2(self.hdl, KeyInt)
    #读取按键状态，0=弹起，1=按下
    def CJdsfDH(self, KeyInt):
        return self.objdll.M_KeyState2(self.hdl, KeyInt)
    #输入字符串
    def LbferJhd(self,inputstr):
        # VbufWr = create_string_buffer(128)  #定义一个可变字符串变量，长度为128
        # VbufWr.raw = inputstr
        # print(" WrData = " + VbufWr.raw)
        pWrBuf = c_char_p()  # 定义一个char型指针变量
        pWrBuf = inputstr
        return self.objdll.M_KeyInputString(self.hdl, pWrBuf, len(inputstr)*2)
    #-----------------------------------鼠标----------------------------------
    #移动
    def UIKBudj(self,intx,inty):
        return self.objdll.M_MoveTo3(self.hdl, intx, inty)
    #单击
    def PPWEbxbar(self,Nbr):
        return self.objdll.M_LeftClick(self.hdl,Nbr)
    #双击左键
    def KFNVCnehsdg(self, Nbr):
        return self.objdll.M_LeftDoubleClick(self.hdl, Nbr)
    #按住左键
    def cndjGdsbSdg(self):
        return self.objdll.M_LeftDown(self.hdl)
    #弹起左键
    def mboHdjGsV(self):
        return self.objdll.M_LeftUp(self.hdl)
    #单击右键
    def XKkncvhe(self, Nbr):
        return self.objdll.M_RightClick(self.hdl, Nbr)
    #按住右键
    def jfgknrtBG(self):
        return self.objdll.M_RightDown(self.hdl)
    #弹起右键
    def MNXjhfejkhV(self):
        return self.objdll.M_RightUp(self.hdl)
if __name__ == '__main__':
    te = HZ(1366, 768, 0, 0xC216, 0x102)