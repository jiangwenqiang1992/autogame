import os

import cv2 as cv

from auto import settings


def template(xt_name,dt_name,threshold=0.00001):



    # 模板图片d
    xt_name = os.path.join(settings.BASE_DIR, "static/{}".format(xt_name))
    dt_name = os.path.join(settings.BASE_DIR, "static/{}".format(dt_name))
    tpl = cv.imread(xt_name)

    # 目标图片
    target = cv.imread(dt_name)
    #cv.imshow('template', tpl)
    #cv.imshow('target', target)

    methods = [cv.TM_SQDIFF_NORMED]

    # 获得模板的高宽
    th, tw = tpl.shape[:2]
    for md in methods:

        # 执行模板匹配
        # target：目标图片
        # tpl：模板图片
        # 匹配模式
        result = cv.matchTemplate(target, tpl, md)
        # 寻找矩阵(一维数组当作向量,用Mat定义) 中最小值和最大值的位置

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc

        #br = (tl[0] + tw, tl[1] + th)
        # 绘制矩形边框，将匹配区域标注出来
        # target：目标图像
        # tl：矩形定点
        # br：举行的宽高
        # (0,0,255)：矩形边框颜色
        # 2：矩形边框大小
        #cv.rectangle(target, tl, br, (0, 0, 255), 2)
        #cv.imshow('match-' + np.str(md), target)
        if min_val > threshold :
            #print(min_val)
            tl = [0, 0]
        return tl



#cv.waitKey(0)
#cv.destroyAllWindows()