import time
import subprocess
import json
import os
import re

def cmd(command, sleep):
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, encoding="utf-8")
    time.sleep(sleep)  # 等ffprobe运行
    if subp.poll() == 0:
                # print(subp.communicate()[0])
        print("title:", json.loads(subp.communicate()[0])[
              "format"]["tags"]["title"])
        print("artist:", json.loads(subp.communicate()[0])[
              "format"]["tags"]["artist"])
        print("size:", json.loads(subp.communicate()[0])["format"]["size"])
        if int(json.loads(subp.communicate()[0])["format"]["size"]) < 20971520:
            return("无需切片")
        else:
            return("需要切片")
    else:
        cmd(command, sleep)  # 错误就重来
dirs = os.listdir(os.getcwd())
k = 0
q = 0
numfailed = 0
failedstr = []
qpstr = []
for files in dirs:
    matchObj = re.match(r'(.*).mp3', files, re.M | re.I)
    if matchObj:
        print(k+1, ": ", matchObj.group())
        command = "ffprobe -v quiet -of json -show_format "+'"'+matchObj.group()+'"'
        theReturn = cmd(command, 0.4)
        if theReturn == "失败":
            numfailed += 1
            failedstr.append(matchObj.group())
            print("失败:", "[", numfailed, "]", matchObj.group())
        elif theReturn == "需要切片":
            q += 1
            k+=1
            qpstr.append(matchObj.group())
            print("需要切片:", "[", q, "]:", matchObj.group())
        else:
            k += 1


if failedstr !=[]:
    print("失败的是:", failedstr)
if qpstr != []:
    print("需要切片的是:", qpstr)
print("正常读取",k,"首歌曲")

    


    

