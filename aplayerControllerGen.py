# -*- coding: UTF-8 -*-
import time
import os
import re
import subprocess
import json
import chardet
import PySimpleGUI as sg

print("Author: https://github.com/MoChanBW/", "v4.0.1 ", "on 2020/6/26")


def musicConverter(allMusicInDict):
    base = input(
        "请输入音乐所在的远程仓库目录\n(默认为'https://cdn.jsdelivr.net/gh/MoChanBW/CDN@latest/APlayer/'):\n")
    if base == '':
        base = 'https://cdn.jsdelivr.net/gh/MoChanBW/CDN@latest/APlayer/'
    time.sleep(1)
    strs = ""
    k = 0
    # {theTitle:{"Artist":theArtist,"Name":theName,"Slice":Boolean},theTitle:{"Artist":theArtist,"Name":theName,"Slice":Boolean}}
    for keys in allMusicInDict:
        if allMusicInDict[keys]["Slice"]:
            command = "ffmpeg -i "+'"' + \
                allMusicInDict[keys]["Name"]+'"'+' -b:a 280k "' + \
                allMusicInDict[keys]["Name"].replace(".mp3", "")+'(280k).mp3"'
            print("正在以280k码率重编码...", keys)
            # print(command)
            subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, encoding="utf-8")
            time.sleep(8)  # 等ffmpeg运行
            if subp.poll() == 0:
                print("subp.communicate()[0]", subp.communicate()[0])
                print(
                    "subp.poll()=0: "+allMusicInDict[keys]["Name"].replace(".mp3", "")+'(280k).mp3')
                data = {
                    'name': keys,
                    'artist': allMusicInDict[keys]["Artist"],
                    'url': base+allMusicInDict[keys]["Name"].replace(".mp3", "")+'(280k).mp3',
                    'cover': "",
                    'lrc': "",
                    'album': allMusicInDict[keys]["Album"],
                }
                strs = strs + str(data) + ","
                k += 1
                print(allMusicInDict[keys]["Name"])
                print(data)
            else:
                print(subp.communicate()[0])
                print("else:", allMusicInDict[keys]["Name"].replace(
                    ".mp3", "")+'(280k).mp3')
                data = {
                    'name': keys,
                    'artist': allMusicInDict[keys]["Artist"],
                    'url': base+allMusicInDict[keys]["Name"].replace(".mp3", "")+'(280k).mp3',
                    'cover': "",
                    'lrc': "",
                    'album': allMusicInDict[keys]["Album"],
                }
                strs = strs + str(data) + ","
                k += 1
                # print(allMusicInDict[keys]["Name"])
                # print(data)
        else:
            data = {
                'name': keys,
                'artist': allMusicInDict[keys]["Artist"],
                'url': base+allMusicInDict[keys]["Name"],
                'cover': "",
                'lrc': "",
                'album': allMusicInDict[keys]["Album"],
            }
            strs = strs + str(data) + ","
            k += 1

    if k != 0:
        js = """
        var ap = new APlayer({
            container: document.getElementById('aplayer'),
            mini: false,
            autoplay: true,
            theme: '#FADFA3',
            loop: 'all',
            order: 'random',
            preload: 'auto',
            volume: 0.7,
            mutex: true,
            lrcType: 1,
            listFolded: false,
            audio: ["""+strs+"""]
            });
            var theLIST = ap.list.audios;
        ap.list["index"];
        console.log(theLIST);
        var ShowList = 0;
        ap.on("listshow", function () {
            ShowList = 1;
            document.getElementById("aplayer").style = "top:0;position:fixed;overflow-y:auto;";
        });
        ap.on("listhide", function () {
            ShowList = 0;
            document.getElementById("aplayer").style = "top:1;position:fixed;overflow-y:auto;";
        });
        var miniswitcherON = 0;
        document.getElementsByClassName("aplayer-miniswitcher")[0].onclick =
            function () {
                if (miniswitcherON == 0) {
                    miniswitcherON = 1;; //现状态
                    if (ShowList) {
                        window.setTimeout(function () {
                            document.getElementById("aplayer").style =
                                "top:0;position:fixed;overflow-y:auto;";
                        }, 300);
                    } else {
                        document.getElementById("aplayer").style = "top:1;position:fixed;overflow-y:auto;";
                    }
                } else {
                    miniswitcherON = 0; //现状态
                    document.getElementById("aplayer").style = "top:1;position:fixed;overflow-y:auto;";
                }
            };
        ap.on("loadstart", function () {
            if (ap.list.audios[ap.list["index"]].lrc == "" && (ap.list.audios[ap.list["index"]].cover == "" ||
                    ap.list.audios[ap.list["index"]].cover == undefined)) {
                console.log("undefine yes")
                var Name = theLIST[ap.list["index"]].name;
                var Album = theLIST[ap.list["index"]].album;
                var Artist = theLIST[ap.list["index"]].artist;
                axios.get('https://api.mochanbw.cn/QMapi/search', {
                        params: {
                            key: Artist + " " + Name + " " + Album
                        }
                    })
                    .then(function (response) {
                        var theSongmid = response.data.data.list[0].songmid;
                        var theAlbummid = response.data.data.list[0].albummid;
                        theLIST[ap.list["index"]].cover =
                            "https://y.gtimg.cn/music/photo_new/T002R300x300M000" + theAlbummid +
                            ".jpg";
                        axios.get('https://api.mochanbw.cn/QMapi/lyric', {
                                params: {
                                    songmid: theSongmid
                                }
                            })
                            .then(function (response) {
                                theLIST[ap.list["index"]].lrc = response.data.data.lyric;
                                let ID = ap.list["index"];
                                ap.list.clear();
                                ap.list.add(theLIST);
                                ap.list.switch(ID);

                            });

                    });


            }
        });
            """
        f = open('aplayerMainController.js', mode='w', encoding='utf-8')
        f.write(js)
        f.close()
        jsfixed = js.replace("listFolded: false", "listFolded: true")
        js = ""
        jsfixed = jsfixed.replace("autoplay: true", "autoplay: false")
        jsfixed = jsfixed.replace("mini: false", "fixed: true")
        fixed = open('aplayerMainFixedController.js',
                     mode='w', encoding='utf-8')
        fixed.write(jsfixed)
        jsfixed = ""
        fixed.close()
        print("\n工作完毕！写入", k, "首歌曲\n\n输出的JS文件为: ", f.name, "和", fixed.name)
    else:
        print("\n没有找到符合条件的歌曲文件喵~\n")


