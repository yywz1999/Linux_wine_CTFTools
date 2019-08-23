#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:W22,张灵灵

import os
import sys

#用来放exe应用程序的位置
Applications = [
    "/home/ling/CTF/编码解码/QR_Research/CQR.exe",
    "/home/ling/CTF/BurpSuite_pro_v2.1/burpsuite_pro_v2.1_BurpHelper.jar",
    "/home/ling/CTF/1.py",
    "/home/ling/CTF/1.hahah"
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

def file_extension(path): 
  return os.path.splitext(path)[1] 

if __name__ == "__main__":
    AppName = GetAppName(Applications)
    while True:
        for i in range(len(Applications)):
            print(AppName[i])
        try:
            Choose = GetUserChoose()
            file_tzm=file_extension(AppName[Choose])
            if(Choose <= len(Applications)-1):    
               if(file_tzm=='.exe'): 
                      OpenItem(Choose)
               elif(file_tzm=='.jar'):
                      OpenJar(Choose)
               elif(file_tzm=='.py'):
                      OpenPy(Choose)
               else:
                    print("----------------------------------\n\n\nUnsupported file types\n\n\n----------------------------------")
            else:print('[-]Error!')
        except:
            pass
