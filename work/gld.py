from model.juese import dizhao
from model.dungeons import dungeons
from model.brush import brush

dz = dizhao()


def reverse(br: brush):
    print('逆序执行')
    br.destination.reverse()
    # 移动到指定位置
    for move in br.destination:
        dz.moveTo(move)
        print('移动到',move)
    # 攻击固定点
    for point in br.attack_point:
        dz.mouse_click(*point)
        print('攻击固定点',*point)
    # 打怪
    dz.daguai()
    print('打怪')

    print('返回顺序')
    br.destination.reverse()


def order():
    gld = dungeons('格兰迪')

    one = brush(1)
    one.direction = 6
    one.destination.append('280,350')
    one.destination.append('780,350')

    gld.brushs.append(one)

    two = brush(2)
    two.direction = 6
    two.destination.append('280,380')
    two.destination.append('780,420')

    gld.brushs.append(two)

    three = brush(3)
    three.direction = 2
    three.destination.append('280,380')
    three.destination.append('550,420')
    three.attack_point.append(('450,300', 20))
    three.attack_point.append(('900,300', 20))

    gld.brushs.append(three)

    four = brush(4)
    four.direction = 2
    four.destination.append('630,250')
    four.destination.append('630,350')

    gld.brushs.append(four)

    five = brush(5)
    five.direction = 6
    five.destination.append('630,350')
    five.destination.append('780,350')
    five.attack_point.append(('250,300', 20))

    gld.brushs.append(five)

    six = brush(6)
    six.direction = 8
    six.attack_point.append(('300,200', 20))
    six.attack_point.append(('300,320', 20))
    six.attack_point.append(('830,200', 20))
    six.attack_point.append(('830,320', 20))
    six.destination.append('180,350')
    six.destination.append('650,280')

    seven = brush(0)

    gld.brushs.append(seven)

    for br in gld.brushs:
        print(str(br.name) + '————————————————————')
        for i in range(3):
            # 打怪
            dz.daguai()
            print('打怪')

            # 攻击固定点
            for point in br.attack_point:
                dz.mouse_click(*point)
                print('攻击固定点', *point)

            # 移动到指定位置
            for move in br.destination:
                dz.moveTo(move)
                print('移动到', move)

            if br.name == 0:
                dz.attack_boss()
                print('攻击boos')

            # 过门
            result = dz.guomen(br.direction)

            print('过门成功'+'————————————————————')

            if result:  # 过门成功
                break
            else:  # 过门失败，反向操作
                print('过门失败'+'————————————————————')
                reverse(br)


#
# dz = dizhao()
#
# dz.daguai().moveTo('780,380').guomen('右') \
#     .daguai().moveTo('780,380').guomen('右') \
#     .daguai().mouse_click('450,300', 20).mouse_click('900,300', 20).moveTo('550,300').guomen('下') \
#     .daguai().moveTo('630,350').guomen('下') \
#     .daguai().mouse_click('250,300', 20).moveTo('780,380').guomen('右') \
#     .daguai().mouse_click('300,200', 20).mouse_click('300,320', 20).mouse_click('830,200', 20) \
#     .mouse_click('830,320', 20).moveTo('650,300').guomen('上') \
#     .daguai()
