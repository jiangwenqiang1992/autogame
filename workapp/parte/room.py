from time import sleep
from workapp import Template as tl, jietu as jt
from workapp.Click import *


class room():
    juese_name = 'juese.png'
    dt_name = 'DNF.jpg'
    xt_name = 'guai.png'
    liangmen_name = 'blue.png'


    blue = 'blue.png'
    red = 'red.png'
    black = 'black.png'
    copper = 'copper.png'


    def __init__(self):
        self.getRoleCoor()

    def getRoleCoor(self):
        jt.screenshot()
        return tl.template(self.juese_name, self.dt_name, 0.1)


    def getMonsterCoor(self):
        jt.window_capture('./static/' + self.dt_name)
        zb = tl.template(xt_name=self.xt_name, dt_name=self.dt_name, threshold=0.01)
        return zb

    def getDoorStatus(self):
        print("判断是否开门")
        for i in range(20):
            jt.window_capture(self.dt_name)
            zb1 = tl.template(self.blue, self.dt_name, 0.3)
            zb2 = tl.template(self.red, self.dt_name, 0.3)
            if zb1[0] + zb2[0] != 0:
                print('已开门')
                return True
            else:
                print('未开门')
        return False
