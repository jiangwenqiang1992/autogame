from time import sleep

from workapp.parte import room
from workapp.parte import role


class player:
    current_room = room.room()
    current_role = role.dizhao()

    def moveTo(self, zb):
        x, y = str(zb).split(',')
        x = int(x)
        y = int(y) - 120

        if abs(self.current_room.getRoleCoor()[0] - x) > 50:
            if self.current_room.getRoleCoor()[0] > x:
                self.current_role.move_left()
                while self.current_room.getRoleCoor()[0] > x:
                    sleep(0.1)
                self.current_role.move_stop()
            else:
                self.current_role.move_right()
                while x > self.current_room.getRoleCoor()[0]:
                    sleep(0.1)
                self.current_role.move_stop()

        if abs(self.current_room.getRoleCoor()[1] - y) > 30:
            if self.current_room.getRoleCoor()[1] > y:
                self.current_role.move_up()
                while self.current_room.getRoleCoor()[1] > y:
                    sleep(0.1)
                self.current_role.move_stop()
            else:
                self.current_role.move_dowm()
                while y > self.current_room.getRoleCoor()[1]:
                    sleep(0.1)
                self.current_role.move_stop()

        print('到达指定位置')

    def attack(self):
        while True:
            coor = self.current_room.getMonsterCoor()
            if coor[1] == 0:
                return
            else:
                self.current_role.attack(coor)

    def passDoor(self):
        if self.current_room.getDoorStatus():
            self.current_role.directionMove(direction)

