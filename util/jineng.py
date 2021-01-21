import threading
import time

from model.skill import skill


ice = skill('寒冰')
ice.max_time = 10
ice.left_count = 10
ice.right_count = 5

fire = skill('火焰')
fire.max_time = 10
fire.left_count = 10
fire.right_count = 5

skills = []
skills.append(ice)
skills.append(fire)

def shifang(sk:skill):
    sk.cr_time = sk.max_time
    sk.left = sk.left_count
    sk.right = sk.right_count
    print('使用技能:{}'.format(sk.name))

def attact(sk:skill,right):
    if right == 1:
        sk.right -= 1
    else:
        sk.left -= 1
    time.sleep(0.1)


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
                attact(sk,1)
                print('技能：{}，冷却：{}，右击剩余：{}'.format(sk.name,sk.cr_time,sk.right))
                return
            for i in range(sk.left):
                attact(sk,0)
                print('技能：{},冷却：{}，左击剩余：{}'.format(sk.name,sk.cr_time,sk.left))
                return
        else:
            print('技能冷却中：{}:{}，无使用次数'.format(sk.name,sk.cr_time))

for i in range(1000):
    skill_attack()

    time.sleep(0.1)
