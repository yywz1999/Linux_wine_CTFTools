#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:W22

import os
import sys

#用来放exe应用程序的位置
Applications = [
    "/home/w22/CTF_Tools/CTF_Tools_3/编码解码/QR_Research/CQR.exe",
    "/home/w22/CTF_Tools/CTF_Tools_1/编码与密码/密码/PYG密码学综合工具/PYG_TOOLS_VER5.exe",
    "/home/w22/CTF_Tools/CTF_Tools_1/编码与密码/密码/RSA/RSA大整数分解/yafu-1.34/yafu-Win32.exe",
    "/home/w22/CTF_Tools/Extended/UPXUnPacKer/UPXUnPacKer.V0.3.By.skylly.exe",
    "/home/w22/CTF_Tools/CTF_Tools_3/信息隐藏/audacity-win-2.1.0/audacity.exe",
    "/home/w22/CTF_Tools/CTF_Tools_3/信息隐藏/MP3Stego_1_1_18/MP3Stego/MP3StegoEncode.exe",
    "/home/w22/CTF_Tools/CTF_Tools_3/信息隐藏/MP3Stego_1_1_18/MP3Stego/MP3StegoDecode.exe"
]


def GetAppName(List):
    Name = []
    for i in range(len(List)):
        Name.append(str(i)+'. '+str(List[i]).split('/')[-1])
    return Name



def GetUserChoose():
    choose = raw_input("Please select the tool you want to use to Num: ")
    return int(choose)

def OpenItem(Num):
    cmd = "wine "+Applications[Num]+" &"
    os.system(cmd)
    return 0;

def OpenJar(Num):
    cmd = "java -jar "+Applications[Num]+" &"
    os.system(cmd)
    return 0;

def OpenPy(Num):
    cmd = "python "+Applications[Num]+" &"
    os.system(cmd)
    return 0;

if __name__ == "__main__":
    AppName = GetAppName(Applications)
    while True:
        for i in range(len(Applications)):
            print(AppName[i])
        try:
            Choose = GetUserChoose()
            if (Choose <= len(Applications)-1):
                OpenItem(Choose)
            else:
                print('[-]Error!')
        except:
            pass
