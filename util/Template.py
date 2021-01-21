
import cv2 as cv
import cv2
from matplotlib import pyplot as plt


# from auto import settings
from util.path import get_static_dir


def template(xt_name,dt_name,threshold=0.00001):



    # 模板图片d
    # xt_name = os.path.join(settings.BASE_DIR, "static/{}".format(xt_name))
    # dt_name = os.path.join(settings.BASE_DIR, "static/{}".format(dt_name))
    xt_name = get_static_dir() + xt_name
    dt_name = get_static_dir() + dt_name

    tpl = cv.imread(xt_name)

    # 目标图片
    target = cv.imread(dt_name)
    cv.imshow('template', tpl)
    cv.imshow('target', target)

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

        if md in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            tl = min_loc
        else:
            tl = max_loc

        # br = (tl[0] + tw, tl[1] + th)
        # 绘制矩形边框，将匹配区域标注出来
        # target：目标图像
        # tl：矩形定点
        # br：举行的宽高
        # (0,0,255)：矩形边框颜色
        # 2：矩形边框大小
        # cv.rectangle(target, tl, br, (0, 0, 255), 2)
        # cv.imshow('match-' + np.str(md), target)
        print(min_val)
        if min_val > threshold :
            tl = [0, 0]
        return tl


# cv.waitKey(0)
# cv.destroyAllWindows()

def tp2(xt_name,dt_name):
    xt_name = get_static_dir() + xt_name
    dt_name = get_static_dir() + dt_name


    img = cv.imread(dt_name, 0)
    img2 = img.copy()
    template = cv.imread(xt_name, 0)
    w, h = template.shape[::-1]

    # 6 中匹配效果对比算法
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

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

        print(meth,min_val,top_left)

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