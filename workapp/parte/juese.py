from time import sleep
from workapp import Template as tl, jietu as jt
from workapp.Click import *


class dizhao:
    # juese_name = '../image/juese.png'
    # dt_name = '../DNF.jpg'
    # xt_name = '../image/guai.png'
    # liangmen_name = '../image/kaimen.png'
    juese_name = 'juese.png'
    dt_name = 'DNF.jpg'
    xt_name = 'guai.png'
    liangmen_name = 'kaimen.png'

    def __init__(self):
        self.getZB()
    def getZB(self):
        jt.window_capture('./static/'+self.dt_name)
        juese_zb = tl.template(self.juese_name, self.dt_name, 0.1)
        return juese_zb

    def daguai(self,threshold=0.001):
        sleep(1)
        #print('status=1;  开始打怪')
        while True:
            jt.window_capture('./static/'+self.dt_name)
            zb = tl.template(xt_name=self.xt_name, dt_name=self.dt_name, threshold=threshold)
            if zb[0] != 0:
                print('有怪', '打怪')
                mouse_click(str(zb[0] + 25)+','+ str(zb[1] + 25))
            else:
                print('没怪了')
                break

    def kaimen(self):
        print("判断是否开门")
        sleep(2)
        jt.window_capture('./static/' + self.dt_name)
        zb = tl.template(self.liangmen_name, self.dt_name, 0.0001)
        if zb[0] != 0:
            print('已开门')
            return True
        else:
            print('未开门')
            return False
    def moveTo(self,zb):
        x, y = str(zb).split(',')
        x = int(x)
        y = int(y) - 120
        print('y:{}'.format(y))


        if abs(self.getZB()[0] - x) > 50:
            if self.getZB()[0] > x:
                key_down('a')
                #while abs(self.getZB()[0] - x) > 50:
                while self.getZB()[0] > x:
                    sleep(0.1)
                key_up('a')
            else:
                key_down('d')
                while x > self.getZB()[0]:
                    sleep(0.1)
                key_up('d')

        if abs(self.getZB()[1] - y) > 30:
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

    def guomen(self, menFangXiang):

        jszb1 = self.getZB()
        if menFangXiang == '上':
            clicktwo('w', 0.8)
        elif menFangXiang == '右':
            clicktwo('d', 0.8)
        elif menFangXiang == '下':
            clicktwo('s', 0.8)
        elif menFangXiang == '左':
            clicktwo('a', 0.8)

        sleep(1.5)

        jt.window_capture('./static/'+self.dt_name)
        zb = tl.template(self.liangmen_name, self.dt_name, 0.0000001)
        jszb2 = self.getZB()

        if zb[0] == 0:
            print('过图成功')
            return True
        else:
            print('过图失败')
            return False
# dz = dizhao()
# dz.moveTo(150,100)
