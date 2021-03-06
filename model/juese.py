from time import sleep
from util import Template as tl, jietu as jt
from util.Click import *

from util.listener import a
class dizhao:

    juese_name = 'juese.png'
    dt_name = 'DNF.png'
    xt_name = 'guai.png'
    blue = 'blue.png'
    red = 'red.png'
    black = 'black.png'
    copper = 'copper.png'

    def __init__(self):
        # self.getZB()
        print()

    def getZB(self):
        jt.window_capture(self.dt_name)
        juese_zb = tl.template(self.juese_name, self.dt_name, 0.1)
        return juese_zb

    def daguai(self, threshold=0.001):
        sleep(1)
        # print('status=1;  开始打怪')
        while True:
            jt.window_capture(self.dt_name)
            zb = tl.template(xt_name=self.xt_name, dt_name=self.dt_name, threshold=threshold)
            if zb[0] != 0:
                print('有怪', '打怪')
                mouse_move(zb[0] + 25, zb[1] + 25)
                a.status = True
            else:
                print('没怪了')
                a.status = False
                break
        return self

    def get_door_status(self):
        print("判断是否开门")

        jt.window_capture(self.dt_name)
        zb1 = tl.template(self.blue, self.dt_name, 0.0001)
        if zb1[0] != 0:
            print('已开门')
            return True
        else:
            print('未开门')
        return False

    def moveTo(self, zb):
        x, y = str(zb).split(',')
        x = int(x)
        y = int(y) - 100

        if abs(self.getZB()[0] - x) > 30:
            if self.getZB()[0] > x:
                key_down('a')
                # while abs(self.getZB()[0] - x) > 50:
                while self.getZB()[0] > x:
                    sleep(0.1)
                key_up('a')
            else:
                key_down('d')
                while x > self.getZB()[0]:
                    sleep(0.1)
                key_up('d')

        if abs(self.getZB()[1] - y) > 15:
            if self.getZB()[1] > y:
                key_down('w')
                while self.getZB()[1] > y:
                    sleep(0.1)
                key_up('w')
            else:
                key_down('s')
                while y > self.getZB()[1]:
                    sleep(0.1)
                key_up('s')

        print('到达指定位置')
        self.daguai()
        return self

    def guomen(self, menFangXiang):
        print('执行过门')
        if self.get_door_status():
            if int(menFangXiang) == 8:
                key_input('w', 1)
            elif int(menFangXiang) == 6:
                key_input('d', 1)
            elif int(menFangXiang) == 2:
                key_input('s', 1)
            elif int(menFangXiang) == 4:
                key_input('a', 1)
            else:
                print('错误：',menFangXiang)
                return
        else:
            print('未开门')
            return False
        #
        # for i in range(100):
        #     jt.window_capture(self.dt_name)
        #     zb = tl.template(self.blue, self.dt_name, 0.00001)
        #     zb2 = tl.template(self.blue, self.dt_name, 0.00001)
        #     zb3 = tl.template(self.blue, self.dt_name, 0.00001)
        #     zb[0] = zb[0] + zb2[0] + zb3[0]
        #     if zb[0] == 0:
        #         print('已过门')
        #         break
        #     elif i == 19:
        #         print('过门失败')
        #         return False

        for i in range(20):
            time.sleep(1)
            jt.window_capture(self.dt_name)
            zb = tl.template(self.blue, self.dt_name, 0.00001)
            if zb[0] == 0:
                print('开图成功')
                if int(menFangXiang) == 8:
                    key_input('w', 1)
                elif int(menFangXiang) == 6:
                    key_input('d', 1)
                elif int(menFangXiang) == 2:
                    key_input('s', 1)
                elif int(menFangXiang) == 4:
                    key_input('a', 1)
                return True
            elif i == 19:
                print('开图失败')
                return False


    def mouse_click(self, zb, num=1):
        for i in range(num):
            mouse_click(zb)
        return self

    def attack_boss(self):
        for i in range(100):
            time.sleep(1)
            jt.window_capture(self.dt_name)
            zb = tl.template(self.copper, self.dt_name, 0.0000001)
            if zb[0] != 0:
                print('打boss完成')
                return True
            elif i == 99:
                print('打boss失败')
                return False
            self.daguai()


# dz = dizhao()
# dz.moveTo(150,100)
