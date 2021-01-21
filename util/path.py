

import os


def get_root_dir():
    dir_path = os.path.realpath(__file__)  # 获取当前路径
    dir_path = os.path.dirname(dir_path)
    dir_path = os.path.dirname(dir_path)
    return dir_path


def get_static_dir():
    path = get_root_dir() + "\\util\\static\\"
    return path

print(get_static_dir())

