import threading

from pynput.keyboard import Controller, Key, Listener
import time
from util.jineng import skill_attack


class attacking:
    pass


a = attacking()
a.status = False


def attack():
    while True:
        if a.status:
            skill_attack()
            time.sleep(0.1)


# 监听按压
def on_press(key):
    try:
        if key.char == 'b':
            # print("正在按压:", key.char)
            a.status = True

    except:
        pass


# 监听释放
def on_release(key):
    try:
        if key.char == 'b':
            # print("已经释放:", key.char)
            a.status = False

    except:
        pass


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


t = threading.Thread(target=start_listen, name='LoopThread')
t.start()

t = threading.Thread(target=attack, name='LoopThread_attack')
t.start()
