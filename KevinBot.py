import time
import os
import re
print("Author: https://github.com/MoChanBW/\n", "v1.0.1 ", "on 2020/6/13")
base = input(
    "请输入远程仓库目录(默认为'https://cdn.jsdelivr.net/gh/MoChanBW/CDN@master/APlayer/'):")
if base == '':
    base = 'https://cdn.jsdelivr.net/gh/MoChanBW/CDN@master/APlayer/'
print("请在mp3文件目录内运行...3秒后开始处理\n")
print("\n按Ctrl+C终止操作")
time.sleep(3)
f = open('aplayerMainController.js', mode='w', encoding='utf8')
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

js="const ap = new APlayer({\
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
    listMaxHeight: 10,\
    lrcType: 3,\
    audio: ["+strs+"]\
});\
function getDefaultCover() { \
    return 'https://cdn.jsdelivr.net/gh/MoChanBW/DPlayer-ReadyToUse@latest/assets/Cloud_Play_128px.png'}"
f.write(js)
f.close()
print("\n工作完毕！写入", k, "首歌曲\n\n输出的JS文件为: ", f.name)
fs=input("\n按回车键退出...")