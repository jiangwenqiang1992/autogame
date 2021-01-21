from workapp.Click import *
from workapp.parte import juese

status = 1

tu = 1
tuList = {1: 2, 2: 2, 3: 4, 4: 2, 5: 2}
menList = {1: (950, 350), 2: (670, 450), 3: (950, 350), 4: (950, 300)}
menFangXiangList = {1: 2, 2: 3, 3: 2, 4: 2}

# 动作 1 移动到  2 移动 3 打怪 4 点击
dang = [{'dongzuo': [(1, (250, 300)), (3, 3), (1, (780, 300)), (3, 3)], 'fangxiang': 2},
        {'dongzuo': [(1, (250, 300)), (3, 3), (1, (780, 380)), (3, 3), (1, (640, 380))], 'fangxiang': 3},
        {'dongzuo': [(1, (670, 300)), (3, 3), (1, (200, 300)), (3, 3), (1, (780, 300))], 'fangxiang': 2},

        {'dongzuo': [(1, (670, 300)), (3, 3)], 'fangxiang': 0}]

def action():
    dz = juese.dizhao()
    for i in dang:
        # print(i['dongzuo'])

        while True:
            for u in i['dongzuo']:
                if u[0] == 1:
                    dz.moveTo(u[1][0], u[1][1])
                elif u[0] == 2:
                    move(u[1][0], u[1][1])
                elif u[0] == 3:
                    dz.daguai()
                elif u[0] == 4:
                    mouse_click(u[1][0], u[1][1])

            if dz.kaimen():
                if dz.guomen(i['fangxiang']):
                    break

        # print(i['fangxiang'])