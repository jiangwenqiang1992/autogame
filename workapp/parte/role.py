
from workapp.Click import *
from util.jineng import skill_attack

class dizhao:
    juese_name = 'juese.png'
    dt_name = 'DNF.jpg'
    xt_name = 'guai.png'
    liangmen_name = 'blue.png'

    blue = 'blue.png'
    red = 'red.png'
    black = 'black.png'
    copper = 'copper.png'

    key = ''

    def move_up(self):
        key_down('w')
        self.key = 'w'

    def move_dowm(self):
        key_down('s')
        self.key = 's'

    def move_left(self):
        key_down('a')
        self.key = 'a'

    def move_right(self):
        key_down('d')
        self.key = 'd'

    def move_stop(self):
        key_up(self.key)


    def attack(self, zb):
        mouse_click(str(zb[0] + 25) + ',' + str(zb[1] + 25))
        skill_attack()

