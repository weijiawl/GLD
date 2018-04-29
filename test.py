# -*- coding: cp936 -*-
import ctypes
import string
import time
from ctypes import *  # ���� ctypes ��������ģ��
class HZ:
    def __init__(self,x,y):
        self.objdll = ctypes.windll.LoadLibrary('msdk.dll')
        self.hdl = self.objdll.M_Open(1)
        self.objdll.M_ResolutionUsed(self.hdl, x, y)
        print("open handle = " + str(self.hdl))
        time.sleep(3)  # sleep 3s ����ʱ����ʱ�ڼ佫���㵽���±�����������
    #-----------------------------------����----------------------------------
    # ����
    def KeyPresspy(self, KeyInt, Nbr):
        return self.objdll.M_KeyPress2(self.hdl, KeyInt, Nbr)
    # ��ס
    def KeyDownpy(self, KeyInt):
        return self.objdll.M_KeyDown2(self.hdl, KeyInt)
    #����
    def KeyUppy(self,KeyInt):
        return self.objdll.M_KeyUp2(self.hdl, KeyInt)
    #��ȡ����״̬��0=����1=����
    def GetKeyStatepy(self, KeyInt):
        return self.objdll.M_KeyState2(self.hdl, KeyInt)
    #�����ַ���
    def KeyPressStrpy(self,inputstr):
        # VbufWr = create_string_buffer(128)  #����һ���ɱ��ַ�������������Ϊ128
        # VbufWr.raw = inputstr
        # print(" WrData = " + VbufWr.raw)
        pWrBuf = c_char_p()  # ����һ��char��ָ�����
        pWrBuf = inputstr
        return self.objdll.M_KeyInputString(self.hdl, pWrBuf, len(inputstr)*2)
    #-----------------------------------���----------------------------------
    def MoveTopy(self,x,y,intx,inty):
        return self.objdll.M_MoveTo3(self.hdl, intx, inty)
    #����
    def LeftClickpy(self,Nbr):
        return self.objdll.M_LeftClick(self.hdl,Nbr)
    #˫�����
    def LeftDoubleClickpy(self, Nbr):
        return self.objdll.M_LeftDoubleClick(self.hdl, Nbr)
    #��ס���
    def LeftDownpy(self):
        return self.objdll.M_LeftDown(self.hdl)
    #�������
    def LeftUppy(self):
        return self.objdll.M_LeftUp(self.hdl)
    #�����Ҽ�
    def RightClickpy(self, Nbr):
        return self.objdll.M_RightClick(self.hdl, Nbr)
    #��ס�Ҽ�
    def RightDownpy(self):
        return self.objdll.M_RightDown(self.hdl)
    #�����Ҽ�
    def RightUppy(self):
        return self.objdll.M_RightUp(self.hdl)
# if __name__ == '__main__':
#     te = HZ()
#     print (te.MoveTopy(1920,1080,900,900))
