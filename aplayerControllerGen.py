#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import os
import re
print("Author: https://github.com/MoChanBW/\n", "v2.0.3 ", "on 2020/6/14")
base = input(
    "请输入远程仓库目录\n(默认为'https://cdn.jsdelivr.net/gh/MoChanBW/CDN@latest/APlayer/'):\n")
if base == '':
    base = 'https://cdn.jsdelivr.net/gh/MoChanBW/CDN@latest/APlayer/'
print("请在mp3文件目录内运行本程序...3秒后开始处理")
print("\n按Ctrl+C终止操作")
time.sleep(3)

dirs = os.listdir(os.getcwd())
strs = ''
k = 0
for files in dirs:
    matchObj = re.match(r'(.*) - (.*?).mp3', files, re.M | re.I)
    if matchObj:
        #print("1: ", matchObj.group(1))
        #print("2: ", matchObj.group(2))

        print(k+1, ": ", matchObj.group())
        data = {
            'name': matchObj.group(2),
            'artist': matchObj.group(1),
            'url': base+matchObj.group(),
            'cover': base+matchObj.group().replace("mp3", "jpg"),
            'lrc': base+matchObj.group().replace("mp3", "lrc"),
            'theme': '#ebd0c2'
        }
        strs = strs + str(data) + ","
        k += 1
for files in dirs:
    matchObj = re.match(r'(.*) - (.*?).aac', files, re.M | re.I)
    if matchObj:
        #print("1: ", matchObj.group(1))
        #print("2: ", matchObj.group(2))

        print(k+1, ": ", matchObj.group())
        data = {
            'name': matchObj.group(2),
            'artist': matchObj.group(1),
            'url': base+matchObj.group(),
            'cover': base+matchObj.group().replace("mp3", "jpg"),
            'lrc': base+matchObj.group().replace("mp3", "lrc"),
            'theme': '#ebd0c2'
        }
        strs = strs + str(data) + ","
        k += 1
if k != 0:
    js = "const ap = new APlayer({\
    container: document.getElementById('aplayer'),\
    mini: false,\
    fixed: false,\
    autoplay: false,\
    theme: '#FADFA3',\
    loop: 'all',\
    order: 'random',\
    preload: 'auto',\
    volume: 0.7,\
    mutex: true,\
    listFolded: false,\
    listMaxHeight: 90,\
    lrcType: 3,\
    audio: ["+strs+"]\
    });"
    f = open('aplayerMainController.js', mode='w', encoding='utf8')
    f.write(js)
    f.close()
    print("\n工作完毕！写入", k, "首歌曲\n\n输出的JS文件为: ", f.name)
else:
    print("\n没有找到符合条件的歌曲文件喵~\n")

da = input("要转换lrc文件的编码吗？(Y/n):")
k = ''
if da not in "Nn" or da == '':
    k = 0
    for files in dirs:
        matchObj = re.match(r'(.*) - (.*?).lrc', files, re.M | re.I)
        if matchObj:
            lr = open(matchObj.group(), mode='r+', encoding='gb18030')
            try:
                data = lr.read(-1)
            except UnicodeDecodeError:
                lr.close()
                lr = open(matchObj.group(), mode='r+', encoding='utf8')
                data = lr.read(-1)

            data = str(data)
            lr.close()
            lr = open(matchObj.group(), mode='w', encoding='utf-8')
            lr.write(data)
            lr.close()
            print(k+1, ": ", matchObj.group())
            k += 1

if k != 0:
    print("\n工作完毕！写入",k, "份歌词")
else:

    print("\n没有找到符合条件的歌词文件喵~")
fs = input("\n按回车键退出...\n")
print("再见！")
