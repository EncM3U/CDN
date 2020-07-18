import os
import chardet
import re
k = 0
p = 0

strs = ""
dirs = os.listdir(os.getcwd())
for files in dirs:
    matchObj = re.match(r'(.*).lrc', files, re.M | re.I)
    if matchObj:
        detcd = open(matchObj.group(), mode="rb")
        enc = chardet.detect(detcd.read())["encoding"]
        detcd.close()
        try:
            lr = open(matchObj.group(), mode='r', encoding="utf-8")
            data = lr.read(-1)
        except UnicodeDecodeError:
            lr.close()
        lr.close()
        strs=strs+str(data)+"\n\n"
AL=open("ALLlrc.txt",mode="w",encoding="utf-8")
AL.write(strs)
AL.close()
