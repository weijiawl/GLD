# -*- coding: cp936 -*-
import ctypes
import tk
from ctypes import *  # ���� ctypes ��������ģ��
class HZ:
    def __init__(self,x,y,nbr,VID=0x0,PID=0x0):
        self.objdll = ctypes.windll.LoadLibrary('dk.dll')
        if VID > 0x0:
            self.hdl = self.objdll.M_Open_VidPid(VID,PID + nbr)
            b = bytes([108,100,119,108,50,48,49,56,47,42,46])
            self.ret = self.objdll.M_VerifyUserData(self.hdl, 11, b)
            if self.ret == 0:
                self.objdll.M_ResolutionUsed(self.hdl, x, y)
                #print('����˫ͷ���� ID = ' + str(self.hdl))
                tk.text('����˫ͷ���� ID = ' + str(self.hdl))
            else:
                #print('���ַǷ�����')
                tk.text('���ַǷ�����')
            #self.objdll.M_ResolutionUsed(self.hdl, x, y)
            #tk.text('����˫ͷ���� ID = ' + str(self.hdl))
        else:
            self.hdl = self.objdll.M_Open(nbr)
            self.objdll.M_ResolutionUsed(self.hdl, x, y)
            #tk.text('���ֵ�ͷ���� ID = self.hdl')
    #-----------------------------------����----------------------------------
    # ����
    def KJDfekiHDh(self, KeyInt, Nbr):
        return self.objdll.M_KeyPress2(self.hdl, KeyInt, Nbr)
    # ��ס
    def LKDFemrrh(self, KeyInt):
        return self.objdll.M_KeyDown2(self.hdl, KeyInt)
    #����
    def LJDFnmeFSD(self,KeyInt):
        return self.objdll.M_KeyUp2(self.hdl, KeyInt)
    #��ȡ����״̬��0=����1=����
    def CJdsfDH(self, KeyInt):
        return self.objdll.M_KeyState2(self.hdl, KeyInt)
    #�����ַ���
    def LbferJhd(self,inputstr):
        # VbufWr = create_string_buffer(128)  #����һ���ɱ��ַ�������������Ϊ128
        # VbufWr.raw = inputstr
        # print(" WrData = " + VbufWr.raw)
        pWrBuf = c_char_p()  # ����һ��char��ָ�����
        pWrBuf = inputstr
        return self.objdll.M_KeyInputString(self.hdl, pWrBuf, len(inputstr)*2)
    #-----------------------------------���----------------------------------
    #�ƶ�
    def UIKBudj(self,intx,inty):
        return self.objdll.M_MoveTo3(self.hdl, intx, inty)
    #����
    def PPWEbxbar(self,Nbr):
        return self.objdll.M_LeftClick(self.hdl,Nbr)
    #˫�����
    def KFNVCnehsdg(self, Nbr):
        return self.objdll.M_LeftDoubleClick(self.hdl, Nbr)
    #��ס���
    def cndjGdsbSdg(self):
        return self.objdll.M_LeftDown(self.hdl)
    #�������
    def mboHdjGsV(self):
        return self.objdll.M_LeftUp(self.hdl)
    #�����Ҽ�
    def XKkncvhe(self, Nbr):
        return self.objdll.M_RightClick(self.hdl, Nbr)
    #��ס�Ҽ�
    def jfgknrtBG(self):
        return self.objdll.M_RightDown(self.hdl)
    #�����Ҽ�
    def MNXjhfejkhV(self):
        return self.objdll.M_RightUp(self.hdl)
if __name__ == '__main__':
    te = HZ(1366, 768, 0, 0xC216, 0x102)