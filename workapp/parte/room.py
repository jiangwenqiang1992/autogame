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
        val,coor = tl.template(self.role_png, self.DNF_jpg)
        return coor


    def getMonsterCoor(self):
        jt.window_capture('./static/' + self.DNF_jpg)
        val,coor = tl.template(xt_name=self.mounster_png, dt_name=self.DNF_jpg)
        return coor

    def getDoorStatus(self):
        print("判断是否开门")
        for i in range(20):
            jt.window_capture(self.DNF_jpg)
            val,zb = tl.template_door("kaimen.png","DNF.jpg")
            if 0.1 > val:
                print('已开门')
                return True
            else:
                print('未开门')
        return False
