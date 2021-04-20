import threading
import time
from util.Click import *
from model.skill import skill


zf = skill('原力增幅')
zf.max_time = 100
zf.left_count = 0
zf.right_count = 0
zf.key = 'ddz'

ice = skill('寒冰')
ice.max_time = 10
ice.left_count = 10
ice.right_count = 5
ice.left_sleep = 0.2
ice.right_sleep = 0.6
ice.left_count = 7
ice.right_count = 3
ice.key = 'sdz'

fire = skill('火焰')
fire.max_time = 10
fire.left_count = 10
fire.right_count = 5
fire.left_sleep = 0.2
fire.right_sleep = 0.8
fire.right_count = 9
fire.key = 'dz'

sh = skill('守护')
sh.max_time = 10
sh.left_count = 0
sh.right_count = 2
sh.key = 'dwz'

feng = skill('feng')
feng.max_time = 28
feng.left_count = 0
feng.right_count = 7
feng.key = 'sdz'

zmkx = skill('终末狂想')
zmkx.max_time = 46
zmkx.left_count = 1
zmkx.right_count = 0
zmkx.key = 'wsz'

gz = skill('构造')
gz.max_time = 35
gz.left_count = 1
gz.right_count = 0
gz.key = 'waz'

xk = skill('虚空')
xk.max_time = 46
xk.left_count = 1
xk.right_count = 0
xk.key = 'ssz'

skills = []
skills.append(zf)
skills.append(zmkx)
skills.append(xk)
skills.append(gz)
skills.append(feng)
skills.append(sh)
skills.append(ice)
skills.append(fire)
def shifang(sk: skill):
    sk.cr_time = sk.max_time
    sk.left = sk.left_count
    sk.right = sk.right_count
    print('使用技能:{}'.format(sk.name), sk.key)
    key_input(sk.key)
    time.sleep(0.7)
def attact(sk: skill, right):
    if right == 1:
        sk.right -= 1
        mouse_right_click()
    else:
        sk.left -= 1
        mouse_left_click()
    time.sleep(0.2)


def update():
    while True:
        for sk in skills:
            if sk.cr_time > 0:
                sk.cr_time -= 1
        time.sleep(1)


t = threading.Thread(target=update, name='LoopThread')
t.start()


def skill_attack():
    for sk in skills:
        if sk.cr_time == 0:
            shifang(sk)

        if sk.cr_time > 0:
            for i in range(sk.right):
                attact(sk, 1)
                print('技能：{}，冷却：{}，右击剩余：{}'.format(sk.name, sk.cr_time, sk.right))
                return
            for i in range(sk.left):
                attact(sk, 0)
                print('技能：{},冷却：{}，左击剩余：{}'.format(sk.name, sk.cr_time, sk.left))
                return
        else:
            print('技能冷却中：{}:{}，无使用次数'.format(sk.name, sk.cr_time))

# for i in range(1000):
#     skill_attack()
#
#     time.sleep(0.1)
