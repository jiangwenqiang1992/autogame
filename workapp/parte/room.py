from workapp import Template as tl, jietu as jt


class room():
    role_png = 'juese.png'
    DNF_jpg = 'DNF.jpg'
    mounster_png = 'guai.png'
    opendoor_png = 'blue.png'


    blue = 'blue.png'
    red = 'red.png'
    black = 'black.png'
    copper = 'copper.png'

    #
    # def __init__(self):
    #     self.getRoleCoor()

    def getRoleCoor(self):
        jt.screenshot()
        return tl.template(self.role_png, self.DNF_jpg, 0.1)


    def getMonsterCoor(self):
        jt.window_capture('./static/' + self.DNF_jpg)
        zb = tl.template(xt_name=self.mounster_png, dt_name=self.DNF_jpg)
        return zb

    def getDoorStatus(self):
        print("判断是否开门")
        for i in range(20):
            jt.window_capture(self.DNF_jpg)
            zb1 = tl.template(self.blue, self.DNF_jpg, 0.3)
            zb2 = tl.template(self.red, self.DNF_jpg, 0.3)
            if zb1[0] + zb2[0] != 0:
                print('已开门')
                return True
            else:
                print('未开门')
        return False