def lrcEncodingConvertToUTF8(dirs):
    k = 0
    p = 0
    numfailed = 0
    da = input("要将lrc文件编码转换为utf-8吗？(Y/n):")
    if da not in "Nn" or da == "":
        print("开始转换咯！")
        for files in dirs:
            matchObj = re.match(r'(.*).lrc', files, re.M | re.I)
            if matchObj:
                detcd = open(matchObj.group(), mode="rb")
                enc = chardet.detect(detcd.read())["encoding"]
                detcd.close()
                if enc == "utf-8":
                    p += 1
                else:

                    allfail = False
                    try:  # 尝试用chardet检测出的编码来解码
                        lr = open(matchObj.group(), mode='r', encoding=enc)
                        data = lr.read(-1)
                    except UnicodeDecodeError:  # 如果chardet检测错误
                        lr.close()
                        print("\n[Warning!] UnicodeDecodeError at",
                              matchObj.group(), ',try decoding it manually...')
                        enc = ""

                        for encmanually in ["gbk", "gb18030", "ansi", "utf-16", "gb2312", "utf-8", "euc-jp"]:
                            try:
                                print("    Try decoding the lrc file by",
                                      encmanually, "...")
                                lr = open(matchObj.group(), mode='r',
                                          encoding=encmanually)
                                data = lr.read(-1)
                                enc = encmanually
                                print(
                                    "Successfully decode the lrc file by", enc, "\n")
                                break
                            except UnicodeDecodeError:
                                print("    failed!")
                                lr.close()
                                if encmanually == "gb18030":
                                    allfail == True
                    lr.close()
                    if allfail != True:  # 如果全部解码失败不为真
                        data = str(data)
                        lr = open(matchObj.group(), mode='w', encoding='utf-8')
                        lr.write(data)
                        lr.close()
                        print(k+1, ":", matchObj.group(), ",",
                              "encoding:", enc, "==> utf-8")
                        k += 1
                    else:
                        numfailed += 1
                        print("[", numfailed, "]",
                              matchObj.group(), "decoding failed.")

    if k != 0:
        if p != 0:  # p pass,跳过
            if numfailed != 0:
                print("工作完毕！", numfailed, "份歌词转码失败,跳过了",
                      p, "份歌词,写入了", k, "份歌词喵~")
            else:
                print("工作完毕！跳过了", p, "份歌词,写入了", k, "份歌词喵~")
        else:
            if numfailed != 0:
                print("工作完毕！", numfailed, "份歌词转码失败,写入了", k, "份歌词喵~")
            else:
                print("工作完毕！写入了", k, "份歌词喵~")
    elif p != 0:  # 这里k=0
        if numfailed != 0:
            print("工作完毕！", numfailed, "份歌词转码失败,跳过了", p, "份歌词喵~")
        else:
            print("工作完毕！跳过了", p, "份歌词,没有找到非utf-8编码的歌词喵~")
    else:  # k=0,p=0
        if numfailed != 0:
            print("工作完毕！", numfailed, "份歌词转码失败了喵~")
        else:
            print("没有找到歌词文件喵~")


