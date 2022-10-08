from src.Player import *
from src.Music import *
from src.Tool import *
import os, time
import vlc
import keyboard
import time
import random
import threading
mutex = threading.Lock()

curMusic = ''
player = Player()
ttime = ''
curname = ''
index = 0
pat = 0 # 0循环，1单曲，2随机
history = []
hisIndex = 0
def clear():
    os.system('cls')


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


def progressBar():
    #time.sleep(1)
    #mutex.acquire()
    print('\r',end='')
    curr_time = player.get_time()
    _,_,ctime = msTotime(curr_time)
    print('  '+ctime,end='\t')
    currp = int(player.get_position()*20)
    for i in range(20):
        print('-',end='')
        if(i==currp):
            print('>',end='')
    print('\t'+ttime,end='')
    #mutex.release()

def show():
    print('\r正在播放：                                                 ')
    pic = '''
    ────█▀█▄▄▄▄─────██▄
    ────█▀▄▄▄▄█─────█▀▀█
    ─▄▄▄█─────█──▄▄▄█
    ██▀▄█─▄██▀█─███▀█
    ─▀▀▀──▀█▄█▀─▀█▄█▀
    '''
    print(pic)
    print(curname)
    progressBar()


def close(tmp):
    clear()
    player.release()
    exit()

def pause():
    global player
    if(player.get_state()==1):
        player.pause()
    else:
        player.resume()


def next():
    global index,musciList,ttime,curname,player
    if(pat==2):
        index = random.randint(0,len(musciList)-1)
    else:
        if(index==len(musciList)-1):
            index = 0
        else:
            index += 1
    player.play(musciList[index].url)
    curname = musciList[index].name
    time.sleep(1)
    total_time = player.get_length()
    _,_,ttime = msTotime(total_time)
    #mutex.acquire()
    clear()
    show()
    #mutex.release()
    # TODO: 下一首

def prev():
    global index,musciList,ttime,curname,player
    if(pat==2):
        hisIndex -= 1
        index = history[hisIndex]
    else:
        if(index==0):
            index = len(musciList)-1
        else:
            index -= 1
    player.play(musciList[index])
    time.sleep(1)
    total_time = player.get_length()
    _,_,ttime = msTotime(total_time)
    mutex.acquire()
    clear()
    mutex.release()
    show()
    # TODO: 上一首

#def pattern():
    # TODO: 播放模式


if "__main__" == __name__:
    keyboard.add_hotkey('ctrl+c',close, args=('',))
    keyboard.add_hotkey('ctrl+s',pause)
    keyboard.add_hotkey('ctrl+alt+n',next)
    #player.add_callback(vlc.EventType.MediaPlayerTimeChanged, my_call_back)
    # 在线播放流媒体视频
    musciList = loadStream('./stream/qqmusic.txt')
    # for mp3 in musciList:
    #     print(mp3.name)
    player.play(musciList[0].url)
    curname = musciList[0].name
    time.sleep(1)
    total_time = player.get_length()
    _,_,ttime = msTotime(total_time)

    # 播放本地mp3
    # player.play("D:/abc.mp3")
    clear()
    show()
    #progressBar()
    # 防止当前进程退出
    #t = threading.Thread(target=progressBar)
    #t.start()
    while True:
        time.sleep(1)
        if(player.get_position()>0.1):
            next()
        progressBar()
        pass
    #t.join()