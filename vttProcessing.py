#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import os
import re
#print("Author: https://github.com/MoChanBW/\n", "v2.0.3 ", "on 2020/6/14")
print("请在vtt文件目录内运行本程序...3秒后开始处理")
print("\n按Ctrl+C终止操作")
time.sleep(3)
dirs = os.listdir(os.getcwd())
k = 0
alldata=""
for files in dirs:
    matchObj = re.match(r'(.*).vtt', files, re.M | re.I)
    if matchObj:
        lr = open(matchObj.group(), mode='r', encoding='utf-8')
        data = lr.read(-1)
        lr.close()
        data = str(data)
        data=data.replace("WEBVTT","")
        alldata=alldata+data

lr = open("index.vtt", mode='w', encoding='utf-8')
alldata="WEBVTT\n" + alldata
lr.write(alldata)
lr.close()
print("完毕！")
fs = input("\n按回车键退出...\n")
print("再见！")
