import cv2 as cv
import cv2
from matplotlib import pyplot as plt

from util.path import get_static_dir
import os
from auto import settings
def template(xt_name, dt_name):
    # 模板图片d
    xt_name = os.path.join(settings.BASE_DIR, "static/{}".format(xt_name))
    dt_name = os.path.join(settings.BASE_DIR, "static/{}".format(dt_name))
    # xt_name = get_static_dir() + xt_name
    # dt_name = get_static_dir() + dt_name

    tpl = cv.imread(xt_name)

    # 目标图片
    target = cv.imread(dt_name)
    cv.imshow('template', tpl)
    cv.imshow('target', target)

    method = cv.TM_SQDIFF_NORMED

    # 执行模板匹配
    # target：目标图片
    # tpl：模板图片
    # 匹配模式
    result = cv.matchTemplate(target, tpl, method)
    # 寻找矩阵(一维数组当作向量,用Mat定义) 中最小值和最大值的位置

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(min_val)

    return min_val, min_loc


def template_door(xt_name, dt_name):
    dt_name = os.path.join(settings.BASE_DIR, "static/{}".format(dt_name))

    img = cv.imread(dt_name)

    a = 0  # y start
    b = 180  # y end
    c = 900  # x start
    d = 1060  # x end
    cropImg = img[a:b, c:d]  # 裁剪图像
    cv.imshow('cropImg', cropImg)

    dt_name = os.path.join(settings.BASE_DIR, "static/{}".format('jt3.png'))

    cv2.imwrite(dt_name, cropImg)  # 写入图像路径
    return template(xt_name, "jt3.png")


# cv.waitKey(0)
# cv.destroyAllWindows()

def tp2(xt_name, dt_name):
    xt_name = get_static_dir() + xt_name
    dt_name = get_static_dir() + dt_name

    img = cv.imread(dt_name, 0)
    img2 = img.copy()
    template = cv.imread(xt_name, 0)
    w, h = template.shape[::-1]

    # 6 中匹配效果对比算法
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF',
               'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()

        method = eval(meth)

        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv.rectangle(img, top_left, bottom_right, 255, 2)

        print(meth, min_val, top_left)

        plt.figure()
        plt.subplot(221)
        plt.imshow(img2, cmap="gray")
        plt.title('Original Image')
        plt.xticks([]), plt.yticks([])
        plt.subplot(222)
        plt.imshow(template, cmap="gray")
        plt.title('template Image')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(223)
        plt.imshow(res, cmap="gray")
        plt.title('Matching Result')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(224)
        plt.imshow(img, cmap="gray")
        plt.title('Detected Point')
        plt.xticks([])
        plt.yticks([])
        plt.show()

# tp2('juese.png','DNF.png')