def probe(dirs):
    def cmd(command, sleep, matchObj):
        subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, encoding="utf-8")
        time.sleep(sleep)  # 等ffprobe运行
        if subp.poll() == 0:
            # print(subp.communicate()[0])
            # print("title:", json.loads(subp.communicate()[0])["format"]["tags"]["title"])
            try:
                theTitle = str(json.loads(subp.communicate()[0])[
                    "format"]["tags"]["title"])
                # print("artist:", json.loads(subp.communicate()[0])["format"]["tags"]["artist"])
                theArtist = str(json.loads(subp.communicate()[0])[
                    "format"]["tags"]["artist"])
                theName = str(json.loads(subp.communicate()[0])[
                    "format"]["filename"])
                theAlbum = str(json.loads(subp.communicate()[0])[
                    "format"]["tags"]["album"])
                # print("size:", json.loads(subp.communicate()[0])["format"]["size"])
            except KeyError:
                print("[Warning!]KeyError Caught at", matchObj)
                if int(json.loads(subp.communicate()[0])["format"]["size"]) < 20971520:
                    KeObj = re.match(r'(.*) - (.*?).mp3',
                                     matchObj, re.M | re.I)
                    if KeObj:
                        subdict = {}
                        subdict["Artist"] = KeObj.group(1).replace("_", "")
                        subdict["Name"] = KeObj.group()
                        #print("============", subdict["Name"])
                        subdict["Slice"] = False
                        subdict["Album"] = ""
                        returnDict = {}
                        returnDict[KeObj.group(2).replace("_", "")] = subdict
                        #print("keObj returnDict: ", returnDict)
                        return returnDict
                else:
                    KeObj = re.match(r'(.*) - (.*?).mp3',
                                     matchObj, re.M | re.I)
                    if KeObj:
                        subdict = {}
                        subdict["Artist"] = KeObj.group(1).replace("_", "")
                        subdict["Name"] = KeObj.group()
                        # print("============",KeObj.group(0))
                        subdict["Slice"] = True
                        subdict["Album"] = ""
                        returnDict = {}
                        returnDict[KeObj.group(2).replace("_", "")] = subdict
                        #print("returnDict: ",returnDict)
                        return returnDict

            if int(json.loads(subp.communicate()[0])["format"]["size"]) < 20971520:
                subdict = {}
                subdict["Artist"] = theArtist
                subdict["Name"] = theName
                subdict["Album"] = theAlbum
                subdict["Slice"] = False
                returnDict = {}
                returnDict[theTitle] = subdict
                #print("returnDict: ",returnDict)
                return returnDict
            else:
                subdict = {}
                subdict["Artist"] = theArtist
                subdict["Name"] = theName
                subdict["Album"] = theAlbum
                subdict["Slice"] = True
                returnDict = {}
                returnDict[theTitle] = subdict
                #print("returnDict: ",returnDict)
                return returnDict
        else:
            cmd(command, sleep, matchObj)  # 错误就重来

    k = 0
    allDict = {}
    for files in dirs:
        matchObj = re.match(r'(.*).mp3', files, re.M | re.I)
        if matchObj:
            print(k+1, ": ", matchObj.group())
            command = "ffprobe -v quiet -of json -show_format "+'"'+matchObj.group()+'"'
            # theReturn={theTitle:{"Artist":theArtist,"Name":theName,"Slice":Boolean}}
            theReturn = None
            while theReturn == None:
                # theReturn 有时会变为空值,
                theReturn = cmd(command, 0.4, matchObj.group())
            try:
                for name in theReturn:
                    allDict[name] = theReturn[name]
                    k += 1
            except TypeError:
                print(theReturn)
                input("TypeError...Please press Enter and retry...")
            except:
                print("Unknown Error...")
    #print("allDict:", allDict)
    return allDict


def main():
    dirs = os.listdir(os.getcwd())
    i = input("需要自动生成APlayer使用的js吗?(Y/n):")
    if i not in "Nn" or i == "":
        allMusicInDict = probe(dirs)
        musicConverter(allMusicInDict)
    lrcEncodingConvertToUTF8(dirs)
    input("按回车键退出...\n")
    print("呐,再见咯！")
    exit(0)


###
main()
