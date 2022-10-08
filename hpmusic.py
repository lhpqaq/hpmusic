from src.Player import *
from src.Music import *
import os, time

import vlc

def my_call_back(event):
    print("call:", player.get_time())

def readtxt(filename):
    with open(filename, "r",encoding='utf-8') as f:  # 打开文件
        dataline = f.read()  # 读取文件
        return dataline.splitlines()

def loadStream(path):
    re = []
    tmp = readtxt(path)
    for i in range(0,len(tmp),2):
        amusic = Music(tmp[i],tmp[i+1])
        re.append(amusic)
    return re


if "__main__" == __name__:
    player = Player()
    #player.add_callback(vlc.EventType.MediaPlayerTimeChanged, my_call_back)
    # 在线播放流媒体视频
    musciList = loadStream('./stream/qqmusic.txt')
    for mp3 in musciList:
        print(mp3.name)
    player.play(musciList[1].url)

    # 播放本地mp3
    # player.play("D:/abc.mp3")

    # 防止当前进程退出
    while True:
        if(player.get_position()>0.1):
            exit()
        pass