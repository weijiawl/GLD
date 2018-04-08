#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ctypes
dll = ctypes.windll.LoadLibrary('SAFEDLL.dll')

class xgdx:
    def jieanquan(self,qq,qqpwd,shouji,xguer,xgmm,rkuer,rkmm):
        dll.SetKfUser('weijiawl'.encode("utf-8"))
        error = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        r = dll.SafeRemove(qq.encode("utf-8"),qqpwd.encode("utf-8"),shouji.encode("utf-8"),error,256,xguer.encode("utf-8"),xgmm.encode("utf-8"),rkuer.encode("utf-8"),rkmm.encode("utf-8"),2)
        if r == 1:
            return True
        return False
    def jiandanjieanquan(self,qq,xguer,xgmm):
        error = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        r = dll.SafeUp(qq.encode("utf-8"),error,256,xguer.encode("utf-8"),xgmm.encode("utf-8"))
        if r == 2:
            return True
        return False

