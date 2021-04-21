from tenacity import retry, stop_after_attempt

from workapp.Click import *
from workapp.parte import role
from .celeryconfig import app

from brush.models import Checkpoint, Actionstep
from .parte.player import player


@app.task()
def yibu():
    print('start yibu')
    # time.sleep(10)
    dz = role.dizhao()
    dz.getZB()
    print('end yibu')


def test1():
    '''幽暗密林剧情1'''
    dz = role.dizhao()
    dz.moveTo('250,300')
    dz.moveTo('780,400')
    dz.guomen('右')


def runAction(ac, er):
    type = int(ac.type)

    time.sleep(1)
    if type == 1:
        print('移动到', ac.content)
        er.moveTo(ac.content)
    elif type == 2:
        print('双击按键', ac.content)
        clicktwo(ac.content)
    elif type == 3:
        print('执行打怪')
        er.attack()
    elif type == 4:
        print('执行鼠标点击{}'.format(ac.content))
        for i in range(int(ac.actionNum) + 1):
            mouse_click(ac.content)
    elif type == 5:
        print('执行键盘按键{}'.format(ac.content))
        for i in range(int(ac.actionNum)):
            clickone(ac.content)
    elif type == 6:
        print('延迟{}秒'.format(ac.content))
        time.sleep(int(ac.content))
    elif type == 7:
        print('键盘{}长按{}秒'.format(ac.content, ac.actionNum))
        key_down(ac.content)
        time.sleep(int(ac.actionNum))
        key_up(ac.content)


def runActions(actions, ck):
    er = player()

    count = 3
    while count > 0:
        print('正序执行')
        for ac in actions:
            print(ac.Checkpoint.checkpointname, ac.actionstep)
            print(ac.type)
            runAction(ac, er)
        print('正序执行结束')

        if '任务' in ck.checkpointname:
            return 1

        if er.passDoor():
            return True
        else:
            print('逆序执行')
            actionsnx = actions.reverse()
            for ac in actionsnx:
                print(ac.Checkpoint.checkpointname, ac.actionstep)
                print(ac.type)
                runAction(ac,er)
            print('逆序执行结束')

        if ck.checkpointname == 'BOSS关':
            print('打完BOSS')
            return 1

        count -= 1
    raise Exception("未开门，已逆序执行")


def testcheckpoint():
    cks = Checkpoint.objects.filter(checkpointname="BOSS前关").all()
    for ck in cks:
        actions = Actionstep.objects.filter(Checkpoint=42).all()
        runActions(actions, ck)


def runworktask(dungeonsname):
    Checkpoints = Checkpoint.objects.filter(Dungeons__dungeonstname__exact=dungeonsname).all()
    for ck in Checkpoints:
        actions = ck.actionstep_checkpoint.order_by('actionstep').all()
        runActions(actions, ck)


@app.task()
def clicktesttask(zb):
    for i in range(10):
        mouse_click(zb)
